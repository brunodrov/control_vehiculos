from rest_framework import viewsets
from .models import Usuario, Vehiculo, Turno, Chequeo
from .serializers import UsuarioSerializer, VehiculoSerializer, TurnoSerializer, ChequeoSerializer


# Vista para Usuarios
class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


# Vista para Vehículos
class VehiculoViewSet(viewsets.ModelViewSet):
    queryset = Vehiculo.objects.all()
    serializer_class = VehiculoSerializer


# Vista para Turnos
class TurnoViewSet(viewsets.ModelViewSet):
    queryset = Turno.objects.all()
    serializer_class = TurnoSerializer


# Vista para Chequeos
class ChequeoViewSet(viewsets.ModelViewSet):
    queryset = Chequeo.objects.all()
    serializer_class = ChequeoSerializer
