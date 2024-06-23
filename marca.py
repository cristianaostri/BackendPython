import conexion_db

class Marca:
    tabla = 'marca'
    campos = ('nombre', 'detalle')

    def __init__(self, nombre, detalle, id=None):
        self.id = id
        self.nombre = nombre
        self.detalle = detalle
        self.conexion = conexion_db.conexion()

    def guardar_db(self):
        cursor = self.conexion.cursor()
        consulta = f"INSERT INTO {self.tabla} ({', '.join(self.campos)}) VALUES (%s, %s);"
        datos = (self.nombre, self.detalle)
        cursor.execute(consulta, datos)
        self.conexion.commit()
        cursor.close()

    def modificar(self, **kwargs):
        for campo, valor in kwargs.items():
            if campo in self.campos:
                setattr(self, campo, valor)
        
        cursor = self.conexion.cursor()
        consulta = f"UPDATE {self.tabla} SET nombre = %s, detalle = %s WHERE id = %s;"
        datos = (self.nombre, self.detalle, self.id)
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
    def obtener_marca(cls, id):
        conexion = conexion_db.conexion()
        cursor = conexion.cursor(dictionary=True)
        consulta = f"SELECT * FROM {cls.tabla} WHERE id = %s;"
        cursor.execute(consulta, (id,))
        datos = cursor.fetchone()
        cursor.close()
        if datos:
            return Marca(datos['nombre'], datos['detalle'], id=datos['id'])
        return None
