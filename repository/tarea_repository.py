from database.connection import Database

class TareaRepository:

    @staticmethod
    def get_all():
        connection = Database.get_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("""
            SELECT Tarea.id, Tarea.nombre, Tarea.descripcion, Tarea.estado, Tarea.prioridad, 
                   Tarea.fecha_creacion, Tarea.fecha_fin, 
                   Tarea.Tablero_id AS tablero_id, Tablero.nombre AS tablero_nombre, 
                   Tarea.Categoria_id AS categoria_id, Categoria.categoria AS categoria_nombre
            FROM Tarea
            INNER JOIN Tablero ON Tarea.Tablero_id = Tablero.id
            INNER JOIN Categoria ON Tarea.Categoria_id = Categoria.id
        """)
        results = cursor.fetchall()
        connection.close()
        return results

    @staticmethod
    def get_by_id(tarea_id):
        connection = Database.get_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("""
            SELECT Tarea.id, Tarea.nombre, Tarea.descripcion, Tarea.estado, Tarea.prioridad, 
                   Tarea.fecha_creacion, Tarea.fecha_fin, 
                   Tarea.Tablero_id AS tablero_id, Tablero.nombre AS tablero_nombre, 
                   Tarea.Categoria_id AS categoria_id, Categoria.categoria AS categoria_nombre
            FROM Tarea
            INNER JOIN Tablero ON Tarea.Tablero_id = Tablero.id
            INNER JOIN Categoria ON Tarea.Categoria_id = Categoria.id
            WHERE Tarea.id = %s
        """, (tarea_id,))
        result = cursor.fetchone()
        connection.close()
        return result

    @staticmethod
    def create(tarea):
        connection = Database.get_connection()
        cursor = connection.cursor()
        sql = """
            INSERT INTO Tarea (nombre, descripcion, estado, prioridad, fecha_creacion, 
                               fecha_fin, Tablero_id, Categoria_id)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(sql, (
            tarea.nombre, tarea.descripcion, tarea.estado, tarea.prioridad,
            tarea.fecha_creacion, tarea.fecha_fin, tarea.tablero_id, tarea.categoria_id
        ))
        connection.commit()
        inserted_id = cursor.lastrowid
        connection.close()
        return inserted_id

    @staticmethod
    def update(tarea_id, tarea):
        connection = Database.get_connection()
        cursor = connection.cursor()
        sql = """
            UPDATE Tarea 
            SET nombre=%s, descripcion=%s, estado=%s, prioridad=%s, 
                fecha_creacion=%s, fecha_fin=%s, Tablero_id=%s, Categoria_id=%s
            WHERE id=%s
        """
        cursor.execute(sql, (
            tarea.nombre, tarea.descripcion, tarea.estado, tarea.prioridad,
            tarea.fecha_creacion, tarea.fecha_fin, tarea.tablero_id, tarea.categoria_id, tarea_id
        ))
        connection.commit()
        connection.close()

    @staticmethod
    def delete(tarea_id):
        connection = Database.get_connection()
        cursor = connection.cursor()
        sql = "DELETE FROM Tarea WHERE id=%s"
        cursor.execute(sql, (tarea_id,))
        connection.commit()
        connection.close()
