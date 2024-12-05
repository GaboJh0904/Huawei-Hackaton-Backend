from database.connection import Database

class CategoriaRepository:

    @staticmethod
    def get_all():
        connection = Database.get_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Categoria")
        results = cursor.fetchall()
        connection.close()
        return results

    @staticmethod
    def get_by_id(categoria_id):
        connection = Database.get_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Categoria WHERE id = %s", (categoria_id,))
        result = cursor.fetchone()
        connection.close()
        return result

    @staticmethod
    def create(categoria):
        connection = Database.get_connection()
        cursor = connection.cursor()
        sql = "INSERT INTO Categoria (categoria) VALUES (%s)"
        cursor.execute(sql, (categoria.categoria,))
        connection.commit()
        inserted_id = cursor.lastrowid
        connection.close()
        return inserted_id

    @staticmethod
    def update(categoria_id, categoria):
        connection = Database.get_connection()
        cursor = connection.cursor()
        sql = "UPDATE Categoria SET categoria=%s WHERE id=%s"
        cursor.execute(sql, (categoria.categoria, categoria_id))
        connection.commit()
        connection.close()

    @staticmethod
    def delete(categoria_id):
        connection = Database.get_connection()
        cursor = connection.cursor()
        sql = "DELETE FROM Categoria WHERE id=%s"
        cursor.execute(sql, (categoria_id,))
        connection.commit()
        connection.close()
