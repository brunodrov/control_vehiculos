from rest_framework import serializers
from .models import Usuario, Vehiculo, Turno, Chequeo, puntos_por_defecto


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'


class VehiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehiculo
        fields = '__all__'


class TurnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Turno
        fields = '__all__'


class ChequeoSerializer(serializers.ModelSerializer):
    puntos = serializers.JSONField(default=puntos_por_defecto)

    class Meta:
        model = Chequeo
        fields = '__all__'

    def create(self, validated_data):
        instance = super().create(validated_data)
        instance.calcular_resultado()
        return instance
