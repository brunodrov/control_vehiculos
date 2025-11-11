from django.db import models
from django.core.exceptions import ValidationError


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


class Turno(models.Model):
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE, related_name='turnos')
    fecha = models.DateField()
    hora = models.TimeField()
    estado = models.CharField(max_length=20, default='Pendiente')

    def __str__(self):
        return f"Turno {self.fecha} - {self.vehiculo.patente}"


# --- Función para inicializar los 8 puntos de chequeo ---
def puntos_por_defecto():
    return {
        "frenos": 0,
        "luces": 0,
        "motor": 0,
        "ruedas": 0,
        "aceite": 0,
        "suspension": 0,
        "direccion": 0,
        "chasis": 0
    }


class Chequeo(models.Model):
    turno = models.OneToOneField(Turno, on_delete=models.CASCADE, related_name='chequeo')
    evaluador = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True)
    puntos = models.JSONField(default=puntos_por_defecto)
    total = models.IntegerField(default=0)
    observaciones = models.TextField(blank=True)
    resultado = models.CharField(max_length=20, default='En evaluación')

    def clean(self):
        # Validar cantidad y nombres de los puntos
        if len(self.puntos) != 8:
            raise ValidationError("Debe haber exactamente 8 apartados de evaluación en 'puntos'.")
        claves_validas = set(puntos_por_defecto().keys())
        if set(self.puntos.keys()) != claves_validas:
            raise ValidationError("Los nombres de los apartados deben ser exactamente: frenos, luces, motor, ruedas, aceite, suspension, direccion y chasis.")

        # Validar que el evaluador tenga rol correcto
        if self.evaluador and self.evaluador.rol.lower() != "evaluador":
            raise ValidationError("El usuario asignado como evaluador debe tener el rol 'Evaluador'.")

    def calcular_resultado(self):
        self.total = sum(self.puntos.values())
        if self.total >= 80:
            self.resultado = "Seguro"
        elif self.total < 40 or any(p < 5 for p in self.puntos.values()):
            self.resultado = "Rechequeo"
        else:
            self.resultado = "Aprobado"
        self.save()

    def __str__(self):
        return f"Chequeo del turno {self.turno.id} - Resultado: {self.resultado}"
