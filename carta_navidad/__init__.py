from flask import Flask
from dotenv import load_dotenv
import os

def create_app():
    # Cargar variables de entorno desde el archivo .env
    load_dotenv()

    app = Flask(__name__, static_folder='static', template_folder='templates')

    # Configuración de la aplicación
    app.config.from_object('config.Config')

    # Importar routes
    from . import routes
    routes.init_app(app)

    return app