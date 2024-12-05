from repository.familia_empresa_repository import FamiliaEmpresaRepository

class FamiliaEmpresaBL:

    @staticmethod
    def get_all_familias_empresas():
        return FamiliaEmpresaRepository.get_all()

    @staticmethod
    def get_familia_empresa_by_id(familia_empresa_id):
        return FamiliaEmpresaRepository.get_by_id(familia_empresa_id)

    @staticmethod
    def create_familia_empresa(familia_empresa):
        return FamiliaEmpresaRepository.create(familia_empresa)

    @staticmethod
    def update_familia_empresa(familia_empresa_id, familia_empresa):
        FamiliaEmpresaRepository.update(familia_empresa_id, familia_empresa)

    @staticmethod
    def delete_familia_empresa(familia_empresa_id):
        FamiliaEmpresaRepository.delete(familia_empresa_id)
