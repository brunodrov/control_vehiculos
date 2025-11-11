from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Usuario, Vehiculo, Turno, Chequeo


# ------------------ TESTS DE MODELOS ------------------

class UsuarioModelTest(TestCase):
    def setUp(self):
        self.usuario = Usuario.objects.create(
            nombre="Juan Pérez",
            email="juan@example.com",
            rol="Dueño"
        )

    def test_usuario_creado_correctamente(self):
        """Verifica que el usuario se crea correctamente"""
        usuario = Usuario.objects.get(nombre="Juan Pérez")
        self.assertEqual(usuario.email, "juan@example.com")


class VehiculoModelTest(TestCase):
    def setUp(self):
        self.usuario = Usuario.objects.create(
            nombre="María",
            email="maria@example.com",
            rol="Dueño"
        )
        self.vehiculo = Vehiculo.objects.create(
            marca="Toyota",
            modelo="Corolla",
            patente="ABC123",
            anio=2020,
            estado="Activo",
            usuario=self.usuario
        )

    def test_vehiculo_relacion_usuario(self):
        """Verifica que el vehículo está asociado al usuario correcto"""
        self.assertEqual(self.vehiculo.usuario.nombre, "María")


# ------------------ TESTS DE API ------------------

class UsuarioAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = '/api/usuarios/'

    def test_crear_usuario_via_api(self):
        """Verifica creación de usuario vía API"""
        data = {"nombre": "Pedro", "email": "pedro@example.com", "rol": "Evaluador"}
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['nombre'], "Pedro")

    def test_listar_usuarios(self):
        """Verifica listado de usuarios vía API"""
        Usuario.objects.create(nombre="Laura", email="laura@example.com", rol="Dueño")
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)


class VehiculoAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.usuario = Usuario.objects.create(nombre="Carlos", email="carlos@example.com", rol="Dueño")
        self.url = '/api/vehiculos/'

    def test_crear_vehiculo_via_api(self):
        """Verifica creación de vehículo asociado a un usuario"""
        data = {
            "marca": "Ford",
            "modelo": "Focus",
            "anio": 2022,
            "patente": "XYZ789",
            "estado": "Activo",
            "usuario": self.usuario.id
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['marca'], "Ford")

    def test_listar_vehiculos(self):
        """Verifica listado de vehículos"""
        Vehiculo.objects.create(
            marca="Chevrolet",
            modelo="Onix",
            anio=2021,
            patente="ABC999",
            estado="Activo",
            usuario=self.usuario
        )
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)


class TurnoAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.usuario = Usuario.objects.create(nombre="Ana", email="ana@example.com", rol="Dueño")
        self.vehiculo = Vehiculo.objects.create(
            marca="Peugeot",
            modelo="208",
            anio=2022,
            patente="CCC333",
            estado="Activo",
            usuario=self.usuario
        )
        self.url = '/api/turnos/'

    def test_crear_turno_via_api(self):
        """Verifica creación de turno para revisión"""
        data = {"vehiculo": self.vehiculo.id, "fecha": "2025-12-01", "hora": "09:00:00", "estado": "Pendiente"}
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_listar_turnos(self):
        """Verifica listado de turnos existentes"""
        Turno.objects.create(vehiculo=self.vehiculo, fecha="2025-12-02", hora="10:30:00", estado="Confirmado")
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)


class ChequeoAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.evaluador = Usuario.objects.create(nombre="Patricio", email="patricio@example.com", rol="Evaluador")
        self.duenio = Usuario.objects.create(nombre="Lucía", email="lucia@example.com", rol="Dueño")
        self.vehiculo = Vehiculo.objects.create(
            marca="Fiat",
            modelo="Cronos",
            anio=2023,
            patente="DDD444",
            estado="En revisión",
            usuario=self.duenio
        )
        self.turno = Turno.objects.create(vehiculo=self.vehiculo, fecha="2025-11-15", hora="10:00:00", estado="Confirmado")
        self.url = '/api/chequeos/'

    def test_crear_chequeo_via_api(self):
        """Verifica creación de chequeo con cálculo automático del resultado"""
        data = {
            "turno": self.turno.id,
            "evaluador": self.evaluador.id,
            "puntos": {
                "frenos": 10,
                "luces": 9,
                "motor": 8,
                "ruedas": 9,
                "aceite": 9,
                "suspension": 8,
                "direccion": 9,
                "chasis": 9
            },
            "observaciones": "Chequeo general correcto"
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn(response.data['resultado'], ['Seguro', 'Aprobado', 'Rechequeo'])

    def test_listar_chequeos(self):
        """Verifica listado de chequeos"""
        Chequeo.objects.create(
            turno=self.turno,
            evaluador=self.evaluador,
            puntos={
                "frenos": 8,
                "luces": 8,
                "motor": 8,
                "ruedas": 8,
                "aceite": 8,
                "suspension": 8,
                "direccion": 8,
                "chasis": 8
            },
            total=64,
            resultado="Aprobado"
        )
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)
