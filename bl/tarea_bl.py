from repository.tarea_repository import TareaRepository

class TareaBL:

    @staticmethod
    def get_all_tareas():
        return TareaRepository.get_all()

    @staticmethod
    def get_tarea_by_id(tarea_id):
        return TareaRepository.get_by_id(tarea_id)

    @staticmethod
    def create_tarea(tarea):
        return TareaRepository.create(tarea)

    @staticmethod
    def update_tarea(tarea_id, tarea):
        TareaRepository.update(tarea_id, tarea)

    @staticmethod
    def delete_tarea(tarea_id):
        TareaRepository.delete(tarea_id)
