# test1.py
from usuario import Usuarioss

# Insertar un nuevo usuario
nuevo_usuario = Usuarioss('cris', 'prueba_deb@gmail.com', 'prueba123' )
print(nuevo_usuario)
nuevo_usuario.guardar_db()
# print(nuevo_usuario)
# # Modificar un usuario existente
# usuario_existente = Usuarios.obtener_usuario(1)  # Obtener el usuario con id 1
# if usuario_existente:
#     usuario_existente.modificar(nombre='Johnathan Doe', email='johnathan.doe@example.com')

# Eliminar un usuario
# usuario_a_eliminar = Usuarios.obtener_usuario(6) 
# print(usuario_a_eliminar.__dict__)
# Obtener el usuario con id 2
# if usuario_a_eliminar:
#     usuario_a_eliminar.eliminar()

# # Obtener todos los usuarios
todos_los_usuarios = Usuarioss.obtener_todos()  # Llamada al método con paréntesis
for usuario in todos_los_usuarios:
    print(usuario.__dict__)

todos_los_usuarios = Usuarioss.obtener_todos()  # Llamada al método con paréntesis
for usuario in todos_los_usuarios:
    print(usuario.__dict__)


