from django.contrib import admin
from .models import Usuario, Vehiculo, Mantenimiento, ReporteEstado

admin.site.register(Usuario)
admin.site.register(Vehiculo)
admin.site.register(Mantenimiento)
admin.site.register(ReporteEstado)

