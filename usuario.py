import base_db.config_db as config_db

class Usuarios:
    tabla = 'usuarios'
    campos = ('nombre', 'email', 'password')

    def __init__(self, nombre, email, password, id=None):
        self.id = id
        self.nombre = nombre
        self.email = email
        self.password = password
        self.conexion = config_db.conexion

    def guardar_db(self):
        cursor = self.conexion.cursor()
        consulta = f"INSERT INTO {self.tabla} ({', '.join(self.campos)}) VALUES (%s, %s, %s);"
        datos = (self.nombre, self.email, self.password)
        cursor.execute(consulta, datos)
        self.conexion.commit()
        cursor.close()

    def modificar(self, **kwargs):
        # Actualizar solo los campos que se pasan como argumentos de palabras clave
        for campo, valor in kwargs.items():
            if campo in self.campos:
                setattr(self, campo, valor)
        
        cursor = self.conexion.cursor()
        consulta = f"UPDATE {self.tabla} SET nombre = %s, email = %s, password = %s WHERE id = %s;"
        datos = (self.nombre, self.email, self.contraseña, self.id)
        cursor.execute(consulta, datos)
        self.conexion.commit()
        cursor.close()

    def eliminar(self):
        cursor = self.conexion.cursor()
        consulta = f"DELETE FROM {self.tabla} WHERE id = %s;"
        datos = (self.id,)
        cursor.execute(consulta, datos)
        self.conexion.commit()
        cursor.close()

    @classmethod
    def obtener_todos(cls):
        conexion = config_db.conexion
        cursor = conexion.cursor(dictionary=True)
        consulta = f"SELECT * FROM {cls.tabla};"
        cursor.execute(consulta)
        datos = cursor.fetchall()
        cursor.close()
        
        if isinstance(datos, list) and datos and isinstance(datos[0], dict):
            return [cls(usuario['nombre'], usuario['email'], usuario['password'], id=usuario['id']) for usuario in datos]
        else:
            print("Los datos obtenidos no son una lista de diccionarios.")
            return []

    @classmethod
    def obtener_usuario(cls, id):
        conexion = config_db.conexion
        cursor = conexion.cursor(dictionary=True)
        consulta = f"SELECT * FROM {cls.tabla} WHERE id = %s;"
        cursor.execute(consulta, (id,))
        datos = cursor.fetchone()
        cursor.close()
        if datos:
            return Usuarios(datos['nombre'], datos['email'], datos['password'], id=datos['id'])
        return None


    @classmethod
    def autenticar(cls,nombre, password):
        conexion = config_db.conexion
        cursor = conexion.cursor(dictionary=True)
        consulta = "SELECT * FROM {cls.tabla} WHERE nombre = %s AND password = %s"
        cursor.execute(consulta, (nombre, password))
        usuario = cursor.fetchone()
        cursor.close()
        return usuario