# BlogFinal

## Descripción

BlogFinal es una aplicación web desarrollada en Django que permite a los usuarios escribir, publicar y comentar artículos en un blog. También incluye funciones de análisis de datos para visualizar la distribución de comentarios por usuario y el número de publicaciones por día.

## Tabla de Contenidos

- [Comenzando](#comenzando)
  - [Requisitos previos](#requisitos-previos)
  - [Instalación](#instalación)
- [Uso](#uso)
- [Características](#características)
- [Contribución](#contribución)


## Comenzando

### Requisitos previos

- Python 3.6 o superior
- Django
- Matplotlib
- Pandas
- psycopg2 (si se utiliza PostgreSQL como base de datos)

### Instalación

1. Clona este repositorio:

   
   git clone https://github.com/Alejo2786/BlogFinal.git

   cd Blog_Final

2. Crea un entorno virtual e instala las dependencias:
   python -m venv venv
   
   source venv/bin/activate
   
   En Windows, usa "venv\Scripts\activate"

   pip install -r requirements.txt

3. Ejecuta las migraciones:

   python manage.py migrate

4. Crea un superusuario para administrar el sitio:

   python manage.py createsuperuser

5. Inicia el servidor de desarrollo:

   python manage.py runserver


6. Accede a la aplicación en http://localhost:8000/admin y utiliza las credenciales del superusuario para iniciar sesión en el panel de administración.



## Uso

- Los usuarios pueden escribir y publicar artículos en el blog.
- Los visitantes pueden comentar en los artículos.
- La vista de análisis de datos muestra la distribución de comentarios por usuario y el número de publicaciones por día.


## Características

- Sistema de autenticación de usuarios.
- Panel de administración de Django.
- Gráficos de Matplotlib para análisis de datos.

## Contribución


¡Estamos abiertos a contribuciones! Si deseas colaborar en el proyecto, sigue estos pasos:

- Haz un fork del repositorio.
- Crea una nueva rama: git checkout -b mi-funcionalidad
- Realiza tus cambios y commitea: git commit -am 'Agrega mi funcionalidad'
- Sube tus cambios: git push origin mi-funcionalidad
- Envía un pull request desde tu rama a la rama principal.
