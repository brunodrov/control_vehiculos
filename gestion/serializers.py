from rest_framework import serializers
from .models import Usuario, Vehiculo, Mantenimiento, ReporteEstado, Turno, Chequeo

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'   # Usa todos los campos del modelo

class VehiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehiculo
        fields = '__all__'

class MantenimientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mantenimiento
        fields = '__all__'

class ReporteEstadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReporteEstado
        fields = '__all__'

class TurnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Turno
        fields = '__all__'


class ChequeoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chequeo
        fields = '__all__'
