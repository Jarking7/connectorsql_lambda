import mysql.connector
import os

def lambda_handler(event, context):
    # Leer variables de entorno
    host = os.environ['db_host']
    user = os.environ['db_usuario']
    password = os.environ['db_password']
    database = os.environ['db_nombre']

    # Conectar a la base de datos
    try:
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )

        cursor = connection.cursor()
        cursor.execute("SELECT * FROM clientes")
        results = cursor.fetchall()

        # Retornar los resultados
        return {
            'statusCode': 200,
            'body': results
        }

    except mysql.connector.Error as err:
        return {
            'statusCode': 500,
            'body': f"Error al conectar a la base de datos: {err}"
        }
    
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()


##utilice un layer para el mysql.connector