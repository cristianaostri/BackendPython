from usuarios.crear_user import crear_usuario
from usuarios.sesion import iniciar_sesion

opcion = ''
menu = """
** menú**
1 Crear usuario
2. Iniicar SEsion
3 - Salir
"""

while opcion != "3":
    print(menu)
    opcion = input("Ingrese su opcion: ")
    
    if opcion == "1":
        crear_usuario()
    elif opcion == "2":
        saludo = iniciar_sesion()
        print(saludo)
    elif opcion == "3":
        print("Adios")
    else:
        print("Opcion incorrecta")
        
        
        