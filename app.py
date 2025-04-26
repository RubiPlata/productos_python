from flask import Flask
from config import db, migrate
from dotenv import load_dotenv
from flask_cors import CORS
from flasgger import Swagger, LazyString, LazyJSONEncoder
import os

# Cargar variables de entorno
load_dotenv()

# Crear instancia de Flask
app = Flask(__name__)
CORS(app)

# Configurar el JSON encoder para Swagger
app.json_encoder = LazyJSONEncoder

# Configuración de la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Configuración extendida de Swagger
swagger_template = {
    "swagger": "2.0",
    "info": {
        "title": "API de Productos",
        "description": "Documentación completa para la API de gestión de productos",
        "version": "1.0",
        "contact": {
            "name": "Soporte Técnico",
            "url": "http://www.example.com/support",
            "email": "support@example.com"
        }
    },
    "basePath": "/api",  # Asegúrate que coincida con tu url_prefix
    "schemes": [
        "http",
        "https"
    ],
    "definitions": {
        "Producto": {
            "type": "object",
            "properties": {
                "id": {
                    "type": "integer",
                    "example": 1
                },
                "nombre": {
                    "type": "string",
                    "example": "Producto Ejemplo"
                },
                "categoria": {
                    "type": "string",
                    "example": "Electrónicos"
                },
                "cantidad": {
                    "type": "integer",
                    "example": 10
                }
            }
        },
        "ProductoInput": {
            "type": "object",
            "required": ["nombre", "categoria", "cantidad"],
            "properties": {
                "nombre": {
                    "type": "string",
                    "example": "Producto Ejemplo"
                },
                "categoria": {
                    "type": "string",
                    "example": "Electrónicos"
                },
                "cantidad": {
                    "type": "integer",
                    "example": 10
                }
            }
        }
    }
}

swagger_config = {
    "headers": [],
    "specs": [
        {
            "endpoint": 'apispec_1',
            "route": '/apispec_1.json',
            "rule_filter": lambda rule: True,
            "model_filter": lambda tag: True,
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/docs/"
}

# Inicializar extensiones
db.init_app(app)
migrate.init_app(app, db)
swagger = Swagger(app, template=swagger_template, config=swagger_config)

# Registrar rutas
from routes.pro import producto_bp
app.register_blueprint(producto_bp, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True)