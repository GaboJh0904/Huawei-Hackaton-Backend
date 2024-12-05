import mysql.connector
from mysql.connector import pooling

class Database:
    __pool = None

    @staticmethod
    def get_connection():
        if Database.__pool is None:
            Database.__pool = pooling.MySQLConnectionPool(
                pool_name="task_manager_pool",
                pool_size=10,
                pool_reset_session=True,
                host="localhost",  # Cambia según tu configuración
                database="EfficientConnect_db",  # Cambia según tu base de datos
                user="root",  # Cambia según tu usuario
                password="1590PPL"  # Cambia según tu contraseña
            )
        return Database.__pool.get_connection()
