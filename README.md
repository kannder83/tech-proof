# Procedimiento:

Tener Python y Docker instalado.

## Tecnologias:

- Python
- Docker
- Framework django
- PostgresSQL

## Preparación:

Correr Entorno Virutal:

`python3 -m venv venv`

Instalar dependencias:

`pip install -r requirements.txt`

Configuracion archivo .env en la ruta mysite/.env

```py
SECRET_KEY=django-insecure-7*-ow8t@iau7%%9s!*wou_eg&p5(e(9m4v9$\_eiw9iguni@zny
POSTGRES_HOST_AUTH_METHOD=trust
POSTGRESQL_NAME=postgres
POSTGRESQL_USER=postgres
POSTGRESQL_PASS=postgres123
POSTGRESQL_HOST=postgres
POSTGRESQL_PORT=5432
DEBUG=True
ALLOWED_HOSTS=localhost
```

## Docker

Realizar build de docker:

`docker-compose -f dev_docker.yml build`

Subir las imagenes de docker:

`docker-compose -f dev_docker.yml up`

Correr los siguientes comandos:

`docker exec -it dev_django_tech bash`

Al ingresar al contenedor ejecutar:

- Hacer la migración de los modelos y creación de tablas:

`python manage.py makemigrations`

`python manage.py migrate`

- Luego crear el super usuario, seguir las instrucciones:

`python manage.py createsuperuser`

## Aplicación:

Ingresar al localhost:

[http://localhost:8000/](http://localhost:8000/proof)

En la página de inicio se tiene la opcion para visualizar cada uno de los registros.

Se tiene la opción de crear un nuevo registro.

[Nuevo Registro](http://localhost:8000/proof/register/new)

Se puede seleccionar un registro para entrar a la vista de detalle.

### Superadmin:

Para ingresar al super admin:

[Super Admin](http://localhost:8000/admin)

- No olvidar crear el acceso para acceder.

### Detalle:

Se puede elimintar el registro.

Se puede editar el registro.

## API

Para consumir la API se realiza desde la URL:

[http://localhost:8000/api/proof/](http://localhost:8000/api/proof/)
