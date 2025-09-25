import os

# Directorio raíz del proyecto
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "clave_por_defecto")

    # Rutas personalizadas
    CSS_FOLDER = os.path.join(PROJECT_ROOT, 'carta_navidad', 'static', 'css')
    JS_FOLDER = os.path.join(PROJECT_ROOT, 'carta_navidad', 'static', 'js')
    IMAGES_FOLDER = os.path.join(PROJECT_ROOT, 'carta_navidad', 'static', 'img')