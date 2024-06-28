from flask import render_template

from main import app
from componentes.modelos import Usuarios


# ****** Inicio ******
@app.route('/')
def inicio():
    return render_template('./base.html')
