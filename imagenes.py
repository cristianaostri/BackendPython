import base_db.config_db as config_db

class Imagenes:
    tabla = 'imagenes'
    campos = ('url_img', 'texto_alt')

    def __init__(self, url_img, text_alt, id=None):
        self.id = id
        self.url_img = url_img
        self.text_alt = text_alt
        self.conexion = config_db.conexion()

    def guardar_db(self):
        cursor = self.conexion.cursor()
        consulta = f"INSERT INTO {self.tabla} ({', '.join(self.campos)}) VALUES (%s, %s);"
        datos = (self.url_img, self.text_alt)
        cursor.execute(consulta, datos)
        self.conexion.commit()
        cursor.close()

    def modificar(self, **kwargs):
        for campo, valor in kwargs.items():
            if campo in self.campos:
                setattr(self, campo, valor)
        
        cursor = self.conexion.cursor()
        consulta = f"UPDATE {self.tabla} SET url_img = %s, texto_alt = %s,  WHERE id = %s;"
        datos = (self.url_img, self.text_alt)
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
        conexion = config_db.conexion()
        cursor = conexion.cursor(dictionary=True)
        consulta = f"SELECT * FROM {cls.tabla};"
        cursor.execute(consulta)
        datos = cursor.fetchall()
        cursor.close()
        return datos

    @classmethod
    def obtener_imagenes(cls, id):
        conexion = config_db.conexion()
        cursor = conexion.cursor(dictionary=True)
        consulta = f"SELECT * FROM {cls.tabla} WHERE id = %s;"
        cursor.execute(consulta, (id,))
        datos = cursor.fetchone()
        cursor.close()
        if datos:
            return Imagenes(datos['url_img'], datos['texto_alt'], id=datos['id'])
        return None