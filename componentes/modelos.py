# Clases que corresponden a entidades en la BBDD
from base_db.dml import Tabla
from base_db.config_db import conexion as con
from auxiliares.cifrado import encriptar

class Productos(Tabla):
    
    tabla = 'productos'
    campos = ('nombre', 'precio_venta', 'tipo', 'imagen_url')
    conexion = con
    
    def __init__(self, *args, de_bbdd=False):
        super().crear(args, de_bbdd)
        
class Usuarios(Tabla):
    
    tabla = 'usuarios'
    campos = ('nombre', 'email', 'password')
    conexion = con
    
    def __init__(self, *args, de_bbdd=False):
        
        if not de_bbdd:
            cuenta = []
            cuenta.append(args[0])
            cuenta.append(encriptar(args[1]))
            super().crear(tuple(cuenta), de_bbdd)
        else:
            super().crear(args, de_bbdd)
        

