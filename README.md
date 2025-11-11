# Proyecto Integrador: Control del Estado de los Vehículos

## 1. Descripción General

El proyecto implementa una aplicación cliente-servidor desarrollada con el framework **Django** y una base de datos **PostgreSQL** relacional.  
Su propósito es gestionar el estado de los vehículos mediante una **API REST** completamente desacoplada, aplicando principios de diseño como la **programación orientada a objetos (POO)**, **principios SOLID** y la **arquitectura en tres capas** (presentación, negocio y datos).

---

## 2. Arquitectura del Sistema

El sistema se estructura en tres capas principales:

- **Capa de presentación:** gestionada por la API REST y el panel administrativo de Django, donde se visualizan y manipulan los datos.
- **Capa de negocio:** maneja la lógica en las vistas (`views.py`), conectando las peticiones HTTP con los modelos de datos.
- **Capa de datos:** implementada con los modelos del ORM de Django y persistida en PostgreSQL.

Esta separación permite mantener un sistema escalable, fácil de mantener y modular.

---

## 3. Inyección de Dependencias y Desacoplamiento

Django aplica de forma implícita la inyección de dependencias.  
Cada componente recibe los objetos que necesita sin instanciarlos directamente.  
Por ejemplo, las vistas (ViewSets) reciben los **serializadores** y los **querysets** desde el framework, cumpliendo con el principio de inversión de dependencias (Dependency Inversion) de SOLID.

---

## 4. Componentes Principales

- **Models:** definen la estructura de las entidades del sistema (Usuario, Vehículo, Mantenimiento, ReporteEstado, Turno, Chequeo).  
- **Serializers:** traducen los objetos Python a formato JSON y viceversa, permitiendo la comunicación entre la API y el cliente.  
- **Views:** implementan los endpoints REST y gestionan las operaciones CRUD (crear, leer, actualizar, eliminar).  
- **URLs:** definen las rutas para acceder a los endpoints y vinculan cada recurso con su vista correspondiente.  
- **Tests:** validan el correcto funcionamiento del sistema, creando una base de datos temporal para las pruebas unitarias e integrales.

---

## 5. Pruebas y Validación

Se realizaron pruebas automáticas con **Django TestCase**, cubriendo:

- Creación, actualización y eliminación de usuarios, vehículos, reportes, mantenimientos.
- Validación de relaciones entre entidades (vehículo-usuario, mantenimiento-vehículo, chequeo-turno).
- Verificación de endpoints REST mediante el cliente de pruebas de Django.

Todas las pruebas fueron exitosas, garantizando la integridad del sistema y la correcta interacción entre la API y la base de datos.

---

## 6. Manual de Ejecución

### Clonar el proyecto
```bash
git clone https://github.com/brunodrov/control_vehiculos.git
cd control_vehiculos
```
# Algunos puntos a tener en cuenta para ejecucion y despliegue y ejecucion del proyecto

## 1. resquitivos previos
- Python 3.10 o superior
- PostgreSQL instalado y ejecutandose
- Django y Django REST Framework
- Git (opcional, para control de versiones)

## 2. Crear entorno virtual e instalar dependencias
```bash
python3 -m venv venv
source venv/bin/activate  # (En Windows: venv\Scripts\activate)
pip install -r requirements.txt
```
## 3. configurar la base de datos PostgreSQL
editamos settings.py con las credencias locales de PostgreSQL:
```bash
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'control_vehiculos',
        'USER': 'tu_usuario',
        'PASSWORD': 'tu_contraseña',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```
luego abrimos la base desde la terminal
## 4. aplicar migraciones y crear usuario:
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```
## 5. correr el servidor local
```bash
python manage.py runserver
```
luego ingresasr desde el navegador a:
* Panel admin: http://127.0.0.1:8000/admin/
* API REST: http://127.0.0.1:8000/api/

## 6. Probar endpoints de la api
los principales endpoints disponibles son:
*/api/usuarios/
*/api/vehiculos/
*/api/mantenimientos/
*/api/reportes/
*/api/turnos/
*/api/chequeos/
cada uno permite hacer operaciones CRUD mediante HTTP

## 7. ejecucion de pruebas automaticas
```bash
python manage.py test
```
esto ejecutara los casos definidos en gestion/tests.py, creando una base temporal de prueba que se elimina al finalizar
