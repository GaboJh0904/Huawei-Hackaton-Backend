from repository.miembros_repository import MiembrosRepository

class MiembrosBL:

    @staticmethod
    def get_all_miembros():
        return MiembrosRepository.get_all()

    @staticmethod
    def get_miembro_by_id(miembro_id):
        return MiembrosRepository.get_by_id(miembro_id)

    @staticmethod
    def create_miembro(miembro):
        return MiembrosRepository.create(miembro)

    @staticmethod
    def update_miembro(miembro_id, miembro):
        MiembrosRepository.update(miembro_id, miembro)

    @staticmethod
    def delete_miembro(miembro_id):
        MiembrosRepository.delete(miembro_id)
