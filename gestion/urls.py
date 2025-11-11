from rest_framework import routers
from django.urls import path, include
from .views import UsuarioViewSet, VehiculoViewSet, TurnoViewSet, ChequeoViewSet

# Router automático que genera las rutas CRUD
router = routers.DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)
router.register(r'vehiculos', VehiculoViewSet)
router.register(r'turnos', TurnoViewSet)
router.register(r'chequeos', ChequeoViewSet)

# Incluye todas las rutas registradas
urlpatterns = [
    path('', include(router.urls)),
]

