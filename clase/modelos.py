"""import conexion_db

class Productos:
    tabla = 'productos'
    campos = ('id', 'nombre', 'stock', 'precio_venta', 'id_usuario', 'id_categoria', 'id_marca')
    conexion = conexion_db.conexion
    
    def __init__(self, nombre, stock, precio_venta, id_usuario, id_categoria, id_marca):
        self.nombre = nombre
        self.stock = stock
        self.precio_venta = precio_venta
        self.id_usuario = id_usuario
        self.id_categoria = id_categoria
        self.id_marca = id_marca
    
    def guardar_db(self):
        self.conexion.connect()
        cursor = self.conexion.cursor()
        consulta = f""""""
        datos = (self.nombre, self.stock, self.precio_venta, self.id_usuario, self.id_categoria, self.id_marca)    
        cursor.execute(consulta, datos) 
        self.conexion.commit()
        self.conexion.close()
"""

"""INSERT INTO {self.tabla} (nombre, stock, precio_venta, id_usuario, id_categoria, id_marca) VALUES (%s, %s, %s, %s, %s, %s);"""