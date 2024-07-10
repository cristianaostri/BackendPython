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

conexion = mysql.connector.connect(**config_prod)