import conexion_db

class Detalle_Carrito:
    tabla = 'detalle_carrito'
    campos = ('cantidad', 'precio_unitario', 'id_carrito', 'id_producto')

    def __init__(self, cantidad, precio_unitario, id_carrito, id_producto, id=None):
        self.id = id
        self.cantidad = cantidad
        self.precio_unitario = precio_unitario
        self.id_carrito = id_carrito
        self.id_producto = id_producto
        self.conexion = conexion_db.conexion()

    def guardar_db(self):
        cursor = self.conexion.cursor()
        consulta = f"INSERT INTO {self.tabla} ({', '.join(self.campos)}) VALUES (%s, %s, %s, %s);"
        datos = (self.cantidad, self.precio_unitario, self.id_carrito, self.id_producto)
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
    def obtener_detalle(cls, id):
        conexion = conexion_db.conexion()
        cursor = conexion.cursor(dictionary=True)
        consulta = f"SELECT * FROM {cls.tabla} WHERE id = %s;"
        cursor.execute(consulta, (id,))
        datos = cursor.fetchone()
        cursor.close()
        if datos:
            return Detalle_Carrito(datos['cantidad'], datos['precio_unitario'], datos['id_carrito'], datos['id_producto'], id=datos['id'])
        return None