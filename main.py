from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
from componentes.vistas_api import *
from componentes.vistas_web import *

app.json.ensure_ascii = False

# Configuración de CORS (si es necesario)
cors = CORS(app, resources={r"/perfumeria/*": {"origins": "*"}})

if __name__ == '__main__':
    app.run(debug=True)

app.secret_key = 'cristian12'
