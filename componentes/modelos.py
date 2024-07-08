# Clases que corresponden a entidades en la BBDD
from base_db.dml import Tabla
from base_db import config_db
from base_db.config_db import conexion as con
from auxiliares.cifrado import encriptar

class Productos(Tabla):
    
    tabla = 'productos'
    campos = ('id', 'nombre', 'precio_venta', 'tipo', 'imagen_url')
    conexion = con
    
    def __init__(self, *args, de_bbdd=False):
        super().crear(args, de_bbdd)
        
class Usuarios(Tabla):
    
    tabla = 'usuarios'
    campos = ('id','nombre', 'email', 'password')
    conexion = con
    
    def __init__(self, *args, de_bbdd=False):
        if not de_bbdd:
            cuenta = []
            cuenta.append(args[0])
            cuenta.append(encriptar(args[0]))
            super().crear(tuple(cuenta), de_bbdd)
        else:
            super().crear(args, de_bbdd)
    
    @classmethod
    def obtener_por_email(cls, email):
        try:
            consulta = f"SELECT * FROM {cls.tabla} WHERE email = %s;"
            resultado = cls.__conectar(consulta, (email,))
            
            if resultado:
                return cls(*resultado, de_bbdd=True)
            else:
                return None
    
        except Exception as e:
            print(f"Error al obtener usuario por email: {e}")
            return None
        
    @classmethod
    def __conectar(cls, consulta, parametros=None):
        cursor = cls.conexion.cursor()
        cursor.execute(consulta, parametros)
        return cursor.fetchone()

    @classmethod
    def obtener_por_id(cls, id):
        try:
            consulta = "SELECT * FROM usuarios WHERE id = %s"
            parametros = (id,)
            resultado = cls.__conectar(consulta, parametros)  # Llamada al método desde la clase

            if resultado:
                return cls(resultado, de_bbdd=True)
            else:
                return None
        except Exception as e:
            resultado = cls.__conectar(consulta, parametros)
            
    @classmethod
    def autenticar(cls, nombre):
        try:
            conexion = config_db.conexion
            cursor = conexion.cursor(dictionary=True)
            consulta = f"SELECT * FROM {cls.tabla} WHERE nombre = %s;"
            cursor.execute(consulta, (nombre,))
            datos = cursor.fetchone()
            cursor.close()
            if datos:
                return cls(datos['nombre'])
            return None
        except Exception as e:
            cursor.execute(consulta, (nombre,))
            
    @classmethod
    def obtener_usuario(cls, id):
        print(f"El Id traido es: {id}")
        consulta = f"SELECT * FROM {cls.tabla} WHERE id = %s;"
        parametros = (id,)
        try:
            resultado = cls.__conectar(consulta, parametros)
            if resultado:
                return cls(resultado, de_bbdd=True)
            else:
                return None
        except Exception as e:
            resultado = cls.__conectar(consulta, parametros)
            
    @classmethod
    def modificar_por_id(cls, id, nombre, email, password):
        consulta = f"UPDATE {cls.tabla} SET nombre = %s, email = %s, password = %s WHERE id = %s;"
        parametros = (nombre, email, password, id)
        try:
            cursor = cls.conexion.cursor()
            cursor.execute(consulta, parametros)
            cls.conexion.commit()
            cursor.close()
            return True
        except Exception as e:
            cursor = cls.conexion.cursor()
            print(f"Error al modificar usuario: {e}")
            return False
    
class Imagenes(Tabla):
    tabla = 'imagenes'
    campos = ('id','url_img', 'texto_alt')
    conexion = con
    
    def __init__(self, *args, de_bbdd=False):
        
        if not de_bbdd:
            cuenta = []
            cuenta.append(args[0])
            cuenta.append(encriptar(args[1]))
            super().crear(tuple(cuenta), de_bbdd)
        else:
            super().crear(args, de_bbdd)