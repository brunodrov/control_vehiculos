from rest_framework import viewsets
from .models import Usuario, Vehiculo, Mantenimiento, ReporteEstado, Turno, Chequeo
from .serializers import UsuarioSerializer, VehiculoSerializer, MantenimientoSerializer, ReporteEstadoSerializer, TurnoSerializer, ChequeoSerializer

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

# Vista para Turnos
class TurnoViewSet(viewsets.ModelViewSet):
    queryset = Turno.objects.all()
    serializer_class = TurnoSerializer


# Vista para Chequeos
class ChequeoViewSet(viewsets.ModelViewSet):
    queryset = Chequeo.objects.all()
    serializer_class = ChequeoSerializer