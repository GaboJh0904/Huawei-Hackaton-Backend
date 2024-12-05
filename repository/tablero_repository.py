from database.connection import Database

class TableroRepository:

    @staticmethod
    def get_all():
        connection = Database.get_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("""
            SELECT Tablero.id, Tablero.nombre, Tablero.descripcion, Tablero.fecha_creacion, 
                   Tablero.Familia_empresa_id AS familia_empresa_id,
                   Familia_empresa.nombre AS familia_empresa_nombre
            FROM Tablero
            INNER JOIN Familia_empresa ON Tablero.Familia_empresa_id = Familia_empresa.id
        """)
        results = cursor.fetchall()
        connection.close()
        return results

    @staticmethod
    def get_by_id(tablero_id):
        connection = Database.get_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("""
            SELECT Tablero.id, Tablero.nombre, Tablero.descripcion, Tablero.fecha_creacion, 
                   Tablero.Familia_empresa_id AS familia_empresa_id,
                   Familia_empresa.nombre AS familia_empresa_nombre
            FROM Tablero
            INNER JOIN Familia_empresa ON Tablero.Familia_empresa_id = Familia_empresa.id
            WHERE Tablero.id = %s
        """, (tablero_id,))
        result = cursor.fetchone()
        connection.close()
        return result

    @staticmethod
    def create(tablero):
        connection = Database.get_connection()
        cursor = connection.cursor()
        sql = "INSERT INTO Tablero (nombre, descripcion, fecha_creacion, Familia_empresa_id) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (tablero.nombre, tablero.descripcion, tablero.fecha_creacion, tablero.familia_empresa_id))
        connection.commit()
        inserted_id = cursor.lastrowid
        connection.close()
        return inserted_id

    @staticmethod
    def update(tablero_id, tablero):
        connection = Database.get_connection()
        cursor = connection.cursor()
        sql = "UPDATE Tablero SET nombre=%s, descripcion=%s, fecha_creacion=%s, Familia_empresa_id=%s WHERE id=%s"
        cursor.execute(sql, (tablero.nombre, tablero.descripcion, tablero.fecha_creacion, tablero.familia_empresa_id, tablero_id))
        connection.commit()
        connection.close()

    @staticmethod
    def delete(tablero_id):
        connection = Database.get_connection()
        cursor = connection.cursor()
        sql = "DELETE FROM Tablero WHERE id=%s"
        cursor.execute(sql, (tablero_id,))
        connection.commit()
        connection.close()
