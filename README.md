# Archi_Media_Master

## Descripción

Archi_Media_Master es un proyecto Django que incluye un backend para gestionar artículos de noticias y un frontend para mostrar y generar contenido utilizando un modelo de IA local.

Aqui la interaccion principales son el backend con el frontend, y el backend con el servicio de IA.

## Requisitos

Asegúrate de tener instalado Python 3.6 o superior. También necesitarás instalar las dependencias listadas en `requirements.txt`.

## Instalación

1. Clona el repositorio:

   ```bash
   git clone https://github.com/tu_usuario/Archi_Media_Master.git
   cd Archi_Media_Master
   ```

2. Crea y activa un entorno virtual:

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

3. Instala las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

4. Realiza las migraciones de la base de datos:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Carga datos de ejemplo en la base de datos (opcional):

   ```bash
   python manage.py shell
   from backend.models import NewsArticle
   NewsArticle.objects.create(title="Sample Article", content="This is a sample article.")
   ```

## Uso

1. Inicia el servidor de desarrollo:

   ```bash
   python manage.py runserver
   ```

2. Abre tu navegador y ve a `http://127.0.0.1:8000/articles/` para ver la lista de artículos.

3. Haz clic en el botón "Generate Content" para generar contenido utilizando el modelo de IA.

## Estructura del Proyecto

```
Archi_Media_Master/
├── ai_service_content/
│   └── ai_service.py
├── backend/
│   ├── __init__.py
│   ├── asgi.py
│   ├── models.py
│   ├── settings.py
│   ├── urls.py
│   ├── views.py
│   └── wsgi.py
├── frontend/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations/
│   │   └── __init__.py
│   ├── models.py
│   ├── templates/
│   │   └── frontend/
│   │       └── article_list.html
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── manage.py
└── requirements.txt
```

## Dependencias

Las principales dependencias del proyecto incluyen:

- Django==5.1.3
- nltk==3.6.3
- requests==2.26.0
- torch==1.9.0
- transformers==4.9.2

## Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue o un pull request para discutir cualquier cambio que te gustaría hacer.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.


