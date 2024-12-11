# Práctica 2 - Coderhouse Python

Este es un proyecto académico desarrollado como parte de la materia **Python** de **Coderhouse**. Es mi primer sitio web utilizando **Python**, **Django**, **HTML**, y **CSS** con Bootstrap. El propósito del proyecto es poner en práctica los conceptos aprendidos en la materia.

## **Descripción**

El proyecto consiste en una página web de presentación personal con funcionalidades básicas como:
- Incorporación de formularios para cargar datos en la base de datos.
- Búsqueda de información almacenada en la base de datos.
- Uso de **Django** para manejar el backend y la lógica de la aplicación.
- Uso de **Bootstrap** para estilizar la interfaz.

El proyecto se compone de una sola aplicación llamada `app`, donde se organizan los modelos, formularios, vistas y plantillas.

## **Tecnologías utilizadas**

- **Python 3.11.9**
- **Django 4.2**
- **Bootstrap** (para el diseño de la interfaz)
- **SQLite3** (base de datos por defecto)

## **Estructura del proyecto**

La estructura principal del proyecto es la siguiente:

```
practica2/
├── App/
│   ├── migrations/       # Archivos de migración para la base de datos
│   ├── static/           # Archivos estáticos (CSS, JS, imágenes)
│   ├── templates/        # Plantillas HTML
│   ├── __init__.py       # Archivo de inicialización
│   ├── admin.py          # Configuración del administrador de Django
│   ├── apps.py           # Configuración de la aplicación
│   ├── forms.py          # Definición de formularios
│   ├── models.py         # Definición de modelos de la base de datos
│   ├── tests.py          # Tests automatizados
│   ├── urls.py           # Enrutamiento de URLs
│   ├── views.py          # Lógica de las vistas
├── db.sqlite3            # Base de datos SQLite3
├── manage.py             # Archivo principal para la administración del proyecto
├── requirements.txt      # Lista de dependencias
```

## **Requisitos de instalación**

Para ejecutar el proyecto en tu máquina local, sigue estos pasos:

1. Clona el repositorio desde GitHub:
   ```bash
   git clone https://github.com/LautaroPetersen/practica2.git
   cd practica2
   ```

2. Crea y activa un entorno virtual (opcional, pero recomendado):
   ```bash
   python -m venv venv
   source venv/bin/activate    # En Linux/Mac
   venv\Scripts\activate       # En Windows
   ```

3. Instala las dependencias requeridas:
   ```bash
   pip install -r requirements.txt
   ```

4. Realiza las migraciones para configurar la base de datos:
   ```bash
   python manage.py migrate
   ```

5. Inicia el servidor de desarrollo:
   ```bash
   python manage.py runserver
   ```

6. Accede al proyecto en tu navegador en:  
   `http://127.0.0.1:8000/`

## **Uso del proyecto**

- Navega por las páginas de presentación disponibles.
- Utiliza los formularios para cargar datos en la base de datos.
- Realiza búsquedas en la base de datos a través de los formularios.

## **Contribuciones**

Este proyecto es solo para fines educativos y no está abierto a contribuciones externas en este momento.

## **Licencia**

Este proyecto fue desarrollado como parte de una práctica académica y no incluye una licencia específica.

---

### **Notas adicionales**

- Si tienes alguna duda o sugerencia, no dudes en abrir un issue en el repositorio.
- Recuerda que este proyecto está en desarrollo y puede contener errores o funcionalidades pendientes.
