from flask import redirect, render_template, request, url_for
import requests

from main import app
from componentes.modelos import Usuarios
from usuario import Usuarioss
# ****** Inicio ******
# @app.route('/')
# def inicio():
#     return render_template('./home/base.html')
@app.route('/')
def inicio():
    # Hacer la solicitud a la API de las imágenes
    try:
        response = requests.get('http://localhost:5000/perfumeria/imagenes')
        if response.status_code == 200:
            imagenes = response.json()
            return render_template('inicio.html', imagenes=imagenes)
        else:
            # Manejar el caso de error si la API no responde correctamente
            return render_template('inicio.html', imagenes=[])
    except requests.exceptions.RequestException as e:
        # Manejar errores de conexión
        print(f"Error al hacer la solicitud a la API: {e}")
        return render_template('inicio.html', imagenes=[])
# @app.route('/productos')
# def productos():
#     return render_template('productos.html') 

@app.route('/perfumeria/registro', methods=['GET', 'POST'])
def cargando_datos():
    if request.method == 'POST':
        nombre = request.form['first-name']
        email = request.form['email']
        password = request.form['new-password']
        print(nombre, email, password)
        # Guardar el usuario en la base de datos
        nuevo_usuario = Usuarios(nombre, email, password)
        print(nuevo_usuario)
        nuevo_usuario.guardar_db()

        # Redirigir a la página de inicio después del registro exitoso
        return redirect(url_for('inicio'))  
    else:
        return render_template('/formulario/formulario.html')

@app.route('/perfumeria/contacto')
def tienda():
    return render_template('/contacto/contacto.html') 


@app.route('/perfumeria/infotienda')
def contacto():
    return render_template('/sobre_tienda/tienda.html') 

@app.route('/perfumeria/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        usuario = Usuarios(username, password)
        print(type(usuario))
        print(usuario)
        usuarios = Usuarioss.autenticar(username,password)
        if usuarios:
            aviso = f"Bienvenido {usuario.nombre}"
            usuarios = obtener_usuarios_desde_api()
            
            return render_template('./admin/admin.html', aviso=aviso, usuarios=usuarios, usuario=usuario)
            
            # return redirect(url_for('inicio'))  # Redirigir a la página de inicio
        else:
            # Autenticación fallida
            print("pasó por acá")
            error = 'Credenciales inválidas. Por favor, inténtalo de nuevo.'
            return render_template('/inicio_sesion/sesion.html', error=error)
    else:
        return render_template('/inicio_sesion/sesion.html')


@app.route('/perfumeria/productos', methods=['GET', 'POST'])
def ventas():
    return render_template('/productos/productos.html') 


# Ruta para modificar un usuario (GET para obtener el formulario de modificación)
@app.route('/modificar_usuario/<int:usuario_id>', methods=['GET'])
def mostrar_formulario_modificar(usuario_id):
    usuario = Usuarioss.obtener_usuario(usuario_id)
    print(usuario)
    return render_template('formulario_modificar_usuario.html', usuario=usuario)

# Ruta para procesar la modificación de un usuario (POST para actualizar en la base de datos)
@app.route('/modificar_usuario/<int:usuario_id>', methods=['POST'])
def modificar_usuario(usuario_id):
    # Obtener datos del formulario de modificación
    print("*********  ***************  **************")
    
    nombre = request.form['nombre']
    email = request.form['email']
    password = request.form['password']
    usuario = Usuarioss.obtener_usuario(usuario_id)
    print(f"nombre: {nombre}, email: {email} password: {password}")
    
    # Usuarios.actualizar(usuario_id, nombre, email, password)
    usuario.modificar(nombre=nombre, email=email, password=password)
    
    return redirect(url_for('login'))  


@app.route('/eliminar/<int:usuario_id>', methods=['POST'])
def eliminar_usuario(usuario_id):
    usuario = Usuarioss.obtener_usuario(usuario_id)
    print(usuario.id)
    print("*"*20)
    print(usuario)
    usuario.eliminar()
    return redirect(url_for('inicio'))  


def obtener_usuarios_desde_api():
    # URL de la API donde se obtienen los usuarios
    api_url = 'http://localhost:5000/perfumeria/usuarios'

    # Realizar la solicitud GET a la API
    response = requests.get(api_url)

    # Verificar si la solicitud fue exitosa (código 200)
    if response.status_code == 200:
        usuarios = response.json()  # Convertir la respuesta JSON en un diccionario de Python
        return usuarios
    else:
        return f'Error al obtener usuarios desde la API. Código de estado: {response.status_code}'
    
    
    