{% extends "devices/home_base2.html" %}
    {% block cabecera%}
    {% load static %}
            <div class="col-12 font-weight-bolder" >
                <label style="margin-left: 30px; margin-top: 5px; font-size: 25px; font-family:'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;">
                    <img src="{% static 'devices/img/direccion4.png' %}"> Reporte - MKT
                </label>       
            </div>     
    {% endblock %}
    {% block content %}
    {% load static %}
    <div class="col-sm-12" style="margin-top: 10px; margin-bottom: 20px;">   
        <div class="card border-info">
            <div style="background-color: #006476; padding: 10px; font-size: 17px;" class="card-header border-success text-light">
                Registros
            </div>
            <div class="card-body" id="grafico">
                <div class="row">
                    <div class="form-group col-12">   
                        <form class="form" action="" method="POST">
                            {% csrf_token %} 
                            <div class="row">
                                <div class="form-group col">
                                    <div class="input-group">
                                        <div class="input-group-prepend">
                                            <div class="input-group-text"> <img style="margin-right: 8px;" src="{% static 'devices/img/calendar.svg' %}"/> Desde: </div>
                                        </div>
                                        <input class="form-control" type="datetime-local" name="desde" value="{{desde}}">
                                    </div>             
                                </div>
                                <div class="form-group col">
                                    <div class="input-group">
                                        <div class="input-group-prepend">
                                            <div class="input-group-text"> <img style="margin-right: 8px;" src="{% static 'devices/img/calendar.svg' %}"/> Hasta: </div>
                                        </div>
                                        <input class="form-control" type="datetime-local" name="hasta" value="{{hasta}}">
                                    </div>             
                                </div>
                                <div class="form-group col">
                                    <div class="input-group">
                                        <div class="input-group-prepend">
                                            <div class="input-group-text"><img src="{% static 'devices/img/ubicacion.svg' %}"/></div>
                                        </div>
                                            <select class="custom-select" id="inputGroupSelect01" style="width: 300px;" name="sucur">
                                                <option>Seleccion de planta</option>
                                                {% for sucursal in sucursal %}                                
                                                    <option value="{{sucursal.id_sucursal}}" 
                                                        {% if idsucur == sucursal.id_sucursal%}
                                                            selected
                                                        {%else%}
                                                        {% endif %}>{{sucursal.nombre}}</options>
                                                {% endfor %}
                                            </select>
                                    </div>             
                                </div>
                                <div class="form-group col">
                                    <div class="input-group">
                                        <div class="input-group-prepend">
                                            <div class="input-group-text"><img src="{% static 'devices/img/ubicacion.svg' %}"/></div>
                                        </div>
                                        <select class="form-control" id="exampleFormControlSelect1" name="equip">
                                            <option selected>Equipo</option>
                                            {% for equipo in equipo %}                                
                                                <option value="{{equipo.agrupado}}">{{equipo.agrupado}}</options>
                                            {% endfor %}
                                        </select>                                       
                                    </div>             
                                </div>
                                <div class="form-group col">
                                    <div class="input-group">
                                        <div class="input-group-prepend">
                                            <button class="btn btn-info fo" type="submit" href=""><img src="{% static 'devices/img/search.svg' %}" > Buscar</button>
                                        </div>
                                        <div style="margin-left: 30px; background-color:#ff9900; border-radius: 20px;">
                                            <a class="btn" href="{% url 'generatepdfMKT' %}?equip={{equ}}&sucur={{suc}}&desde={{desde}}&hasta={{hasta}}" ><img src="{% static 'devices/img/printer.svg' %}"> Exportar PDF</a>
                                        </div>              
                                    </div>
                                    
                                </div>               
                            </div>         
                        </form>       
                    </div>
                    <div class="col-12" style="margin-left: 0px;">
                        <label>MKT:  </label>
                        <div style="width: 100%;" >
                            <table class="table table-striped border border-info" style="text-align: center;">
                                <thead class="bg-info">
                                  <tr class="table-info">                                                 
                                    <th style="padding-top: 0px;padding-bottom: 0px;" scope="col">{{ pec.2 }} </th> 
                                    <th style="padding-top: 0px;padding-bottom: 0px;" scope="col">{{ pec.3 }} </th> 
                                    <th style="padding-top: 0px;padding-bottom: 0px;" scope="col">{{ pec.4 }} </th> 
                                    <th style="padding-top: 0px;padding-bottom: 0px;" scope="col">{{ pec.5 }} </th> 
                                    <th style="padding-top: 0px;padding-bottom: 0px;" scope="col">{{ pec.6 }} </th> 
                                    <th style="padding-top: 0px;padding-bottom: 0px;" scope="col">{{ pec.7 }} </th> 
                                    <th style="padding-top: 0px;padding-bottom: 0px;" scope="col">{{ pec.8 }} </th> 
                                    <th style="padding-top: 0px;padding-bottom: 0px;" scope="col">{{ pec.9 }} </th> 
                                  </tr>
                                </thead>
                                <tbody style="padding: 0px;"> 
                                    {% for users in users %}                       
                                        <tr>
                                            <td style="padding-top: 1px;padding-bottom: 1px;">{{users.2}}</td>
                                            <td style="padding-top: 1px;padding-bottom: 1px;">{{users.3|date:'Y-m-d H:m:s'}}</td>
                                            <td style="padding-top: 1px;padding-bottom: 1px;">{{users.4}}</td>
                                            <td style="padding-top: 1px;padding-bottom: 1px;">{{users.5}}</td>
                                            <td style="padding-top: 1px;padding-bottom: 1px;">{{users.6}}</td>
                                            <td style="padding-top: 1px;padding-bottom: 1px;">{{users.7}}</td>
                                            <td style="padding-top: 1px;padding-bottom: 1px;">{{users.8}}</td>
                                            <td style="padding-top: 1px;padding-bottom: 1px;">{{users.9}}</td>                                                                                   
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
    </div>
    {% endblock %}
