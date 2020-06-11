from django.contrib import admin

# Register your models here.
from .models import Devices
from .models import Sucursal


admin.site.register(Sucursal)
admin.site.register(Devices)