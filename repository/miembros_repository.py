from database.connection import Database

class MiembrosRepository:

    @staticmethod
    def get_all():
        connection = Database.get_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("""
            SELECT Miembros.id, Miembros.Usuario_id AS usuario_id, Usuario.username, 
                   Miembros.Familia_empresa_id AS familia_empresa_id, Familia_empresa.nombre AS familia_empresa_nombre,
                   Miembros.rol
            FROM Miembros
            INNER JOIN Usuario ON Miembros.Usuario_id = Usuario.id
            INNER JOIN Familia_empresa ON Miembros.Familia_empresa_id = Familia_empresa.id
        """)
        results = cursor.fetchall()
        connection.close()
        return results

    @staticmethod
    def get_by_id(miembro_id):
        connection = Database.get_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("""
            SELECT Miembros.id, Miembros.Usuario_id AS usuario_id, Usuario.username, 
                   Miembros.Familia_empresa_id AS familia_empresa_id, Familia_empresa.nombre AS familia_empresa_nombre,
                   Miembros.rol
            FROM Miembros
            INNER JOIN Usuario ON Miembros.Usuario_id = Usuario.id
            INNER JOIN Familia_empresa ON Miembros.Familia_empresa_id = Familia_empresa.id
            WHERE Miembros.id = %s
        """, (miembro_id,))
        result = cursor.fetchone()
        connection.close()
        return result

    @staticmethod
    def create(miembro):
        connection = Database.get_connection()
        cursor = connection.cursor()
        sql = """
            INSERT INTO Miembros (Usuario_id, Familia_empresa_id, rol)
            VALUES (%s, %s, %s)
        """
        cursor.execute(sql, (miembro.usuario_id, miembro.familia_empresa_id, miembro.rol))
        connection.commit()
        inserted_id = cursor.lastrowid
        connection.close()
        return inserted_id

    @staticmethod
    def update(miembro_id, miembro):
        connection = Database.get_connection()
        cursor = connection.cursor()
        sql = """
            UPDATE Miembros 
            SET Usuario_id=%s, Familia_empresa_id=%s, rol=%s
            WHERE id=%s
        """
        cursor.execute(sql, (miembro.usuario_id, miembro.familia_empresa_id, miembro.rol, miembro_id))
        connection.commit()
        connection.close()

    @staticmethod
    def delete(miembro_id):
        connection = Database.get_connection()
        cursor = connection.cursor()
        sql = "DELETE FROM Miembros WHERE id=%s"
        cursor.execute(sql, (miembro_id,))
        connection.commit()
        connection.close()
