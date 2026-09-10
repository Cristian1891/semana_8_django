# Blog Django - Semana 8

Proyecto de ejemplo desarrollado con Django para practicar la creación de vistas, rutas y plantillas en una aplicación web sencilla de publicaciones.

## Descripción

Este proyecto consiste en una pequeña aplicación de blog con estas secciones:

- Página de inicio
- Listado de publicaciones
- Detalle de una publicación
- Página de contacto

La lógica principal se encuentra en la app `posts`, donde se definen las vistas y las URLs del sitio.

## Estructura del proyecto

- `config/`: configuración principal del proyecto Django
- `posts/`: aplicación principal del blog
- `manage.py`: archivo de gestión del proyecto
- `requirements.txt`: dependencias del proyecto

## Funcionalidades

- Vista de inicio en `/`
- Listado de publicaciones en `/posts/`
- Detalle de publicación en `/posts/<id>/`
- Página de contacto en `/contacto/`
- Plantillas reutilizables con base HTML para mantener un diseño consistente

## Requisitos

- Python 3.10 o superior
- Django
- Entorno virtual recomendado

## Instalación

1. Clona el repositorio
2. Entra al proyecto:

   ```bash
   cd semana_8_django
   ```

3. Crea un entorno virtual:

   ```bash
   python -m venv .venv
   ```

4. Activa el entorno virtual:

   En Windows:

   ```bash
   .venv\Scripts\activate
   ```

   En Linux/macOS:

   ```bash
   source .venv/bin/activate
   ```

5. Instala las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

## Ejecución

Ejecuta el servidor de desarrollo:

```bash
python manage.py runserver
```

Luego abre en tu navegador:

```text
http://127.0.0.1:8000/
```

## Migraciones

Si agregas modelos o haces cambios en la base de datos, puedes aplicar migraciones con:

```bash
python manage.py migrate
```

## Autor

Proyecto educativo para practicar Django y desarrollo web con Python.
