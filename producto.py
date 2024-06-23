import conexion_db

class Productos:
    tabla = 'productos'
    campos = ('nombre', 'stock', 'precio_venta', 'id_usuario', 'id_categoria', 'id_marca')

    def __init__(self, nombre, stock, precio_venta, id_usuario, id_categoria, id_marca, id=None):
        self.id = id
        self.nombre = nombre
        self.stock = stock
        self.precio_venta = precio_venta
        self.id_usuario = id_usuario
        self.id_categoria = id_categoria
        self.id_marca = id_marca
        self.conexion = conexion_db.conexion()

    def guardar_db(self):
        cursor = self.conexion.cursor()
        consulta = f"INSERT INTO {self.tabla} ({', '.join(self.campos)}) VALUES (%s, %s, %s, %s, %s, %s);"
        datos = (self.nombre, self.stock, self.precio_venta, self.id_usuario, self.id_categoria, self.id_marca)
        cursor.execute(consulta, datos)
        self.conexion.commit()
        cursor.close()

    def modificar(self, **kwargs):
        for campo, valor in kwargs.items():
            if campo in self.campos:
                setattr(self, campo, valor)
        
        cursor = self.conexion.cursor()
        consulta = f"UPDATE {self.tabla} SET nombre = %s, stock = %s, precio_venta = %s, id_usuario = %s, id_categoria = %s, id_marca = %s WHERE id = %s;"
        datos = (self.nombre, self.stock, self.precio_venta, self.id_usuario, self.id_categoria, self.id_marca, self.id)
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
    def obtener_producto(cls, id):
        conexion = conexion_db.conexion()
        cursor = conexion.cursor(dictionary=True)
        consulta = f"SELECT * FROM {cls.tabla} WHERE id = %s;"
        cursor.execute(consulta, (id,))
        datos = cursor.fetchone()
        cursor.close()
        if datos:
            return Productos(datos['nombre'], datos['stock'], datos['precio_venta'], datos['id_usuario'], datos['id_categoria'], datos['id_marca'], id=datos['id'])
        return None