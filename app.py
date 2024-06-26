from flask import Flask, jsonify
from usuario import Usuarios

app = Flask(__name__)

# Vistas
@app.route('/')
def inicio():
    return "<h1>Bienvenid@s a Flask!!!</h1>"

@app.route('/api/test')
def mostrar_usuario():
    usuario = Usuarios.obtener_usuario(1)  # Obtener el usuario con ID 1, ajusta según tu lógica
    if usuario:
        return jsonify({
            
            'nombre': usuario.nombre,
            'email': usuario.email,
            
        })
    else:
        return jsonify({'error': 'Usuario no encontrado'}), 404

if __name__ == "__main__":
    app.run(debug=True)
