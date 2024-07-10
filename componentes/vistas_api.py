from flask import jsonify


# Vistas para la arquitectura API REST
from flask import jsonify
from main import app
from componentes.modelos import Productos
from componentes.modelos import Imagenes
from componentes.modelos import Usuarios

@app.route('/perfumeria/api_productos')
def mostrar_productos():
    productos =  Productos.obtener()
    dicc_productos = [p.__dict__ for p in productos]
    return jsonify(dicc_productos)

@app.route('/perfumeria/imagenes')
def mostrar_imagenes():
    productos =  Imagenes.obtener()
    dicc_productos = [p.__dict__ for p in productos]
    return jsonify(dicc_productos)

@app.route('/perfumeria/usuarios')
def mostrar_usuarios():
    usuario = Usuarios.obtener()
    dicc_productos = [u.__dict__ for u in usuario]
    return jsonify(dicc_productos)
