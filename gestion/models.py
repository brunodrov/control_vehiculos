from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    rol = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Vehiculo(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    anio = models.IntegerField()
    patente = models.CharField(max_length=10, unique=True)
    estado = models.CharField(max_length=50)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='vehiculos')

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.patente})"


class Mantenimiento(models.Model):
    fecha = models.DateField()
    descripcion = models.TextField()
    costo = models.DecimalField(max_digits=10, decimal_places=2)
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE, related_name='mantenimientos')

    def __str__(self):
        return f"Mantenimiento {self.id} - {self.vehiculo.patente}"


class ReporteEstado(models.Model):
    fecha = models.DateField()
    nivel_combustible = models.DecimalField(max_digits=5, decimal_places=2)
    kilometraje = models.IntegerField()
    observaciones = models.TextField(blank=True)
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE, related_name='reportes')

    def __str__(self):
        return f"Reporte {self.fecha} - {self.vehiculo.patente}"

