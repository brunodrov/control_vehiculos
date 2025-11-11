from django.contrib import admin
from .models import Usuario, Vehiculo, Turno, Chequeo

admin.site.register(Usuario)
admin.site.register(Vehiculo)
admin.site.register(Turno)
admin.site.register(Chequeo)


