from repository.asignacion_repository import AsignacionRepository

class AsignacionBL:

    @staticmethod
    def get_all_asignaciones():
        return AsignacionRepository.get_all()

    @staticmethod
    def get_asignacion_by_id(asignacion_id):
        return AsignacionRepository.get_by_id(asignacion_id)

    @staticmethod
    def create_asignacion(asignacion):
        return AsignacionRepository.create(asignacion)

    @staticmethod
    def update_asignacion(asignacion_id, asignacion):
        AsignacionRepository.update(asignacion_id, asignacion)

    @staticmethod
    def delete_asignacion(asignacion_id):
        AsignacionRepository.delete(asignacion_id)
