from database.connection import Database

class AsignacionRepository:

    @staticmethod
    def get_all():
        connection = Database.get_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("""
            SELECT Asignacion.id, Asignacion.fecha_asignacion, 
                   Asignacion.Usuario_id AS usuario_id, Usuario.username, 
                   Asignacion.Tarea_id AS tarea_id, Tarea.nombre AS tarea_nombre
            FROM Asignacion
            INNER JOIN Usuario ON Asignacion.Usuario_id = Usuario.id
            INNER JOIN Tarea ON Asignacion.Tarea_id = Tarea.id
        """)
        results = cursor.fetchall()
        connection.close()
        return results

    @staticmethod
    def get_by_id(asignacion_id):
        connection = Database.get_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("""
            SELECT Asignacion.id, Asignacion.fecha_asignacion, 
                   Asignacion.Usuario_id AS usuario_id, Usuario.username, 
                   Asignacion.Tarea_id AS tarea_id, Tarea.nombre AS tarea_nombre
            FROM Asignacion
            INNER JOIN Usuario ON Asignacion.Usuario_id = Usuario.id
            INNER JOIN Tarea ON Asignacion.Tarea_id = Tarea.id
            WHERE Asignacion.id = %s
        """, (asignacion_id,))
        result = cursor.fetchone()
        connection.close()
        return result

    @staticmethod
    def create(asignacion):
        connection = Database.get_connection()
        cursor = connection.cursor()
        sql = """
            INSERT INTO Asignacion (fecha_asignacion, Usuario_id, Tarea_id)
            VALUES (%s, %s, %s)
        """
        cursor.execute(sql, (asignacion.fecha_asignacion, asignacion.usuario_id, asignacion.tarea_id))
        connection.commit()
        inserted_id = cursor.lastrowid
        connection.close()
        return inserted_id

    @staticmethod
    def update(asignacion_id, asignacion):
        connection = Database.get_connection()
        cursor = connection.cursor()
        sql = """
            UPDATE Asignacion 
            SET fecha_asignacion=%s, Usuario_id=%s, Tarea_id=%s
            WHERE id=%s
        """
        cursor.execute(sql, (asignacion.fecha_asignacion, asignacion.usuario_id, asignacion.tarea_id, asignacion_id))
        connection.commit()
        connection.close()

    @staticmethod
    def delete(asignacion_id):
        connection = Database.get_connection()
        cursor = connection.cursor()
        sql = "DELETE FROM Asignacion WHERE id=%s"
        cursor.execute(sql, (asignacion_id,))
        connection.commit()
        connection.close()
