from repository.comentarios_repository import ComentariosRepository

class ComentariosBL:

    @staticmethod
    def get_all_comentarios():
        return ComentariosRepository.get_all()

    @staticmethod
    def get_comentario_by_id(comentario_id):
        return ComentariosRepository.get_by_id(comentario_id)

    @staticmethod
    def create_comentario(comentario):
        return ComentariosRepository.create(comentario)

    @staticmethod
    def update_comentario(comentario_id, comentario):
        ComentariosRepository.update(comentario_id, comentario)

    @staticmethod
    def delete_comentario(comentario_id):
        ComentariosRepository.delete(comentario_id)
