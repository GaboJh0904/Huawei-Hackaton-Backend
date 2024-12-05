from database.connection import Database

class ComentariosRepository:

    @staticmethod
    def get_all():
        connection = Database.get_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("""
            SELECT Comentarios.id, Comentarios.comentario, Comentarios.fecha_creacion,
                   Comentarios.Usuario_id AS usuario_id, Usuario.username, 
                   Comentarios.Tarea_id AS tarea_id, Tarea.nombre AS tarea_nombre
            FROM Comentarios
            INNER JOIN Usuario ON Comentarios.Usuario_id = Usuario.id
            INNER JOIN Tarea ON Comentarios.Tarea_id = Tarea.id
        """)
        results = cursor.fetchall()
        connection.close()
        return results

    @staticmethod
    def get_by_id(comentario_id):
        connection = Database.get_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("""
            SELECT Comentarios.id, Comentarios.comentario, Comentarios.fecha_creacion,
                   Comentarios.Usuario_id AS usuario_id, Usuario.username, 
                   Comentarios.Tarea_id AS tarea_id, Tarea.nombre AS tarea_nombre
            FROM Comentarios
            INNER JOIN Usuario ON Comentarios.Usuario_id = Usuario.id
            INNER JOIN Tarea ON Comentarios.Tarea_id = Tarea.id
            WHERE Comentarios.id = %s
        """, (comentario_id,))
        result = cursor.fetchone()
        connection.close()
        return result

    @staticmethod
    def create(comentario):
        connection = Database.get_connection()
        cursor = connection.cursor()
        sql = """
            INSERT INTO Comentarios (comentario, fecha_creacion, Usuario_id, Tarea_id)
            VALUES (%s, %s, %s, %s)
        """
        cursor.execute(sql, (comentario.comentario, comentario.fecha_creacion, comentario.usuario_id, comentario.tarea_id))
        connection.commit()
        inserted_id = cursor.lastrowid
        connection.close()
        return inserted_id

    @staticmethod
    def update(comentario_id, comentario):
        connection = Database.get_connection()
        cursor = connection.cursor()
        sql = """
            UPDATE Comentarios 
            SET comentario=%s, fecha_creacion=%s, Usuario_id=%s, Tarea_id=%s
            WHERE id=%s
        """
        cursor.execute(sql, (comentario.comentario, comentario.fecha_creacion, comentario.usuario_id, comentario.tarea_id, comentario_id))
        connection.commit()
        connection.close()

    @staticmethod
    def delete(comentario_id):
        connection = Database.get_connection()
        cursor = connection.cursor()
        sql = "DELETE FROM Comentarios WHERE id=%s"
        cursor.execute(sql, (comentario_id,))
        connection.commit()
        connection.close()
