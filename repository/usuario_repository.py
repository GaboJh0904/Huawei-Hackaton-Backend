import bcrypt
from database.connection import Database

class UsuarioRepository:

    @staticmethod
    def hash_password(password: str) -> str:
        """Cifra la contraseña usando bcrypt."""
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed.decode('utf-8')

    @staticmethod
    def verify_password(password: str, hashed_password: str) -> bool:
        """Verifica si una contraseña coincide con su hash."""
        return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))

    @staticmethod
    def get_all():
        connection = Database.get_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("""
            SELECT Usuario.id, Usuario.username, 
                   CONCAT(Persona.nombre, " ", Persona.email) AS nombre_completo
            FROM Usuario
            INNER JOIN Persona ON Usuario.Persona_id = Persona.id
        """)
        results = cursor.fetchall()
        connection.close()
        return results

    @staticmethod
    def get_by_id(usuario_id):
        connection = Database.get_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("""
            SELECT Usuario.id, Usuario.username, 
                   CONCAT(Persona.nombre, " ", Persona.email) AS nombre_completo
            FROM Usuario
            INNER JOIN Persona ON Usuario.Persona_id = Persona.id
            WHERE Usuario.id = %s
        """, (usuario_id,))
        result = cursor.fetchone()
        connection.close()
        return result

    @staticmethod
    def create(usuario):
        connection = Database.get_connection()
        cursor = connection.cursor()
        hashed_password = UsuarioRepository.hash_password(usuario.password)
        sql = "INSERT INTO Usuario (username, password, Persona_id) VALUES (%s, %s, %s)"
        cursor.execute(sql, (usuario.username, hashed_password, usuario.persona_id))
        connection.commit()
        inserted_id = cursor.lastrowid
        connection.close()
        return inserted_id

    @staticmethod
    def update(usuario_id, usuario):
        connection = Database.get_connection()
        cursor = connection.cursor()
        updates = []
        values = []

        if usuario.username is not None:
            updates.append("username=%s")
            values.append(usuario.username)

        if usuario.password is not None:
            hashed_password = UsuarioRepository.hash_password(usuario.password)
            updates.append("password=%s")
            values.append(hashed_password)

        values.append(usuario_id)
        sql = f"UPDATE Usuario SET {', '.join(updates)} WHERE id=%s"
        cursor.execute(sql, values)
        connection.commit()
        connection.close()

    @staticmethod
    def delete(usuario_id):
        connection = Database.get_connection()
        cursor = connection.cursor()
        sql = "DELETE FROM Usuario WHERE id=%s"
        cursor.execute(sql, (usuario_id,))
        connection.commit()
        connection.close()

    @staticmethod
    def get_user_by_username(username: str):
        connection = Database.get_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Usuario WHERE username = %s", (username,))
        result = cursor.fetchone()
        connection.close()
        return result
