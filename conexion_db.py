import mysql.connector

def conexion():
    return mysql.connector.connect(
        user='root',
        password='',
        host='127.0.0.1',
        database='perfumeria'
    )



""" import mysql.connector
# establezco la conexion
config_dev = {
    'user': 'root',
    'password': '',
    'host': '127.0.0.1',
    'database': 'perfumeria'
    
}

config_prod = {}
conexion = mysql.connector.connect(**config_dev) # los ** signos transforma el disccionario en asignaciones.


"""