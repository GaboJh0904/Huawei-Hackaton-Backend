from repository.tablero_repository import TableroRepository

class TableroBL:

    @staticmethod
    def get_all_tableros():
        return TableroRepository.get_all()

    @staticmethod
    def get_tablero_by_id(tablero_id):
        return TableroRepository.get_by_id(tablero_id)

    @staticmethod
    def create_tablero(tablero):
        return TableroRepository.create(tablero)

    @staticmethod
    def update_tablero(tablero_id, tablero):
        TableroRepository.update(tablero_id, tablero)

    @staticmethod
    def delete_tablero(tablero_id):
        TableroRepository.delete(tablero_id)
