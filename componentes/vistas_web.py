from flask import flash, redirect, render_template, request, url_for
import requests
from main import app
from componentes.modelos import Usuarios

# Ruta principal, muestra imágenes de la perfumería
@app.route('/')
def inicio():
    try:
        # Usa la URL pública de tu API
        response = requests.get('http://localhost:5000/perfumeria/imagenes')
        if response.status_code == 200:
            imagenes = response.json()
            return render_template('inicio.html', imagenes=imagenes)
        else:
            print(f"Error: Recibido código de estado {response.status_code}")
            return render_template('inicio.html', imagenes=[])
    except requests.exceptions.RequestException as e:
        print(f"Error al hacer la solicitud a la API: {e}")
        return render_template('inicio.html', imagenes=[])

# Ruta para registrar un nuevo usuario
@app.route('/perfumeria/registro', methods=['GET', 'POST'])
def cargando_datos():
    if request.method == 'POST':
        nombre = request.form['first-name']
        email = request.form['email']
        password = request.form['new-password']

        nuevo_usuario = Usuarios(nombre, email, password)
        nuevo_usuario.guardar_db()

        return redirect(url_for('inicio'))  # Redirigir a la página de inicio después del registro exitoso
    else:
        return render_template('/formulario/formulario.html')
@app.route('/perfumeria/contacto')
def tienda():
        return render_template('/sobre_tienda/tienda.html')




@app.route('/perfumeria/infotienda')
def contacto():
    return render_template('/contacto/contacto.html')

# Ruta para autenticar y hacer login de usuarios
@app.route('/perfumeria/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']


        # No es necesario convertir a diccionario
        usuario = Usuarios(username, None, password)  # Opcionalmente, pasas None o un valor para email

        print(usuario.nombre)

        # Obtener usuario por nombre y validar la contraseña
        usuario_completo = Usuarios.autenticar(usuario.nombre)
        print(usuario_completo)
        if usuario_completo:
            aviso = f"Bienvenido {usuario.nombre}"
            usuarios = Usuarios.obtener()
            print("se fue")
            return render_template('./admin/admin.html', aviso=aviso, usuarios=usuarios)
        else:
            error = 'Credenciales inválidas. Por favor, inténtalo de nuevo.'
            return render_template('/inicio_sesion/sesion.html', error=error)
    else:
        return render_template('/inicio_sesion/sesion.html')

@app.route('/perfumeria/productos', methods=['GET', 'POST'])
def ventas():

    return render_template('/productos/productos.html')


# # Ruta para mostrar todos los productos disponibles
# @app.route('/perfumeria/productos')
# def productos():
#     try:
#         response = requests.get('http://localhost:5000/perfumeria/productos')
#         if response.status_code == 200:
#             productos = response.json()
#             return render_template('productos.html', productos=productos)
#         else:
#             return render_template('productos.html', productos=[])
#     except requests.exceptions.RequestException as e:
#         print(f"Error al hacer la solicitud a la API: {e}")
#         return render_template('productos.html', productos=[])

# Ruta para modificar un usuario (GET para obtener el formulario de modificación)
@app.route('/modificar_usuario/<int:usuario_id>', methods=['GET'])
def mostrar_formulario_modificar(usuario_id):
    print(usuario_id)
    print("muestra el formulario")
    usuario = Usuarios.obtener_usuario(usuario_id)
    print(usuario)
    if usuario:
        return render_template('formulario_modificar_usuario.html', usuario=usuario)
    else:
        # Manejar el caso en que el usuario no se encuentre en la base de datos
        return "Usuario no encontrado"


# Ruta para procesar la modificación de un usuario (POST para actualizar en la base de datos)
@app.route('/modificar_usuario/<int:usuario_id>', methods=['POST'])
def modificar_usuario(usuario_id):
    # Obtener datos del formulario de modificación
    nombre = request.form.get('nombre')
    email = request.form.get('email')
    password = request.form.get('password')

    # Validar que todos los campos necesarios estén presentes
    if not (nombre and email and password):
        flash('Por favor, complete todos los campos para modificar el usuario.', 'error')
        return redirect(url_for('modificar_usuario'))  # Redirigir a la página de formulario de modificación

    # Modificar el usuario en la base de datos
    if Usuarios.modificar_por_id(usuario_id, nombre, email, password):
        flash('Usuario modificado exitosamente.', 'success')
    else:
        flash(f'Error al modificar usuario.', 'error')

    return redirect(url_for('login', usuario_id=usuario_id))  # Redirigir a la página de formulario de modificación

# Ruta para eliminar un usuario
@app.route('/eliminar_usuario/<int:usuario_id>', methods=['POST'])
def eliminar_usuario(usuario_id):
    print("llegué")
    print(usuario_id)
    usuario = Usuarios.obtener_por_id(usuario_id)
    usuario.eliminar()
    return redirect(url_for('inicio'))  # Redirigir a la página de inicio después de eliminar el usuario

# Función para obtener todos los usuarios desde la API
def obtener_usuarios_desde_api():
    try:
        response = requests.get('http://localhost:5000/perfumeria/usuarios')
        if response.status_code == 200:
            usuarios = response.json()
            return usuarios
        else:
            return f'Error al obtener usuarios desde la API. Código de estado: {response.status_code}'
    except requests.exceptions.RequestException as e:
        return f'Error al obtener usuarios desde la API: {e}'
