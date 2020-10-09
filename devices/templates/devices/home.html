{% extends "devices/home_base.html" %}
{% block cardbody %}
{% load static %}
    <div class="card-body" style="padding-top: 13px;">
        <div class="form-group col-6">
            <div class="input-group">
                <form class="form" action="{% url 'home' %}" method="POST">
                    {% csrf_token %}
                    <div class="input-group">
                        <div class="input-group-prepend">
                          <label class="input-group-text" for="inputGroupSelect01"><img for="inputGroupSelect01" src="{% static 'devices/img/ubicacion.svg' %}"/></label>
                        </div>
                        <select class="custom-select" id="inputGroupSelect01" style="width: 300px;" name="sucur">
                            {% for sucursal in sucursal %}                                
                                <option value="{{sucursal.id_sucursal}}" 
                                    {% if idsucur == sucursal.id_sucursal%}
                                        selected
                                    {%else%}
                                    {% endif %}>{{sucursal.nombre}}</options>
                            {% endfor %}
                        </select>
                        <div style="margin-left: 10px;">
                            <button class="btn btn-info" type="submit" ><img src="{% static 'devices/img/search.svg' %}"></button>
                        </div> 
                    </div>                        
                </form>
            </div>            
        </div>
    </div>
    <div class=" border-top" style="background: #fafafa; height: 40px;">
        <a href="">
        <img src="{% static 'devices/img/ajustes2.png' %}" style="margin: 5px;" />
        <small class="text-info">Busqueda por sucursales</small>
        </a>
    </div>
{% endblock %}
    {% block content%}
    {% load static %}
    <div id="alerta_incidencias" class="row" style="margin: 8px;">
        {% for agrup in agrup %}
            {% if agrup.cont and agrup.cont == 4 %}
                <div class="col-sm-6" style="margin-top: 10px; margin-bottom: 20px;">
            {% elif agrup.cont == 2 %}
                <div class="col-sm-3" style="margin-top: 10px; margin-bottom: 20px;">
            {% else %}
                <div class="col-sm-2" style="margin-top: 10px; margin-bottom: 20px;">  
            {% endif %}                                        
                {% if agrup.iden == 0 %}
                    <div class="card border-info"> 
                        <div class="card-header border-success" style="background-color: #00bcd4;">  
                {% else %}
                    <div class="card border-danger"> 
                        <div class="card-header " style="background-color: #ff5722; border: solid 2px #ff5722;">  
                {% endif %}                          
                            <a class="text-dark" href="{% url 'backup' %}?agrup={{agrup.agrupado}}&sucur={{agrup.id_sucursal}}">{{agrup.agrupado}}</a>
                            <img style="height: 30px; margin-left: 10px;" src="{% static 'devices/img/calenda.png' %}"/>
                            <small>{{agrup.updated_at|date:"Y-m-d H:i:s"}}</small>                                           
                        </div>
                                <div class="card-body">
                                    <div class="row">                     
                                        {% if agrup.cont and agrup.cont == 4 %}
                                            {% for caja in caja %}
                                                {%if caja.agrupado == agrup.agrupado %}
                                                    <div class="col-3" style="text-align: center;">
                                                        <div class="border-bottom">
                                                            <label style="margin-bottom: 10px; padding-top:0px;">
                                                                {% if caja.id_tipo_componente == '2' %}
                                                                    Temperatura
                                                                {% else %}
                                                                    Humedad
                                                                {% endif %}
                                                            </label>
                                                        </div>
                                                        <div style="margin-top: 20px;">
                                                            {% if caja.id_tipo_componente == '2' %}
                                                                {% if caja.ultimo_valor <= caja.mini %}
                                                                    <img  src="{% static 'devices/img/ventilfrio.png' %}"/>
                                                                {% elif caja.ultimo_valor >= caja.maxi %}
                                                                    <img  src="{% static 'devices/img/calentar.png' %}"/>
                                                                {% else %}
                                                                    <img  src="{% static 'devices/img/ventil3.png' %}"/>
                                                                {% endif %}
                                                            {% else %}
                                                                {% if caja.ultimo_valor <= caja.mini %}
                                                                    <img  src="{% static 'devices/img/humedad.png' %}"/>
                                                                {% elif caja.ultimo_valor >= caja.maxi %}
                                                                    <img  src="{% static 'devices/img/aguacaliente.png' %}"/>
                                                                {% else %}
                                                                    <img  src="{% static 'devices/img/agua.png' %}"/>
                                                                {% endif %}    
                                                            {% endif %}
                                                            <small class="text-black-50">{{ caja.ubicacion }}</small>
                                                            </br>
                                                            <div class="font-weight-bolder" style="margin: 10px;">
                                                                <label>
                                                                    {% if caja.id_tipo_componente == '2' %}
                                                                        {{ caja.ultimo_valor }} °C
                                                                    {% else %}
                                                                        {{ caja.ultimo_valor }} %
                                                                    {% endif %}
                                                                </label>
                                                            </div>                            
                                                        </div>
                                                        <div class="row text-black-50">
                                                            <div class="col-6">
                                                                <img  src="{% static 'devices/img/disminucion2.png' %}"/>
                                                                <small>
                                                                    {% if caja.id_tipo_componente == '2' %}
                                                                        {{ caja.valor_minimo }} °C
                                                                    {% else %}
                                                                        {{ caja.valor_minimo }} %
                                                                    {% endif %}                                                            
                                                                </small>
                                                                </br>
                                                                <small>T.min</small>
                                                            </div>
                                                            <div class="col-6">
                                                                <img src="{% static 'devices/img/aumento2.png' %}"/>
                                                                <small>
                                                                    {% if caja.id_tipo_componente == '2' %}
                                                                        {{ caja.valor_maximo }} °C
                                                                    {% else %}
                                                                        {{ caja.valor_maximo }} %
                                                                    {% endif %} 
                                                                </small>
                                                                </br>
                                                                <small>T.max</small>
                                                            </div>                                                            
                                                        </div>
                                                    </div>
                                                {% endif %}
                                            {% endfor %}
                                        {% elif agrup.cont == 2 %}
                                            {% for caja in caja %}
                                                {% if caja.agrupado == agrup.agrupado %}
                                                    <div class="col-6" style="text-align: center;">
                                                        <div class="border-bottom">
                                                            <label style="margin-bottom: 10px;">
                                                                {% if caja.id_tipo_componente == '2' %}
                                                                    Temperatura
                                                                {% else %}
                                                                    Humedad
                                                                {% endif %}
                                                            </label>
                                                        </div>
                                                        <div style="margin-top: 20px;">
                                                            {% if caja.id_tipo_componente == '2' %}
                                                                {% if caja.ultimo_valor <= caja.mini %}
                                                                    <img  src="{% static 'devices/img/ventilfrio.png' %}"/>
                                                                {% elif caja.ultimo_valor >= caja.maxi %}
                                                                    <img  src="{% static 'devices/img/calentar.png' %}"/>
                                                                {% else %}
                                                                    <img  src="{% static 'devices/img/ventil3.png' %}"/>
                                                                {% endif %}
                                                            {% else %}
                                                                {% if caja.ultimo_valor <= caja.mini %}
                                                                    <img  src="{% static 'devices/img/humedad.png' %}"/>
                                                                {% elif caja.ultimo_valor >= caja.maxi %}
                                                                    <img  src="{% static 'devices/img/calentar.png' %}"/>
                                                                {% else %}
                                                                    <img  src="{% static 'devices/img/agua.png' %}"/>
                                                                {% endif %}    
                                                            {% endif %}
                                                            <small class="text-black-50">{{ caja.ubicacion }}</small>
                                                            </br>
                                                            <div class="font-weight-bolder" style="margin: 10px;">
                                                                <label>
                                                                    {% if caja.id_tipo_componente == '2' %}
                                                                        {{ caja.ultimo_valor }} °C
                                                                    {% else %}
                                                                        {{ caja.ultimo_valor }} %
                                                                    {% endif %}
                                                                </label>
                                                            </div>                            
                                                        </div>
                                                        <div class="row text-black-50">
                                                            <div class="col-6">
                                                                <img  src="{% static 'devices/img/disminucion2.png' %}"/>
                                                                <small>
                                                                    {% if caja.id_tipo_componente == '2' %}
                                                                        {{ caja.valor_minimo }} °C
                                                                    {% else %}
                                                                        {{ caja.valor_minimo }} %
                                                                    {% endif %}  
                                                                </small>
                                                                </br>
                                                                <small>T.min</small>
                                                            </div>
                                                            <div class="col-6">
                                                                <img  src="{% static 'devices/img/aumento2.png' %}"/>
                                                                <small>
                                                                    {% if caja.id_tipo_componente == '2' %}
                                                                        {{ caja.valor_maximo }} °C
                                                                    {% else %}
                                                                        {{ caja.valor_maximo }} %
                                                                    {% endif %} 
                                                                </small>
                                                                </br>
                                                                <small>T.max</small>
                                                            </div>                                                            
                                                        </div>
                                                    </div>
                                                {% endif %}
                                            {% endfor %}                                    
                                        {% else %}
                                            {% for caja in caja %}
                                                {% if caja.agrupado == agrup.agrupado %}
                                                    <div class="col-12" style="text-align: center;">
                                                        <div class="border-bottom">
                                                            <label style="margin-bottom: 10px;">
                                                                {% if caja.id_tipo_componente == '2' %}
                                                                    Temperatura
                                                                {% else %}
                                                                    Humedad
                                                                {% endif %}
                                                            </label>
                                                        </div>
                                                        <div style="margin-top: 20px;">
                                                            {% if caja.ultimo_valor > 0 %}
                                                                {% if caja.ultimo_valor <= caja.mini %}
                                                                    <img  src="{% static 'devices/img/ventilfrio.png' %}"/>
                                                                {% elif caja.ultimo_valor >= caja.maxi %}
                                                                    <img  src="{% static 'devices/img/calentar.png' %}"/>
                                                                {% else %}
                                                                    <img  src="{% static 'devices/img/ventil3.png' %}"/>
                                                                {% endif %}
                                                            {% else %}
                                                                {% if caja.ultimo_valor >= caja.mini %}
                                                                    <img  src="{% static 'devices/img/calentar.png' %}"/>
                                                                {% elif caja.ultimo_valor <= caja.maxi%}
                                                                    <img  src="{% static 'devices/img/ventilfrio.png' %}"/>
                                                                {% else %}
                                                                    <img  src="{% static 'devices/img/ventil3.png' %}"/>
                                                                {% endif %}
                                                            {% endif %}
                                                            <small class="text-black-50">{{ caja.ubicacion }}</small>
                                                            </br>
                                                            <div class="font-weight-bolder" style="margin: 10px;">
                                                                <label>
                                                                    {% if caja.id_tipo_componente == '2' %}
                                                                        {{ caja.ultimo_valor }} °C
                                                                    {% else %}
                                                                        {{ caja.ultimo_valor }} %
                                                                    {% endif %}
                                                                </label>
                                                            </div>                            
                                                        </div>
                                                        <div class="row text-black-50">
                                                            <div class="col-6">
                                                                <img  src="{% static 'devices/img/disminucion2.png' %}"/>
                                                                <small>
                                                                    {% if caja.id_tipo_componente == '2' %}
                                                                        {{ caja.valor_minimo }} °C
                                                                    {% else %}
                                                                        {{ caja.valor_minimo }} %
                                                                    {% endif %}
                                                                </small>
                                                                </br>
                                                                <small>T.min</small>
                                                            </div>
                                                            <div class="col-6">
                                                                <img  src="{% static 'devices/img/aumento2.png' %}"/>
                                                                <small>
                                                                    {% if caja.id_tipo_componente == '2' %}
                                                                        {{ caja.valor_maximo }} °C
                                                                    {% else %}
                                                                        {{ caja.valor_maximo }} %
                                                                    {% endif %} 
                                                                </small>
                                                                </br>
                                                                <small>T.max</small>
                                                            </div>                                                            
                                                        </div>
                                                    </div>
                                                {% endif %}
                                            {% endfor %}
                                        {% endif %}                            
                                    
                                        </div>  
                                    </div>
                        </div>
                    </div>
        {% endfor %}       
                </div>
            
    {% endblock %}
