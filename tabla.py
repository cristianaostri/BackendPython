# tabla.py
import config_db

class Tabla:
    conexion = config_db.conexion

    @classmethod
    def obtener_todos(cls):
        conn = cls.conexion.connect()
        cursor = conn.cursor()
        consulta = f"SELECT * FROM {cls.tabla}"
        cursor.execute(consulta)
        datos = cursor.fetchall()
        conn.close()
        return [cls(*dato) for dato in datos]

    @classmethod
    def obtener_por_id(cls, id):
        conn = cls.conexion.connect()
        cursor = conn.cursor()
        consulta = f"SELECT * FROM {cls.tabla} WHERE id = %s;"
        datos = (id,)
        cursor.execute(consulta, datos)
        dato = cursor.fetchone()
        conn.close()
        return cls(*dato)

    def eliminar(self):
        conn = self.conexion.connect()
        cursor = conn.cursor()
        consulta = f"DELETE FROM {self.tabla} WHERE id = %s;"
        datos = (self.id,)
        cursor.execute(consulta, datos)
        conn.commit()
        conn.close()
