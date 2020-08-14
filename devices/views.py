from django.shortcuts import render, HttpResponse
from .models import Sucursal,Devices,TypeDevices,DataReadings
from datetime import date
from datetime import datetime,timedelta
import json as simplejson
from django.core.serializers.json import DjangoJSONEncoder
import json
from decimal import Decimal
from django.db import connection
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.utils.dateparse import parse_datetime
import io
from django.http import FileResponse

from django.views import View

import pyautogui

import itertools
from random import randint
from statistics import mean
from reportlab.lib.pagesizes import A4,letter, landscape
from reportlab.pdfgen import canvas
from reportlab.lib.colors import pink, black, red, blue, green, gray,white
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, Table, TableStyle, SimpleDocTemplate
from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT, TA_CENTER 
from reportlab.lib import colors
from reportlab.lib.units import cm
# Create your views here.
def home(request):
    if request.method == 'POST':
        idsucur = request.POST['sucur']
    else:
        idsucur = "1"
    variable = ""
    sucursal = Sucursal.objects.all()
    devices = Devices.objects.filter(id_sucursal=idsucur)
    agrup = Devices.objects.raw('SELECT de.id,de.id_sucursal ,de.updated_at,de.agrupado,COUNT(de.agrupado) as cont, sum(if(if(f_security_d(de.ultimo_valor_aes,3264)>0,f_security_d(de.ultimo_valor_aes,3264)>=f_security_d(par.valor_aes,5710) or f_security_d(de.ultimo_valor_aes,3264)<=f_security_d(par.valor_minimo_aes,5710),f_security_d(de.ultimo_valor_aes,3264)<=f_security_d(par.valor_aes,5710) or f_security_d(de.ultimo_valor_aes,3264)>=f_security_d(par.valor_minimo_aes,5710)),1,0)) as iden FROM aresm2m_hofarm.devices as de inner join aresm2m_hofarm.parameter_alerta as par on de.id = par.id_device WHERE de.id_sucursal='+idsucur+' GROUP BY de.agrupado')
    caja = Devices.objects.raw('SELECT de.id, de.id_tipo_componente,de.agrupado,de.ubicacion,f_security_d(de.valor_maximo_aes,3264) as valor_maximo,f_security_d(de.valor_minimo_aes,3264) as vlor_minimo,de.ultimo_fecha,f_security_d(de.ultimo_valor_aes,3264) as ultimo_valor,f_security_d(par.valor_aes,5710) as maxi,f_security_d(par.valor_minimo_aes,5710) as mini,par.valor_minimo minimo,par.valor maximo FROM aresm2m_hofarm.devices as de inner join aresm2m_hofarm.parameter_alerta as par on de.id = par.id_device where de.id_sucursal = '+idsucur+' order by de.agrupado,de.id_tipo_componente')  
    #agrup.refresh_from_db()
    return render(request,"devices/home.html",{'idsucur':idsucur,'sucursal':sucursal,'devices': devices,'agrup':agrup,'caja':caja,'variable':variable});
    
def backup(request):
    if request.GET.get('agrup'):
        agrupado = request.GET['agrup']
    if request.GET.get('sucur'):
        sucursal = request.GET['sucur']
    fecha = datetime.now()
    today = fecha.strftime("%Y-%m-%dT%H:%M:%S")
    todaynew = fecha.strftime("%Y-%m-%dT00:00:00")
    todgrafic = fecha.strftime("%d-%m-%Y")
    if request.POST.get('desdegrafica'):
        desdegrafica = request.POST['desdegrafica']
    else:
        desdegrafica = todaynew
    if request.POST.get('hastagrafica'):
        hastagrafica = request.POST['hastagrafica']
    else:
        hastagrafica = today
    
    if request.POST.get('desdetabla'):
        desdetabla = request.POST['desdetabla']
    else:
        desdetabla = todaynew

    if request.POST.get('hastatabla'):
        hastatabla = request.POST['hastatabla']
    else:
        hastatabla = today
    hastat = parse_datetime(hastatabla)
    ht = hastat.strftime("%d-%m-%Y")
    desdet = parse_datetime(desdetabla)
    dt = desdet.strftime("%d-%m-%Y")

    hasgraf = parse_datetime(hastagrafica)
    hg = hasgraf.strftime("%d-%m-%Y")
    desgraf = parse_datetime(desdegrafica)
    dg = desgraf.strftime("%d-%m-%Y")
    """rangos grafica"""
    rangos = Devices.objects.raw('SELECT distinct de.id,de.agrupado,de.id_tipo_componente as itc,f_security_d(par.valor_aes,5710) as maxi,f_security_d(par.valor_minimo_aes,5710) as mini FROM aresm2m_hofarm.parameter_alerta as par inner join aresm2m_hofarm.devices as de ON par.id_device = de.id where de.agrupado = "'+agrupado+'" order by de.agrupado')
    for rangos in rangos:
        if rangos.itc == '2' :
            ranmintem = rangos.mini
            ranmaxtem = rangos.maxi
        if rangos.itc == '7' :
            ranminhum = rangos.mini
            ranmaxhum = rangos.maxi

    if request.POST.get('temin'):
        temin = request.POST['temin']
    else:
        temin = ranmintem

    if request.POST.get('temax'):
        temax = request.POST['temax']
    else:
        temax = ranmaxtem

    if request.POST.get("humin"):
        humin = request.POST['humin']
    else:
        try:
            humin = ranminhum
        except:
            humin = 30
    if request.POST.get("humax"):
        humax = request.POST['humax']
    else:
        try:
            humax = ranmaxhum 
        except:
            humax = 60

    teminimo = simplejson.dumps(temin)
    temaximo = simplejson.dumps(temax)
    huminimo = simplejson.dumps(humin)
    humaximo = simplejson.dumps(humax)

    ubicacion = DataReadings.objects.raw('SELECT distinct de.id,de.ubicacion as ubicacion,de.id_tipo_componente as tipo_comp FROM aresm2m_hofarm.data_readings as dr inner join aresm2m_hofarm.devices as de on dr.id_device = de.id where de.agrupado = "'+agrupado+'"')
    #agrup = Devices.objects.raw('SELECT de.id,de.id_sucursal as id_sucursal ,de.id_tipo_componente as id_tipo_componente ,de.updated_at as updated_at,de.agrupado as agrupado,COUNT(de.agrupado) as cont, if(f_security_d(de.ultimo_valor_aes,3264)>f_security_d(par.valor_aes,5710) or f_security_d(de.ultimo_valor_aes,3264)<f_security_d(par.valor_minimo_aes,5710) ,1,0) as iden FROM aresm2m_hofarm.devices as de inner join aresm2m_hofarm.parameter_alerta as par on de.id = par.id_device WHERE de.agrupado ="'+agrupado+'" GROUP BY de.id_tipo_componente')
    agrup = Devices.objects.raw('SELECT de.id,de.id_sucursal as id_sucursal ,de.id_tipo_componente as id_tipo_componente ,de.updated_at as updated_at,de.agrupado as agrupado,COUNT(de.agrupado) as cont, sum(if(f_security_d(de.ultimo_valor_aes,3264)>f_security_d(par.valor_aes,5710) or f_security_d(de.ultimo_valor_aes,3264)<f_security_d(par.valor_minimo_aes,5710) ,1,0)) as iden FROM aresm2m_hofarm.devices as de inner join aresm2m_hofarm.parameter_alerta as par on de.id = par.id_device WHERE de.agrupado ="'+agrupado+'" GROUP BY de.id_tipo_componente')
    #agrup = Devices.objects.raw('SELECT id,id_sucursal as suc, updated_at,id_tipo_componente,agrupado,COUNT(agrupado) as cont FROM devices WHERE agrupado ="'+agrupado+'" GROUP BY id_tipo_componente')
    caja = Devices.objects.raw('SELECT de.id, de.id_tipo_componente,de.agrupado,de.ubicacion as ubicacion,f_security_d(de.valor_maximo_aes,3264) as valor_maximo,f_security_d(de.valor_minimo_aes,3264) as valor_minimo,de.ultimo_fecha,f_security_d(de.ultimo_valor_aes,3264) as ultimo_valor,f_security_d(par.valor_aes,5710) as maxi,f_security_d(par.valor_minimo_aes,5710) as mini,par.valor_minimo minimo,par.valor maximo FROM aresm2m_hofarm.devices as de inner join aresm2m_hofarm.parameter_alerta as par on de.id = par.id_device where de.agrupado = "'+agrupado+'" order by de.agrupado')
    cabecera = []
    fechagraf = []
    anexo1 = []
    anexo2 = []
    anexo3 = []
    anexo4 = []
    color1 = []
    border1 = []
    color2 = []
    border2 = []
    color3= []
    border3 = []
    color4 = []
    border4 = []
    anexofech =[]
    dataubica = []
    prueba1 = []
    prueba2 = []
    prueba3 = []
    prueba4 = []
    pruebafech = []
    tbl = []

    """cabecera"""
    for ubi2 in ubicacion:
        if ubi2.tipo_comp == '2':
            cabecera.append(agrupado+'-'+ubi2.ubicacion+'|'+'Temp.')
        else:
            cabecera.append(agrupado+'-'+ubi2.ubicacion+'|'+'Hum.')
    ###cabecera.append(agrupado+'-'+caja.ubicacion+'|'+agrup.id_tipo_componente)
    ancho = len(cabecera)
    """tabla"""
    pr = connection.cursor()
    pr.callproc('sp_reporteG_historico',[dt,ht,1,sucursal,0,3000,1])
    pec = [i[0] for i in pr.description]
    pruebatab = [dict(zip(pec,row)) for row in pr.fetchall()]
   
    for pruebatab in pruebatab:
        if len(cabecera) == 4 :
            try:
                valp1 = pruebatab[cabecera[0]]                   
            except:
                valp1 = ''  
            try: 
                valp2 = pruebatab[cabecera[1]]                         
            except:
                valp2 = ''
            try:
                valp3 = pruebatab[cabecera[2]]                         
            except:
                valp3 = ''
            try:
                valp4 = pruebatab[cabecera[3]]                          
            except:
                pass
            datfech = pruebatab['Fecha']+' '+pruebatab['Hora']
            tbl.append({
                'fetch':datfech,
                'valprueba1':valp1,
                'valprueba2':valp2,
                'valprueba3':valp3,
                'valprueba4':valp4,
                })
        elif len(cabecera) == 2 :
            try:
                valp1 = pruebatab[cabecera[0]]                   
            except:
                pass
            try: 
                valp2 = pruebatab[cabecera[1]]                         
            except:
                pass
            datfech = pruebatab['Fecha']+' '+pruebatab['Hora']
            tbl.append({
                'fetch':datfech,
                'valprueba1':valp1,
                'valprueba2':valp2
                })
        else:
            try:
                valp1 = pruebatab[cabecera[0]]                   
            except:
                pass
            datfech = pruebatab['Fecha']+' '+pruebatab['Hora']
            try:
                tbl.append({
                'fetch':datfech,
                'valprueba1':valp1
                })
            except:
                pass

    if request.POST.get('page'):
        page = request.POST['page']
    else:
        page = 1
    #page = request.GET.get('page',1)
    paginator = Paginator(tbl, 10)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)

    pr.close()
    connection.close()

    """grafica"""
    cur = connection.cursor()
    cur.callproc('sp_reporteG_historico',[dg,hg,1,sucursal,0,3000,1])
    #cur.callproc('sp_reporteG_diario',[todgrafic,todgrafic,2,sucursal,3,agrupado,0,300])
    #datagraf = cur.fetchall()
    rec = [i[0] for i in cur.description]
    datagraf = [dict(zip(rec,row)) for row in cur.fetchall()]
    try:
        for datagraf in datagraf:
            try:
                val1 = float(datagraf[cabecera[0]])
                anexo1.append(val1)
                color1.append('rgba(0, 211, 24, 1)')
                border1.append('rgba(0, 211, 24, 1)')
            except:
                val1 = ''
                anexo1.append(val1)
                color1.append('rgba(0, 211, 24, 1)')
                border1.append('rgba(0, 211, 24, 1)')
            try: 
                val2 = float(datagraf[cabecera[1]])
                anexo2.append(val2)
                color2.append('rgba(255, 153, 0, 1)')
                border2.append('rgba(255, 153, 0, 1)')
            except:
                pass
            try:
                val3 = float(datagraf[cabecera[2]])
                anexo3.append(val3)
                color3.append('rgba(38, 221, 242, 1)')
                border3.append('rgba(38, 221, 242, 1)')      
            except:
                val3 = ''
                anexo3.append(val3)
                color3.append('rgba(38, 221, 242, 1)')
                border3.append('rgba(38, 221, 242, 1)') 
            try:
                val4 = float(datagraf[cabecera[3]])
                anexo4.append(val4)
                color4.append('rgba(56, 0, 211, 1)')
                border4.append('rgba(56, 0, 211, 1)')
                
            except:
                pass
            datefech = datagraf['Fecha']+' '+datagraf['Hora']
            anexofech.append(datefech)
    except:
        pass
    
    cur.close()
    connection.close()
    ubicaciongraf = []
    for ubi in ubicacion:
        if ubi.tipo_comp == '2':
            ubicaciongraf.append(ubi.ubicacion+' Temperatura')
        else:
            ubicaciongraf.append(ubi.ubicacion+' Humedad')
    try:
        tit1 = simplejson.dumps(ubicaciongraf[0])    
    except:
        pass
    try:
        tit2 = simplejson.dumps(ubicaciongraf[1])
    except:
        pass
    try:
        tit3 = simplejson.dumps(ubicaciongraf[2])
    except:
        pass
    try:
        tit4 = simplejson.dumps(ubicaciongraf[3])
    except:
        pass
    titgeneral=[]
    try:
        titgeneral.append(tit1)
        titgeneral.append(tit2)
        titgeneral.append(tit3)
        titgeneral.append(tit4)
    except:
        pass
    
    return render(request,"devices/backup.html",{'ancho':ancho,'sucursal':sucursal,'humin':humin,'humax':humax,'temin':temin,'temax':temax,'pruebatab':pruebatab,'desdetabla':desdetabla,'hastatabla':hastatabla,'hastagrafica':hastagrafica,'desdegrafica':desdegrafica,'tbl':tbl,'cabecera':cabecera,'dt':dt,'ht':ht,'border1':border1,'color1':color1,'border2':border2,'color2':color2,'border3':border3,'color3':color3,'border4':border4,'color4':color4,'users':users,'titgeneral':titgeneral,'anexofech':anexofech,'agrupado':agrupado,'anexo1':anexo1,'anexo2':anexo2,'anexo3':anexo3,'anexo4':anexo4,'ubicacion':ubicacion,'dataubica':dataubica,'agrup':agrup,'caja':caja,'agrupado':agrupado,'teminimo':teminimo,'temaximo':temaximo,'humaximo':humaximo,'huminimo':huminimo});

def login(request): 
    return render(request,"devices/login.html");

def about(request):
    return render(request,"devices/about.html");

def dashboard_geren(request):
    return render(request,"devices/dashboard_geren.html");

def historial_alertas(request):
   return render(request,"devices/historial_alertas.html");

def historico_general(request):

    #owners = Owners.objects.all()s
    return render(request,"devices/historico_general.html");

def reporte_alerta(request):
   return render(request,"devices/reporte_alerta.html");

def reporte_diario(request):
   return render(request,"devices/reporte_diario.html");

def reporte_mkt(request):
   return render(request,"devices/reporte_mkt.html");

def ubicaciones(request):
  return render(request,"devices/ubicaciones.html");

def generatepdf(request):
    if request.GET.get('agrup'):
        agrupado = request.GET['agrup']
    if request.GET.get('sucur'):
        sucursal = request.GET['sucur']
    if request.GET.get('desde'):
        desdegrafica = request.GET['desde']
    if request.GET.get('hasta'):
        hastagrafica = request.GET['hasta']

    hasgraf = parse_datetime(hastagrafica)
    hg = hasgraf.strftime("%d-%m-%Y")
    desgraf = parse_datetime(desdegrafica)
    dg = desgraf.strftime("%d-%m-%Y")
    cabecera = []
    tbl = []
    ubicacion = DataReadings.objects.raw('SELECT distinct de.id,de.ubicacion as ubicacion,de.id_tipo_componente as tipo_comp FROM aresm2m_hofarm.data_readings as dr inner join aresm2m_hofarm.devices as de on dr.id_device = de.id where de.agrupado = "'+agrupado+'"')
    """cabecera"""
    for ubi2 in ubicacion:
        if ubi2.tipo_comp == '2':
            cabecera.append(agrupado+'-'+ubi2.ubicacion+'|'+'Temp.')
        else:
            cabecera.append(agrupado+'-'+ubi2.ubicacion+'|'+'Hum.')
    """tabla"""
    rc = connection.cursor()
    rc.callproc('sp_reporteG_historico',[dg,hg,1,sucursal,0,3000,1])
    pecr = [i[0] for i in rc.description]
    pri = [dict(zip(pecr,row)) for row in rc.fetchall()]
    data = []
    datacabecera = []
    if len(cabecera) == 4 :
        data.append(['Camara','Fecha','Promedio',cabecera[0],cabecera[1],cabecera[2],cabecera[3]])
        datacabecera.append(['Camara','Fecha','Promedio',cabecera[0],cabecera[1],cabecera[2],cabecera[3]])
    elif len(cabecera) == 2 :
        data.append(['Camara','Fecha','Promedio',cabecera[0],cabecera[1]])
        datacabecera.append(['Camara','Fecha','Promedio',cabecera[0],cabecera[1]])
    else:
        data.append(['Camara','Fecha','Promedio',cabecera[0]])
        datacabecera.append(['Camara','Fecha','Promedio',cabecera[0]])
    for i in pri:
        if len(cabecera) == 4 :
            try:
                valp1 = i[cabecera[0]]                   
            except:
                valp1 = ''
            try: 
                valp2 = i[cabecera[1]]                         
            except:
                pass
            try:
                valp3 = i[cabecera[2]]                    
            except:
                valp3 = ''
            try:
                valp4 = i[cabecera[3]]                          
            except:
                pass
            datfech = i['Fecha']+' '+i['Hora']
            prom = (float(valp1)+float(valp2)+float(valp3)+float(valp4)) / 4
            promedio = round(prom,2)
            data.append([agrupado,datfech,promedio,valp1,valp2,valp3,valp4])
        elif len(cabecera) == 2 :
            try:
                valp1 = i[cabecera[0]]                   
            except:
                pass
            try: 
                valp2 = i[cabecera[1]]                         
            except:
                pass
            datfech = i['Fecha']+' '+i['Hora']
            prom = (float(valp1)+float(valp2)) / 2
            promedio = round( prom,2)
            data.append([agrupado,datfech,promedio,valp1,valp2])
        else:
            try:
                valp1 = i[cabecera[0]]                   
            except:
                pass
            datfech = i['Fecha']+' '+i['Hora']
            promedio = valp1
            data.append([agrupado,datfech,promedio,valp1])
    rc.close()
    connection.close()
    buffer = io.BytesIO()
    # Create the PDF object, using the buffer as its "file."
    p = canvas.Canvas(buffer,pagesize=landscape(letter))
    w, h = A4
    max_rows_per_page = 28
    x_offset = 50
    y_offset = 345 
    padding = 15
    if len(cabecera) == 4 :
        xlist = [x + x_offset for x in [0, 100, 200, 300, 400, 500, 600, 700]]
    elif len(cabecera) == 2 :
        xlist = [x + x_offset for x in [0, 100, 200, 300, 400, 500]]
    else:
        xlist = [x + x_offset for x in [0, 100, 200, 300, 400]]
    ylist = [h - y_offset - i*padding for i in range(max_rows_per_page + 1)] 
    ylist2 = [h - 330 - i*padding for i in [0, 1]]
    for rows in grouper(data,max_rows_per_page):
        p.drawImage( "D:/aresM2m/hofarmdjango/hofarm_py/hofarm/devices/static/devices/img/logo_cliente.png",40, 500, 120, 90,preserveAspectRatio=True)
        p.setFont("Helvetica-Bold", 20)
        p.drawString(300, 550, "REPORTE DE CÁMARAS")
        p.setFont("Helvetica-Bold", 11.5)
        p.drawString(315, 530, "FECHA DEL: "+ dg +" al " + hg)
        p.setFont("Helvetica", 9)
        rows = tuple(filter(bool, rows))
        #p.setFillColor(gray)
        
        p.setStrokeColorRGB(0.8, 0.8, 0.8)
        #p.setFillColor(blue)
        #p.grid(xlist,ylist2)
        #for x,cell1 in zip(xlist,datacabecera):
        #    p.drawCentredString(x + 100, 501 , str(cell1))
        p.grid(xlist, ylist[:len(rows) + 1])
        for y, row in zip(ylist[:-1], rows):
            for x, cell in zip(xlist, row):
                p.drawCentredString(x + 50, y - padding + 4, str(cell))
        p.showPage()
    #p.showPage()
    p.save()
    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True,filename='Camara'+agrupado+dg+'.pdf');


def coord(x, y, unit=1):
        x, y = x * unit, height - y * unit
        return x, y

def grouper(iterable,n):
    #num_groups = len(inputs) // n
    #return [tuple(inputs[i*n:(i+1)*n]) for i in range(num_groups)]
    args = [iter(iterable)] * n
    return itertools.zip_longest(*args)
    #args = [iter(inputs)]*n
    #return zip(*args)

def capturagrafico(request):
    """captura = pyautogui.screenshot()
    captura.save(r'C:/Users/Personal/Downloads/grafico.jpg')"""
    #im = pyscreenshot.grab()
    #im.save("screenshot.png")
    response = HttpResponse(captura, content_type='image/png')
    response['Content-Disposition'] = 'attachment'
    return response
