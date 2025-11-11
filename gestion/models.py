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

class Turno(models.Model):
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE, related_name='turnos')
    fecha = models.DateField()
    hora = models.TimeField()
    estado = models.CharField(max_length=20, default='Pendiente')  # Pendiente, Confirmado, Completado

    def __str__(self):
        return f"Turno {self.fecha} - {self.vehiculo.patente}"


class Chequeo(models.Model):
    turno = models.OneToOneField(Turno, on_delete=models.CASCADE, related_name='chequeo')
    evaluador = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True)
    puntos = models.JSONField()  # 8 puntos: {"frenos":8, "luces":9, ...}
    total = models.IntegerField(default=0)
    observaciones = models.TextField(blank=True)
    resultado = models.CharField(max_length=20, default='En evaluación')

    def calcular_resultado(self):
        self.total = sum(self.puntos.values())
        if self.total >= 80:
            self.resultado = "Seguro"
        elif self.total < 40 or any(p < 5 for p in self.puntos.values()):
            self.resultado = "Rechequeo"
        else:
            self.resultado = "Aprobado"

    def save(self, *args, **kwargs):
        self.calcular_resultado()  
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Chequeo turno {self.turno.id} - {self.resultado}"
