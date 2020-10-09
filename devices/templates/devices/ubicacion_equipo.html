{% extends "devices/home_base.html" %}
{% block cabecera%}
{% load static %}
        <div class="col-12 font-weight-bolder" >
            <label style="margin-left: 30px; margin-top: 5px; font-size: 25px; font-family:'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;">
                <img src="{% static 'devices/img/direccion4.png' %}"> {{ agrupado }}
            </label>
            <a id="btnpdfhtml" href="" style="margin-right: 18px;" class="btn btn-info float-right" ><img src="{% static 'devices/img/printer.svg' %}"> Imprimir</a>       
        </div>     
{% endblock %}
{% block cardbody %}
{% load static %}
    <div class="card-body" style="padding-top: 13px; padding-bottom: 0px;">
        <div class="form-group" style="margin-left: 5px;">   
            <form class="form" action="" method="POST">
                {% csrf_token %}
                <div class="input-group row">
                    <div class="input-group-prepend">
                        <label class="input-group-text" for="inputGroupSelect01">Desde: </label>
                    </div>
                    <input class="form-control col-2" style="width: 50px;" type="datetime-local" name="desdegrafica" value="{{ desdegrafica }}"/>
                    <div class="input-group-prepend" style="margin-left: 10px;">
                        <label class="input-group-text" for="inputGroupSelect01">Hasta: </label>
                    </div>
                    <input class="form-control col-2" style="width: 50px;" type="datetime-local" name="hastagrafica" value="{{ hastagrafica }}"/>
                    <div style="margin-left: 10px;">
                        <button class="btn btn-info" type="submit" ><img src="{% static 'devices/img/search.svg' %}"></button>
                    </div> 
                </div>       
            </form>       
        </div>
    </div>
    <div class=" border-top" style="background: #fafafa; padding: 0px;">
        <a href="">
        <img src="{% static 'devices/img/ajustes2.png' %}" style="margin: 5px;" />
        <small class="text-info">Panel de configuracion del grafico</small>
        </a>
    </div>
{% endblock %}
    {% block content%}
    {% load static %}
    <div class="row" style="margin: 8px;">   
            <div class="col-sm-12" style="margin-top: 10px; margin-bottom: 20px;">   
                <div class="card border-info">
                    <div style="background-color: #00bcd4; padding: 10px; font-size: 17px;" class="card-header border-success text-light">
                        Diagrama
                    </div>
                    <div class="card-body" id="grafico">
                        <div class="row">
                            <div class="form-group col-12">   
                                <form class="form" action="" method="POST">
                                    {% csrf_token %} 
                                    <div class="input-group">
                        <!-- ...............................................      -->
                                        <div class="input-group-prepend" >
                                            <label class="input-group-text" style="border-top-left-radius: 20px;border-bottom-left-radius: 20px;" for="inputGroupSelect01">Min. Temperatura: </label>
                                        </div>
                                        <input id="temin" class="form-control" style="border-top-right-radius: 20px;border-bottom-right-radius: 20px;" type="number" name="temin" value="{{ temin|safe }}"/>
                                        <div class="input-group-prepend" style="margin-left: 30px;">
                                            <label class="input-group-text" style="border-top-left-radius: 20px;border-bottom-left-radius: 20px;" for="inputGroupSelect01">Max. Temperatura: </label>
                                        </div>
                                        <input id="temax" class="form-control" style="border-top-right-radius: 20px;border-bottom-right-radius: 20px;" type="number" name="temax" value="{{ temax|safe }}"/>
                        <!-- ...............................................      -->                
                                        <div class="input-group-prepend" style="margin-left: 30px;">
                                            <label class="input-group-text" style="border-top-left-radius: 20px;border-bottom-left-radius: 20px;" for="inputGroupSelect01">Min. Humedad: </label>
                                        </div>
                                        <input id="humin" class="form-control" style="border-top-right-radius: 20px;border-bottom-right-radius: 20px;" type="number" name="humin" value="{{ humin|safe }}"/>
                                        <div class="input-group-prepend" style="margin-left: 30px;">
                                            <label class="input-group-text" style="border-top-left-radius: 20px;border-bottom-left-radius: 20px;" for="inputGroupSelect01">Max. Humedad: </label>
                                        </div>                       
                                        <input id="humax" class="form-control" style="border-top-right-radius: 20px;border-bottom-right-radius: 20px;" type="number" name="humax" value="{{ humax|safe }}"/>
                        <!-- ...............................................      -->
                                        <div style="margin-left: 100px; margin-right: 100px;">
                                            <button id="rangos" class="btn btn-info" style="border-radius: 20px;" type="submit" ><img src="{% static 'devices/img/search.svg' %}"> Modificar rango</button>
                                            <!--<a id="rangos" href="" class="btn btn-info" style="border-radius: 20px;"><img src="{% static 'devices/img/search.svg' %}"> Modificar rango</a>-->
                                        </div>
                                        <div style="margin-right: 150px; background-color:#ff9900; border-radius: 20px;">
                                            <a class="btn" href="{% url 'generatepdf' %}?agrup={{agrupado}}&sucur={{sucursal}}&desde={{desdegrafica}}&hasta={{hastagrafica}}" ><img src="{% static 'devices/img/printer.svg' %}"> Exportar PDF</a>
                                        </div>
                                    </div>
                                    <div class="float-right" style="padding: 0px;">
                                        <a id="btnCapturar" href="" download="{{agrupado}}.jpg" class="btn" ><img src="{% static 'devices/img/ar-camera.png' %}"></a>  
                                    </div>          
                                </form>       
                            </div>
                            <div class="col-6">
                                <img src="{% static 'devices/img/logo_cliente.png' %}" alt="">
                            </div>
                            <div class="col-6">
                                <label>{{agrupado}}</label>
                                </br>
                                <label for="">Temp: {{ ranmintem }}C° - {{ ranmaxtem }}C°</label>
                                </br>
                                <label for="">Hum:
                                    {% if ranminhum %}
                                        {{ ranminhum }}% - {{ ranmaxhum }}
                                    {% endif %}
                                </label>
                            </div>
                            <canvas id="myChart" width="400px" height="100%"></canvas>                                                                                
                        </div>  
                    </div>
                </div>
            </div>
        </br>
        
        <div class="col-sm-12" style="margin-top: 10px; margin-bottom: 20px;">   
            <div class="card border-info">
                <div style="background-color: #00bcd4; padding: 10px; font-size: 17px;" class="card-header border-success text-light">
                    Histórico rango de fecha
                </div>
                <div class="card-body">
                    <div class="row">  
                        <div class="form-group col-12">                           
                            <form class="form" action="" method="POST">
                                {% csrf_token %} 
                                <div class="input-group row">
                                    <div class="input-group-prepend">
                                        <label class="input-group-text" for="inputGroupSelect01">Desde: </label>
                                    </div>
                                    <input class="form-control col-2" type="datetime-local" name="desdetabla" value="{{ desdetabla }}"/>
                                    <div class="input-group-prepend" style="margin-left: 10px;">
                                        <label class="input-group-text" for="inputGroupSelect01">Hasta: </label>
                                        </div>
                                    <input class="form-control col-2"  type="datetime-local" name="hastatabla" value="{{ hastatabla }}"/>
                                    <div style="margin-left: 10px;">
                                        <button class="btn btn-info" type="submit" ><img src="{% static 'devices/img/search.svg' %}"></button>
                                    </div> 
                                </div>       
                            </form>                           
                        </div>                                                 
                        <div style="width: 100%;" >
                            <table class="table table-striped border border-info" style="text-align: center;">
                                <thead class="bg-info">
                                  <tr class="table-info">                                   
                                    <th style="padding-top: 0px;padding-bottom: 0px;" scope="col">Camara</th>
                                    <th style="padding-top: 0px;padding-bottom: 0px;" scope="col">Fecha de Registro</th>
                                    {% for ubicacion in ubicacion %}
                                        {% if ubicacion.tipo_comp == '2' %}
                                            <th style="padding-top: 0px;padding-bottom: 0px;" scope="col">{{ ubicacion.ubicacion }} Temperatura</th>
                                        {% else %}
                                            <th style="padding-top: 0px;padding-bottom: 0px;" scope="col">{{ ubicacion.ubicacion }} Humedad</th>
                                        {% endif %}
                                    {% endfor %}  
                                  </tr>
                                </thead>
                                <tbody style="padding: 0px;"> 
                                    {% for users in users %}                        
                                        <tr>
                                            <td style="padding-top: 1px;padding-bottom: 1px;">{{ agrupado }}</td>
                                            <td style="padding-top: 1px;padding-bottom: 1px;">{{ users.fetch }}</td>
                                            {% if ancho == 4 %}
                                            <td style="padding-top: 1px;padding-bottom: 1px;">{{ users.valprueba1}} C°</td>                                            
                                            <td style="padding-top: 1px;padding-bottom: 1px;">{{ users.valprueba2 }} C°</td>                                            
                                            <td style="padding-top: 1px;padding-bottom: 1px;">{{ users.valprueba3 }} %</td>
                                            <td style="padding-top: 1px;padding-bottom: 1px;">{{ users.valprueba4 }} %</td>
                                            {% elif ancho == 2 %}
                                            <td style="padding-top: 1px;padding-bottom: 1px;">{{ users.valprueba1}} C°</td>                                            
                                            <td style="padding-top: 1px;padding-bottom: 1px;">{{ users.valprueba2 }} C°</td>
                                            {% else %}
                                            <td style="padding-top: 1px;padding-bottom: 1px;">{{ users.valprueba1}} C°</td>                                            
                                            {% endif %}
                                                                                                                                            
                                        </tr> 
                                    {% endfor %} 
                                </tbody>
                              </table>
                            {% if users.has_other_pages %}
                            <form action="" method="POST">
                                {% csrf_token %}   
                                <nav aria-label="Page" style="margin-left: 10px;">
                                    <ul class="pagination">
                                        {% if users.has_previous %}                                                                
                                            <li class="page-item">
                                                <button class="page-link" type="submit" name="page" value="{{ users.previous_page_number }}">&laquo;</button>
                                                <!--<a class="page-link" href="?page={{ users.previous_page_number }}">&laquo;</a>-->
                                            </li>
                                        {% else %}
                                            <li class="page-item disabled">
                                                <a class="page-link" href="#"><span aria-hidden="true">&laquo;</span></a>
                                            </li>
                                        {% endif %}
                                        {% for i in users.paginator.page_range %}
                                        {% if users.number == i %}
                                            <li class="page-item active bg-info" aria-current="page">
                                                <a class="page-link" style="background:#00bcd4; border: 1px solid transparent;">
                                                    <span >{{ i }} <span class="sr-only">(current)</span></span>
                                                </a>                                          
                                            </li>
                                        {% else %}                                       
                                            <li class="page-item">
                                                <button class="page-link" type="submit" name="page" style="color: #00bcd4;" value="{{ i }}">{{ i }}</button>
                                                <!--<a class="page-link" style="color: #00bcd4;" href="?page={{ i }}">{{ i }}</a>-->
                                            </li>                                            
                                        {% endif %}
                                        {% endfor %}
                                        {% if users.has_next %}
                                            <li class="page-item">
                                                <button class="page-link" type="submit" style="color: #00bcd4;" name="page" value="{{ users.next_page_number }}">&raquo;</button>
                                                <!--<a class="page-link" style="color: #00bcd4;" href="?page={{ users.next_page_number }}">&raquo;</a>-->
                                            </li>
                                        {% else %}
                                            <li class="page-item disabled">
                                                <a class="page-link" href="#"><span aria-hidden="true">&raquo;</span></a>
                                            </li>
                                        {% endif %}
                                    </ul>
                                </nav>
                            </form> 
                            {% endif %}
                        </div>                           
                    </div>  
                </div>
            </div>
        </div>
        <div class="col-sm-12" style="margin-top: 10px; margin-bottom: 20px;">   
            <div class="card border-info">
                <div style="background-color: #00bcd4; padding: 10px; font-size: 17px;" class="card-header border-success text-light">
                    Historial de Apagado - Encendido
                </div>
                <div class="card-body">
                    <div class="row">  
                        <div class="form-group col-12">                                                                          
                        <div style="width: 100%;" >
                            <table class="table table-striped border border-info" style="text-align: center;">
                                <thead class="bg-info">
                                  <tr class="table-info">                                   
                                    <th style="padding-top: 0px;padding-bottom: 0px;" scope="col">ID</th>
                                    <th style="padding-top: 0px;padding-bottom: 0px;" scope="col">Camara</th>
                                    <th style="padding-top: 0px;padding-bottom: 0px;" scope="col">Hora Apagado</th>
                                    <th style="padding-top: 0px;padding-bottom: 0px;" scope="col">Hora Prendido</th> 
                                  </tr>
                                </thead>
                                <tbody style="padding: 0px;"> 
                                    <!--{% for users in users %}                        
                                        <tr>
                                            <td style="padding-top: 1px;padding-bottom: 1px;">{{ agrupado }}</td>
                                            <td style="padding-top: 1px;padding-bottom: 1px;">{{ users.fetch }}</td>
                                            {% if ancho == 4 %}
                                            <td style="padding-top: 1px;padding-bottom: 1px;">{{ users.valprueba1}} C°</td>                                            
                                            <td style="padding-top: 1px;padding-bottom: 1px;">{{ users.valprueba2 }} C°</td>                                            
                                            <td style="padding-top: 1px;padding-bottom: 1px;">{{ users.valprueba3 }} %</td>
                                            <td style="padding-top: 1px;padding-bottom: 1px;">{{ users.valprueba4 }} %</td>
                                            {% elif ancho == 2 %}
                                            <td style="padding-top: 1px;padding-bottom: 1px;">{{ users.valprueba1}} C°</td>                                            
                                            <td style="padding-top: 1px;padding-bottom: 1px;">{{ users.valprueba2 }} C°</td>
                                            {% else %}
                                            <td style="padding-top: 1px;padding-bottom: 1px;">{{ users.total_nivel_1}} C°</td>                                            
                                            {% endif %}
                                                                                                                                            
                                        </tr> 
                                    {% endfor %}-->
                                    <tr>
                                    </tr>
                                </tbody>
                              </table>
                            {% if users.has_other_pages %}
                            <form action="" method="POST">
                                {% csrf_token %}   
                                <nav aria-label="Page" style="margin-left: 10px;">
                                    <ul class="pagination">
                                        {% if users.has_previous %}                                                                
                                            <li class="page-item">
                                                <button class="page-link" type="submit" name="page" value="{{ users.previous_page_number }}">&laquo;</button>
                                                <!--<a class="page-link" href="?page={{ users.previous_page_number }}">&laquo;</a>-->
                                            </li>
                                        {% else %}
                                            <li class="page-item disabled">
                                                <a class="page-link" href="#"><span aria-hidden="true">&laquo;</span></a>
                                            </li>
                                        {% endif %}
                                        {% for i in users.paginator.page_range %}
                                        {% if users.number == i %}
                                            <li class="page-item active bg-info" aria-current="page">
                                                <a class="page-link" style="background:#00bcd4; border: 1px solid transparent;">
                                                    <span >{{ i }} <span class="sr-only">(current)</span></span>
                                                </a>                                          
                                            </li>
                                        {% else %}                                       
                                            <li class="page-item">
                                                <button class="page-link" type="submit" name="page" style="color: #00bcd4;" value="{{ i }}">{{ i }}</button>
                                                <!--<a class="page-link" style="color: #00bcd4;" href="?page={{ i }}">{{ i }}</a>-->
                                            </li>                                            
                                        {% endif %}
                                        {% endfor %}
                                        {% if users.has_next %}
                                            <li class="page-item">
                                                <button class="page-link" type="submit" style="color: #00bcd4;" name="page" value="{{ users.next_page_number }}">&raquo;</button>
                                                <!--<a class="page-link" style="color: #00bcd4;" href="?page={{ users.next_page_number }}">&raquo;</a>-->
                                            </li>
                                        {% else %}
                                            <li class="page-item disabled">
                                                <a class="page-link" href="#"><span aria-hidden="true">&raquo;</span></a>
                                            </li>
                                        {% endif %}
                                    </ul>
                                </nav>
                            </form> 
                            {% endif %}
                        </div>                           
                    </div>  
                </div>
            </div>
        </div> 
    </div>
    
    <script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.8.0/Chart.bundle.min.js"></script>
        <script type="text/javascript">
            document.getElementById("rangos").addEventListener('click',function(){
                ti = document.getElementById("temin").value;
                ta = document.getElementById("temax").value;
                x1 = document.getElementById("humin").value;
                x1 = document.getElementById("humax").value;
            });
            const temin = {{teminimo|safe}};
            const tema = {{temaximo|safe}};      
            const huma = {{humaximo|safe}};
            const humin = {{huminimo|safe}};
            {% if anexo1 %}
                var dat1 = {{ anexo1|safe }};
            {% endif %}
            {% if anexo2 %}
                var dat2 = {{ anexo2|safe }};
            {% endif %}
            {% if anexo3 %}
                var dat3 = {{ anexo3|safe }};
            {% endif %}
            {% if anexo4 %}
                var dat4 = {{ anexo4|safe }};
            {% endif %}
            var datfech = {{anexofech|safe}};
            {% if titgeneral.0 %}
                var tit1 = {{titgeneral.0|safe}};
            {% endif %}
            {% if titgeneral.1 %}
                var tit2 = {{titgeneral.1|safe}};
            {% endif %}
            {% if titgeneral.2 %}
                var tit3 = {{titgeneral.2|safe}};
            {% endif %}
            {% if titgeneral.3 %}
                var tit4 = {{titgeneral.3|safe}};
            {% endif %}
            {% if color1 and  border1 %}
                var color1 = {{color1|safe}};
                var border1 = {{border1|safe}};
            {% endif %}
            {% if color2 and  border2 %}
                var color2 = {{color2|safe}};
                var border2 = {{border2|safe}};
            {% endif %}
            {% if color3 and  border3 %}
                var color3 = {{color3|safe}};
                var border3 = {{border3|safe}};
            {% endif %}
            {% if color4 and  border4 %}
                var color4 = {{color4|safe}};
                var border4 = {{border4|safe}};
            {% endif %}
            {% if anexo1 and anexo2 and anexo3 and anexo4 %}
                var cajassets = [
                        {
                        label: tit3,
                        data:dat3,
                        backgroundColor: color3,
                        borderColor: color3,
                        fill:false,
                        yAxisID:'y-axis-1',
                        },
                        {
                        label: tit4,
                        data:dat4,
                        backgroundColor: color4,
                        borderColor: color4,
                        fill:false,
                        yAxisID:'y-axis-1',
                        },
                        {
                        label: tit1,
                        data:dat1,
                        backgroundColor: color1,
                        borderColor: border1,
                        fill:false,
                        yAxisID:'y-axis-2',
                        },
                        {
                        label: tit2,
                        data:dat2,
                        backgroundColor:color2,
                        borderColor: color2,
                        fill:false,
                        yAxisID:'y-axis-2',
                        },
                        
                    ]
            {% elif anexo1 and anexo2 %}
                var cajassets = [{
                    label: tit1,
                        data:dat1,
                        backgroundColor: color1,
                        borderColor: border1,
                        fill:false,
                        yAxisID:'y-axis-2',
                        },
                        {
                        label: tit2,
                        data:dat2,
                        backgroundColor:color2,
                        borderColor: color2,
                        fill:false,
                        yAxisID:'y-axis-2'}]
            {% else %}
                var cajassets = [{
                    label: tit1,
                        data:dat1,
                        backgroundColor: color1,
                        borderColor: border1,
                        fill:false,
                        yAxisID:'y-axis-2',
                        }]
            {% endif %}
            var ctx = document.getElementById('myChart');
            var myChart = new Chart(ctx, {
                type:'line',
                data: {
                    labels:datfech ,
                    datasets: cajassets
                },
                options: {
                    responsive:true,
                    scales: {
                        yAxes: [{
                            type:'linear',
                            display:true,
                            id:'y-axis-1',
                            ticks: {
                                suggestedMin: humin,
                                suggestedMax: huma
                            },
                            scaleLabel:{
                                display:true,
                                labelString:'Humedad',
                                
                            },
                            position: 'left',
                        },
                        {
                            type:'linear',
                            display:true,
                            id:'y-axis-2',
                            ticks: {
                                suggestedMin: temin,
                                suggestedMax: tema
                            },
                            scaleLabel:{
                                display:true,
                                labelString:'Temperatura'
                            },
                            position: 'right',
                        }],
                        xAxes:[{
                            ticks:{
                                autoSkip: true,
                                maxTicksLimit: 8,
                                maxRotation: 0
                            }
                        }]
                    },
                    title:{
                        display:true,
                        text: ' Gráfico de camara '
                    },
                    tooltips:{
                        intersect:false,
                        mode: 'index'                   
                    },
                    elements:{  
                        point:{
                            radius:0,
                        }
                    }
                }
            });
            /*document.getElementById("btnCapturar").addEventListener('click',function(){
                var url_base64jp = document.getElementById("myChart").toDataURL("image/jpg");
                var a = document.getElementById("btnCapturar");
                a.href =url_base64jp;
            });*/
            $(document).ready(function() {
                $("#btnpdfhtml").click(function() {
                    window.print();
                    return true;
                });
                $("#btnCapturar").click(function() {
                    var url_base64jp = document.getElementById("myChart").toDataURL("image/jpg");
                    var a = document.getElementById("btnCapturar");
                    a.href =url_base64jp;
                });
            });
        </script>
       
    {% endblock %}
