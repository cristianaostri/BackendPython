import mysql.connector

config_dev = {
    # configuración en desarrollo (local)
    "user": 'root',
    'password': '',
    'host': '127.0.0.1',
    'database': 'perfumeria'
}

config_prod = {
    # configuración en producción (despliegue)
    "user": 'cial610',
    'password': 'Programacion12',
    'host': 'cial610.mysql.pythonanywhere-services.com',
    'database': 'cial610$perfumeria'
}

def create_connection():
    try:
        conexion = mysql.connector.connect(**config_prod)
        if conexion.is_connected():
            return conexion
    except Error as e:
        print("Error en la conexión a la base de datos:", e)
        return None

conexion = create_connection()