from database.connection import Database

class PersonaRepository:

    @staticmethod
    def get_all():
        connection = Database.get_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Persona")
        results = cursor.fetchall()
        connection.close()
        return results

    @staticmethod
    def create(persona):
        connection = Database.get_connection()
        cursor = connection.cursor()
        sql = "INSERT INTO Persona (nombre, email, telefono, fecha_nacimiento) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (persona.nombre, persona.email, persona.telefono, persona.fecha_nacimiento))
        connection.commit()
        inserted_id = cursor.lastrowid
        connection.close()
        return inserted_id

    @staticmethod
    def update(persona_id, persona):
        connection = Database.get_connection()
        cursor = connection.cursor()
        sql = "UPDATE Persona SET nombre=%s, email=%s, telefono=%s, fecha_nacimiento=%s WHERE id=%s"
        cursor.execute(sql, (persona.nombre, persona.email, persona.telefono, persona.fecha_nacimiento, persona_id))
        connection.commit()
        connection.close()

    @staticmethod
    def delete(persona_id):
        connection = Database.get_connection()
        cursor = connection.cursor()
        sql = "DELETE FROM Persona WHERE id=%s"
        cursor.execute(sql, (persona_id,))
        connection.commit()
        connection.close()
