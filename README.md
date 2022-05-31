Procedimiento:

`pip install -r requirements.txt`

Instalacion django:

- Creación de projecto

`django-admin startproject mysite . `

- Configuracion archivo .env

SECRET_KEY=
POSTGRES_HOST_AUTH_METHOD=trust
POSTGRESQL_NAME=postgres
POSTGRESQL_USER=postgres
POSTGRESQL_PASS=postgres123
POSTGRESQL_HOST=postgres
POSTGRESQL_PORT=5432
DEBUG=True

- Configuración: settings.py

Mover archivo de seguridad:

SECRET_KEY = env('SECRET_KEY')

TIME_ZONE = 'America/Bogota'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

- Configurar: Base de datos

```py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env('POSTGRESQL_NAME'),
        'USER': env('POSTGRESQL_USER'),
        'PASSWORD': env('POSTGRESQL_PASS'),
        'HOST': env('POSTGRESQL_HOST'),
        'PORT': env('POSTGRESQL_PORT'),
    }
}
```

commands:

Inicializar el Docker:

Correr los siguientes comandos:

docker exec -it dev_django_tech bash

python manage.py makemigrations

python manage.py migrate

python manage.py createsuperuser

# Crear aplicación:

```py
python manage.py startapp proof
```

Agregar en settings.py las siguientes lineas:

```py
INSTALLED_APPS = [
    "proof.apps.ProofConfig",
    'rest_framework',
]
```

# Creacion de los modelos:

Agregar las tablas del modelo

```py
python manage.py makemigrations proof
```
