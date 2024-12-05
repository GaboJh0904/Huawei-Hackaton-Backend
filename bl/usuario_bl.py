from repository.usuario_repository import UsuarioRepository

class UsuarioBL:

    @staticmethod
    def get_all_usuarios():
        return UsuarioRepository.get_all()

    @staticmethod
    def get_usuario_by_id(usuario_id):
        return UsuarioRepository.get_by_id(usuario_id)

    @staticmethod
    def get_usuario_by_username(username):
        return UsuarioRepository.get_by_username(username)

    @staticmethod
    def create_usuario(usuario):
        return UsuarioRepository.create(usuario)

    @staticmethod
    def update_usuario(usuario_id, usuario):
        UsuarioRepository.update(usuario_id, usuario)

    @staticmethod
    def delete_usuario(usuario_id):
        UsuarioRepository.delete(usuario_id)
