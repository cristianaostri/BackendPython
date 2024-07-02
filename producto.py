import base_db.config_db as config_db

class Productos:
    tabla = 'productos'
    campos = ('nombre', 'precio_venta', 'tipo', 'imagen_url')

    def __init__(self, nombre, precio_venta, tipo, imagen_url, id=None):
        self.id = id
        self.nombre = nombre
        self.precio_venta = precio_venta
        self.tipo = tipo
        self.imagen_url = imagen_url
        self.conexion = config_db.conexion()

    def guardar_db(self):
        cursor = self.conexion.cursor()
        consulta = f"INSERT INTO {self.tabla} ({', '.join(self.campos)}) VALUES (%s, %s, %s, %s);"
        datos = (self.nombre, self.precio_venta, self.tipo, self.imagen_url)
        cursor.execute(consulta, datos)
        self.conexion.commit()
        cursor.close()

    def modificar(self, **kwargs):
        for campo, valor in kwargs.items():
            if campo in self.campos:
                setattr(self, campo, valor)
        
        cursor = self.conexion.cursor()
        consulta = f"UPDATE {self.tabla} SET nombre = %s, precio_venta = %s, tipo = %s, imagen_url = %s, WHERE id = %s;"
        datos = (self.nombre, self.precio_venta, self.tipo, self.imagen_url, self.id)
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
            return [cls(producto['nombre'], producto['precio_venta'], producto['tipo'], producto['imagen_url'], id=producto['id']) for producto in datos]
        else:
            print("Los datos obtenidos no son una lista de diccionarios.")
            return []

    @classmethod
    def obtener_producto(cls, id):
        conexion = config_db.conexion
        cursor = conexion.cursor(dictionary=True)
        consulta = f"SELECT * FROM {cls.tabla} WHERE id = %s;"
        cursor.execute(consulta, (id,))
        datos = cursor.fetchone()
        cursor.close()
        if datos:
            return Productos(datos['nombre'], datos['precio_venta'], datos['tipo'], datos['imagen_url'], id=datos['id'])
        return None