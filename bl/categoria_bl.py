from repository.categoria_repository import CategoriaRepository

class CategoriaBL:

    @staticmethod
    def get_all_categorias():
        return CategoriaRepository.get_all()

    @staticmethod
    def get_categoria_by_id(categoria_id):
        return CategoriaRepository.get_by_id(categoria_id)

    @staticmethod
    def create_categoria(categoria):
        return CategoriaRepository.create(categoria)

    @staticmethod
    def update_categoria(categoria_id, categoria):
        CategoriaRepository.update(categoria_id, categoria)

    @staticmethod
    def delete_categoria(categoria_id):
        CategoriaRepository.delete(categoria_id)
