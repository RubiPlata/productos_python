"# python_5" 

python -m venv venv

activate windows venv\Scripts\activate

pip install flask flask-sqlalchemy pymysql flask-migrate python-dotenv


#migraciones
flask db init
flask db migrate -m "Initial migration"
flask db upgrade

---------------------------------------

1. Directorio app/
Este es el núcleo de tu aplicación. Contiene las carpetas y archivos principales organizados por lógica.

a) controllers/
Contiene los controladores, que son responsables de manejar la lógica de negocio y procesar las solicitudes HTTP. En este caso, tienes:
productController.py: Controlador para manejar operaciones relacionadas con productos.
userController.py: Controlador para manejar operaciones relacionadas con usuarios.
__pycache__/: Carpeta generada automáticamente por Python para almacenar archivos bytecode compilados.
b) models/
Contiene los modelos, que representan las entidades de tu aplicación y cómo se mapean a la base de datos. En este caso, tienes:
Product.py: Modelo para productos.
User.py: Modelo para usuarios.
__init__.py: Archivo especial que convierte el directorio en un paquete Python. Puede estar vacío o incluir inicializaciones.
c) routes/
Contiene las rutas de tu aplicación, que mapean las solicitudes HTTP a controladores específicos. En este caso, tienes:
product.py: Define las rutas relacionadas con productos.
user.py: Define las rutas relacionadas con usuarios.
config.py: Archivo de configuración relacionado con las rutas o inicialización del servidor.
__init__.py: Hace que esta carpeta sea tratada como un paquete Python.
2. Directorio migrations/
Relacionado con la gestión de esquemas de la base de datos. Es común cuando se utiliza un ORM como SQLAlchemy con Alembic.
Contiene:
alembic.ini: Archivo de configuración para Alembic.
env.py: Archivo generado por Alembic para configurar el entorno de migraciones.
script.py.mako: Plantilla utilizada para generar archivos de migración.
versions/: Carpeta donde se almacenan las migraciones generadas.
3. Directorio venv/
Es el entorno virtual de Python.
Contiene todos los paquetes y dependencias instalados para este proyecto. Las subcarpetas principales son:
Include/, Lib/, Scripts/: Directorios que almacenan las bibliotecas, scripts y archivos ejecutables del entorno virtual.
pyvenv.cfg: Archivo de configuración que describe el entorno virtual.
4. Archivo app.py
Probablemente es el punto de entrada principal de la aplicación. Aquí se inicia el servidor o se configura la aplicación para que comience a ejecutarse.
5. Archivo README.md
Archivo de documentación donde puedes describir tu proyecto, cómo instalarlo, configurarlo y usarlo.
6. Archivo requirements.txt
Contiene una lista de las dependencias del proyecto con sus versiones. Puedes instalar todas estas dependencias con:
bash
Copy code
pip install -r requirements.txt
Resumen de flujo lógico:
Punto de entrada (app.py):
Inicializa la aplicación, conecta controladores, modelos y rutas.
Controladores (controllers/):
Procesan las solicitudes HTTP y ejecutan lógica de negocio.
Modelos (models/):
Representan los datos y su estructura en la base de datos.
Rutas (routes/):
Mapean las solicitudes HTTP a los controladores correspondientes.
Migraciones (migrations/):
Gestionan los cambios en la estructura de la base de datos.
Entorno virtual (venv/):
Asegura que las dependencias sean específicas para este proyecto.
Si tienes dudas sobre alguna parte o necesitas ejemplos, ¡déjamelo saber! 😊

# http://127.0.0.1:5000/apidocs/

# pip install flasgger

