from rest_framework import routers
from django.urls import path, include
from .views import UsuarioViewSet, VehiculoViewSet, MantenimientoViewSet, ReporteEstadoViewSet, TurnoViewSet, ChequeoViewSet

# Router automático que genera las rutas CRUD
router = routers.DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)
router.register(r'vehiculos', VehiculoViewSet)
router.register(r'mantenimientos', MantenimientoViewSet)
router.register(r'reportes', ReporteEstadoViewSet)
router.register(r'turnos', TurnoViewSet)
router.register(r'chequeos', ChequeoViewSet)

# Incluí todas las rutas registradas
urlpatterns = [
    path('', include(router.urls)),
]
