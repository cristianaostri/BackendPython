from flask import redirect, render_template, request, url_for
import requests

from main import app
from componentes.modelos import Usuarios


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
        contraseña = request.form['new-password']

        # Guardar el usuario en la base de datos
        nuevo_usuario = Usuarios(nombre=nombre, email=email, password=contraseña)
        nuevo_usuario.guardar_db()

        # Redirigir a la página de inicio después del registro exitoso
        return redirect(url_for('inicio'))  
    else:
        return render_template('/formulario/formulario.html')


# @app.route('/sobre_la_tienda')
# def sobre_la_tienda():
#     return render_template('sobre_la_tienda.html')

# @app.route('/contacto')
# def contacto():
#     return render_template('contacto.html')

# @app.route('/sign_in')
# def sign_in():
#     return render_template('sign_in.html')

# @app.route('/sign_up')
# def sign_up():
#     return render_template('sign_up.html')

# if __name__ == '__main__':
#     app.run(debug=True)