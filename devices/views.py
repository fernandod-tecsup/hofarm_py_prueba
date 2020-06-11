from django.shortcuts import render, HttpResponse
from .models import Sucursal,Devices,TypeDevices
from datetime import date
from datetime import datetime,timedelta
# Create your views here.
def home(request):
    if request.method == 'POST':
        idsucur = request.POST['sucur']
    else:
        idsucur = "1"
    variable = ""
    sucursal = Sucursal.objects.all()
    devices = Devices.objects.filter(id_sucursal=idsucur)
    agrup = Devices.objects.raw('SELECT id,updated_at,agrupado,COUNT(*) as cont FROM devices WHERE id_sucursal='+idsucur+' GROUP BY agrupado')
    caja = Devices.objects.raw('SELECT de.id, de.id_tipo_componente,de.agrupado,de.ubicacion,f_security_d(de.valor_maximo_aes,3264) as valor_maximo,f_security_d(de.valor_minimo_aes,3264) as vlor_minimo,de.ultimo_fecha,f_security_d(de.ultimo_valor_aes,3264) as ultimo_valor,f_security_d(par.valor_aes,5710) as max,f_security_d(par.valor_minimo_aes,5710) as mini,par.valor_minimo minimo,par.valor maximo FROM aresm2m_hofarm.devices as de inner join aresm2m_hofarm.parameter_alerta as par on de.id = par.id_device where de.id_sucursal = '+idsucur+' order by de.agrupado,de.id_tipo_componente')
    
    return render(request,"devices/home.html",{'sucursal':sucursal,'devices': devices,'agrup':agrup,'caja':caja,'variable':variable});

def backup(request):
    if request.method == 'POST':
        desd = request.POST['desde']
        hast = request.POST['hasta']
    else:
        desd = datetime.now()
        desde = desd + timedelta(days = -1)
        hasta = datetime.now()
    agrupado = "AL1"
    sucursal = Sucursal.objects.all()
    devices = Devices.objects.filter(id_sucursal=1)
    agrup = Devices.objects.raw('SELECT id,id_tipo_componente,updated_at,agrupado,COUNT(*) as cont FROM devices WHERE id_sucursal=1 and agrupado = "AL1" GROUP BY id_tipo_componente')
    caja = Devices.objects.raw('SELECT id, id_tipo_componente,state,orden,agrupado,ubicacion,valor_maximo,valor_minimo,valor_promedio,ultimo_fecha,ultimo_valor FROM aresm2m_hofarm.devices where id_sucursal = 1 AND agrupado = "AL1" order by agrupado')
    return render(request,"devices/backup.html",{'sucursal':sucursal,'devices': devices,'agrup':agrup,'caja':caja,'agrupado':agrupado});

def login(request): 
    return render(request,"devices/login.html");

def about(request):
    return render(request,"devices/about.html");

def dashboard_geren(request):
    return render(request,"devices/dashboard_geren.html");

def historial_alertas(request):
   return render(request,"devices/historial_alertas.html");

def historico_general(request):

    #owners = Owners.objects.all()
    
    return render(request,"devices/historico_general.html");

def reporte_alerta(request):
   return render(request,"devices/reporte_alerta.html");

def reporte_diario(request):
   return render(request,"devices/reporte_diario.html");

def reporte_mkt(request):
   return render(request,"devices/reporte_mkt.html");

def ubicaciones(request):
  return render(request,"devices/ubicaciones.html");
