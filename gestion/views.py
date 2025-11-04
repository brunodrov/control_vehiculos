from rest_framework import viewsets
from .models import Usuario, Vehiculo, Mantenimiento, ReporteEstado
from .serializers import UsuarioSerializer, VehiculoSerializer, MantenimientoSerializer, ReporteEstadoSerializer

# Vista para Usuarios
class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()             
    serializer_class = UsuarioSerializer         

# Vista para Vehículos
class VehiculoViewSet(viewsets.ModelViewSet):
    queryset = Vehiculo.objects.all()
    serializer_class = VehiculoSerializer

# Vista para Mantenimientos
class MantenimientoViewSet(viewsets.ModelViewSet):
    queryset = Mantenimiento.objects.all()
    serializer_class = MantenimientoSerializer

# Vista para Reportes de Estado
class ReporteEstadoViewSet(viewsets.ModelViewSet):
    queryset = ReporteEstado.objects.all()
    serializer_class = ReporteEstadoSerializer
