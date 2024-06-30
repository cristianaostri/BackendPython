from flask import jsonify


# Vistas para la arquitectura API REST
from flask import jsonify
from main import app
from componentes.modelos import Productos
from componentes.modelos import Imagenes
@app.route('/perfumeria/productos')
def mostrar_productos():
    productos =  Productos.obtener()
    dicc_productos = [p.__dict__ for p in productos]
    return jsonify(dicc_productos)

@app.route('/perfumeria/imagenes')
def mostrar_imagenes():
    productos =  Imagenes.obtener()
    dicc_productos = [p.__dict__ for p in productos]
    return jsonify(dicc_productos)