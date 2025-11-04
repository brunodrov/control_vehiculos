from django.test import TestCase
from .models import Usuario, Vehiculo
from rest_framework.test import APIClient
from rest_framework import status

class UsuarioModelTest(TestCase):
    def setUp(self):
        # esto se ejecuta antes de cada test
        self.usuario = Usuario.objects.create(nombre="Juan Pérez", email="juan@example.com")

    def test_usuario_creado_correctamente(self):
        """Verifica que el usuario se crea y se guarda en la base"""
        usuario = Usuario.objects.get(nombre="Juan Pérez")
        self.assertEqual(usuario.email, "juan@example.com")

class VehiculoModelTest(TestCase):
    def setUp(self):
        self.usuario = Usuario.objects.create(nombre="María", email="maria@example.com")
        self.vehiculo = Vehiculo.objects.create(
            marca="Toyota",
            modelo="Corolla",
            patente="ABC123",
            anio=2020,
            usuario=self.usuario
        )

    def test_vehiculo_relacion_usuario(self):
        """Verifica que el vehículo está asociado al usuario correcto"""
        self.assertEqual(self.vehiculo.usuario.nombre, "María")

class UsuarioAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = '/api/usuarios/'

    def test_crear_usuario_via_api(self):
        """Verifica que se pueda crear un usuario mediante POST en la API"""
        data = {
            "nombre": "Pedro API",
            "email": "pedro@example.com",
            "rol": "Administrador"
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['nombre'], "Pedro API")

    def test_listar_usuarios(self):
        """Verifica que el endpoint GET devuelva los usuarios existentes"""
        Usuario.objects.create(nombre="Laura", email="laura@example.com")
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

class VehiculoAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.usuario = Usuario.objects.create(
            nombre="Carlos Tester",
            email="carlos@example.com",
            rol="Operador"
        )
        self.url = '/api/vehiculos/'

    def test_crear_vehiculo_via_api(self):
        """Verifica que se pueda crear un vehículo asociado a un usuario mediante la API"""
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
        """Verifica que el endpoint GET devuelva los vehículos existentes"""
        Vehiculo.objects.create(
            marca="Chevrolet",
            modelo="Onix",
            anio=2021,
            patente="ABC999",
            usuario=self.usuario
        )
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

class ReporteEstadoAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.usuario = Usuario.objects.create(
            nombre="Lucía",
            email="lucia@example.com",
            rol="Técnico"
        )
        self.vehiculo = Vehiculo.objects.create(
            marca="Fiat",
            modelo="Cronos",
            anio=2023,
            patente="AAA111",
            estado="Activo",
            usuario=self.usuario
        )
        self.url = '/api/reportes/'

    def test_crear_reporte_via_api(self):
        """Verifica que se pueda crear un reporte asociado a un vehículo"""
        data = {
            "vehiculo": self.vehiculo.id,
            "fecha": "2025-11-03",
            "nivel_combustible": 45.5,
            "kilometraje": 12000,
            "observaciones": "Motor con temperatura elevada"
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['nivel_combustible'], '45.50')

    def test_listar_reportes(self):
        """Verifica que el endpoint GET devuelva los reportes existentes"""
        from gestion.models import ReporteEstado
        ReporteEstado.objects.create(
            vehiculo=self.vehiculo,
            fecha="2025-11-03",
            nivel_combustible=60.0,
            kilometraje=15000,
            observaciones="Frenos revisados"
        )
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)



class MantenimientoAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.usuario = Usuario.objects.create(
            nombre="Diego",
            email="diego@example.com",
            rol="Supervisor"
        )
        self.vehiculo = Vehiculo.objects.create(
            marca="Renault",
            modelo="Kangoo",
            anio=2021,
            patente="BBB222",
            estado="Mantenimiento",
            usuario=self.usuario
        )
        self.url = '/api/mantenimientos/'

    def test_crear_mantenimiento_via_api(self):
        """Verifica que se pueda crear un mantenimiento asociado a un vehículo"""
        data = {
            "vehiculo": self.vehiculo.id,
            "fecha": "2025-11-03",
            "descripcion": "Cambio de aceite y filtros",
            "costo": 25000.00
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(float(response.data['costo']), 25000.00)

    def test_listar_mantenimientos(self):
        """Verifica que el endpoint GET devuelva los mantenimientos existentes"""
        from gestion.models import Mantenimiento
        Mantenimiento.objects.create(
            vehiculo=self.vehiculo,
            fecha="2025-11-03",
            descripcion="Revisión de frenos",
            costo=12000.00
        )
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

