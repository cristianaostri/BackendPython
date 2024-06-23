import conexion_db

class Usuarios:
    tabla = 'usuarios'
    campos = ('nombre', 'email', 'contraseña', 'comentario', 'categoria', 'edad')

    def __init__(self, nombre, email, contraseña, comentario, categoria, edad, id=None):
        self.id = id
        self.nombre = nombre
        self.email = email
        self.contraseña = contraseña
        self.comentario = comentario
        self.categoria = categoria
        self.edad = edad
        self.conexion = conexion_db.conexion()

    def guardar_db(self):
        cursor = self.conexion.cursor()
        consulta = f"INSERT INTO {self.tabla} ({', '.join(self.campos)}) VALUES (%s, %s, %s, %s, %s, %s);"
        datos = (self.nombre, self.email, self.contraseña, self.comentario, self.categoria, self.edad)
        cursor.execute(consulta, datos)
        self.conexion.commit()
        cursor.close()

    def modificar(self, **kwargs):
        # Actualizar solo los campos que se pasan como argumentos de palabras clave
        for campo, valor in kwargs.items():
            if campo in self.campos:
                setattr(self, campo, valor)
        
        cursor = self.conexion.cursor()
        consulta = f"UPDATE {self.tabla} SET nombre = %s, email = %s, contraseña = %s, comentario = %s, categoria = %s, edad = %s WHERE id = %s;"
        datos = (self.nombre, self.email, self.contraseña, self.comentario, self.categoria, self.edad, self.id)
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
        conexion = conexion_db.conexion()
        cursor = conexion.cursor(dictionary=True)
        consulta = f"SELECT * FROM {cls.tabla};"
        cursor.execute(consulta)
        datos = cursor.fetchall()
        cursor.close()
        return datos

    @classmethod
    def obtener_usuario(cls, id):
        conexion = conexion_db.conexion()
        cursor = conexion.cursor(dictionary=True)
        consulta = f"SELECT * FROM {cls.tabla} WHERE id = %s;"
        cursor.execute(consulta, (id,))
        datos = cursor.fetchone()
        cursor.close()
        if datos:
            return Usuarios(datos['nombre'], datos['email'], datos['contraseña'], datos['comentario'], datos['categoria'], datos['edad'], id=datos['id'])
        return None
