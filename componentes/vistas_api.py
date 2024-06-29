from flask import jsonify


# Vistas para la arquitectura API REST
from flask import jsonify
from main import app
from componentes.modelos import Productos

@app.route('/perfumeria/productos')
def mostrar_productos():
    productos =  Productos.obtener()
    dicc_productos = [p.__dict__ for p in productos]
    return jsonify(dicc_productos)


    # usuario

    @app.route("/api-edtech/cuenta", methods=['POST'])
def crear_cuenta():
    
    if request.method == 'POST':
        datos = request.json["datos"]
        cta_nueva = Cuenta(
            datos['nombre'], #cambie los 3 datos
            datos['email'],
            datos['password'],
        )
        respuesta = {}
       
        try:
            cta_nueva.guardar_db()
            respuesta['mensaje'] = 'Usuario creado con éxito!' #cambie mensaje
            respuesta['status'] = 200
        except Exception as e:
            respuesta['mensaje'] = 'No se puedo crear el usuario!' #cambie mensaje
            respuesta['status'] = 409
            
    else:
        respuesta['mensaje'] = 'No se recibieron datos.'
        respuesta['status'] = 204    

    return jsonify(respuesta)

@app.route('/api-edtech/validar', methods=['POST'])
def validar_cuenta():
    respuesta = {}    
    
    if request.method == 'POST':
        datos = request.json["datos"]
        ingreso = Cuenta(datos['correo'], datos['contrasenia']) #No cambie nada
        cuenta = Cuenta.obtener('correo', datos['correo'])
        
        
        if cuenta and ingreso.clave == cuenta.clave:
            usuario = Usuario.obtener('id_cuenta', cuenta.id) #cambien estudiante por usuario

            if not usuario:
                respuesta['perfil'] = 0
            else:
                respuesta['perfil'] = 1
            
            respuesta['mensaje'] = 'Ingreso exitoso!'
            respuesta['status'] = 200
        else:
            respuesta['mensaje'] = 'Verifique los datos enviados.'
            respuesta['status'] = 409
    
    return jsonify(respuesta)

 