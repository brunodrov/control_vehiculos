from django.contrib import admin
from .models import Usuario, Vehiculo, Mantenimiento, ReporteEstado, Turno, Chequeo

admin.site.register(Usuario)
admin.site.register(Vehiculo)
admin.site.register(Mantenimiento)
admin.site.register(ReporteEstado)
admin.site.register(Turno)
admin.site.register(Chequeo)


