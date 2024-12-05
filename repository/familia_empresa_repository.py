from database.connection import Database

class FamiliaEmpresaRepository:

    @staticmethod
    def get_all():
        connection = Database.get_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Familia_empresa")
        results = cursor.fetchall()
        connection.close()
        return results

    @staticmethod
    def get_by_id(familia_empresa_id):
        connection = Database.get_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Familia_empresa WHERE id = %s", (familia_empresa_id,))
        result = cursor.fetchone()
        connection.close()
        return result

    @staticmethod
    def create(familia_empresa):
        connection = Database.get_connection()
        cursor = connection.cursor()
        sql = "INSERT INTO Familia_empresa (nombre, detalle, fecha_creacion) VALUES (%s, %s, %s)"
        cursor.execute(sql, (familia_empresa.nombre, familia_empresa.detalle, familia_empresa.fecha_creacion))
        connection.commit()
        inserted_id = cursor.lastrowid
        connection.close()
        return inserted_id

    @staticmethod
    def update(familia_empresa_id, familia_empresa):
        connection = Database.get_connection()
        cursor = connection.cursor()
        sql = "UPDATE Familia_empresa SET nombre=%s, detalle=%s, fecha_creacion=%s WHERE id=%s"
        cursor.execute(sql, (familia_empresa.nombre, familia_empresa.detalle, familia_empresa.fecha_creacion, familia_empresa_id))
        connection.commit()
        connection.close()

    @staticmethod
    def delete(familia_empresa_id):
        connection = Database.get_connection()
        cursor = connection.cursor()
        sql = "DELETE FROM Familia_empresa WHERE id=%s"
        cursor.execute(sql, (familia_empresa_id,))
        connection.commit()
        connection.close()
