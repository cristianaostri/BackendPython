def validar_cadena(dato):
    
    if dato.isalpha():
        return False

def crear_usuario():
    nombre = input("ingrese su nombre: ")

    if validar_cadena(nombre):
       print(f"Se creo usuario: {nombre}")
    else:
        print("DATO INVÁLIDO PARA NOMBRE")
    
    
