"""hofarm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from devices import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.home, name="home"),
    path('about/',views.about, name="about"),
    path('login/',views.login, name="login"),
    path('dashboard_geren/',views.dashboard_geren, name="dashboard_geren"),
    path('historial_alertas/',views.historial_alertas, name="historial_alertas"),
    path('historico_general/',views.historico_general, name="historico_general"),
    path('reporte_alerta/',views.reporte_alerta, name="reporte_alerta"),
    path('reporte_diario/',views.reporte_diario, name="reporte_diario"),
    path('reporte_mkt/',views.reporte_mkt, name="reporte_mkt"),
    path('ubicaciones/',views.ubicaciones, name="ubicaciones"),
    path('backup/',views.backup,name="backup"),
    path('generatepdf/',views.generatepdf,name="generatepdf"),
    path('capturagrafico/',views.capturagrafico,name="capturagrafico"),
]
