import base_db.config_db as config_db

class Usuarioss:
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

    def modificar(self, nombre=None, email=None, password=None):
        # Actualizar solo los campos que se pasan como argumentos de palabras clave
        if nombre:
            self.nombre = nombre
        if email:
            self.email = email
        if password:
            self.password = password
        
        cursor = self.conexion.cursor()
        consulta = f"UPDATE {self.tabla} SET nombre = %s, email = %s, password = %s WHERE id = %s;"
        datos = (self.nombre, self.email, self.password, self.id)
        cursor.execute(consulta, datos)
        self.conexion.commit()
        cursor.close()

    # def modificar(self, **kwargs):
    #     # Actualizar solo los campos que se pasan como argumentos de palabras clave
    #     for campo, valor in kwargs.items():
    #         if campo in self.campos:
    #             setattr(self, campo, valor)
        
    #     cursor = self.conexion.cursor()
    #     consulta = f"UPDATE {self.tabla} SET nombre = %s,  email = %s, password = %s WHERE id = %s;"
    #     datos = (self.nombre, self.email, self.password, self.id)
    #     cursor.execute(consulta, datos)
    #     self.conexion.commit()
    #     cursor.close()
        
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
            return Usuarioss(datos['nombre'], datos['email'], datos['password'], id=datos['id'])
        return None


    @classmethod
    def autenticar(cls, nombre, password, email=None ):
        conexion = config_db.conexion
        cursor = conexion.cursor(dictionary=True)
        consulta = f"SELECT * FROM {cls.tabla} WHERE nombre = %s AND password = %s"
        cursor.execute(consulta, (nombre, password))
        usuario = cursor.fetchone()
        cursor.close()
        if usuario:
            return cls(usuario['nombre'], usuario['email'], usuario['password'], id=usuario['id'])
        return None
    @classmethod
    def actualizar(cls, nombre=None, email=None, password=None):
        # usuario = cls.obtener_usuario()
        # if usuario:    
        if nombre is not None:
            cls.nombre = nombre
        if email is not None:
            cls.email = email
        if password is not None:
            cls.password = password
        # else:
    
            raise ValueError("El objeto Usuarios no tiene un ID válido.")
        
        cursor = cls.conexion.cursor()
        consulta = f"UPDATE {cls.tabla} SET nombre = %s, email = %s, password = %s WHERE id = %s;"
        datos = (cls.nombre, cls.email, cls.password, cls.id)
        cursor.execute(consulta, datos)
        cls.conexion.commit()
        cursor.close()