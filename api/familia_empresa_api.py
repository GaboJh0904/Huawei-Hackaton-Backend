from fastapi import APIRouter, HTTPException
from bl.familia_empresa_bl import FamiliaEmpresaBL
from schemas.familia_empresa_schemas import FamiliaEmpresaCreate, FamiliaEmpresaRead, FamiliaEmpresaUpdate

familia_empresa_router = APIRouter()

@familia_empresa_router.get("/", response_model=list[FamiliaEmpresaRead])
def get_all_familias_empresas():
    return FamiliaEmpresaBL.get_all_familias_empresas()

@familia_empresa_router.get("/{familia_empresa_id}", response_model=FamiliaEmpresaRead)
def get_familia_empresa_by_id(familia_empresa_id: int):
    familia_empresa = FamiliaEmpresaBL.get_familia_empresa_by_id(familia_empresa_id)
    if not familia_empresa:
        raise HTTPException(status_code=404, detail="Familia/Empresa no encontrada")
    return familia_empresa

@familia_empresa_router.post("/", response_model=int)
def create_familia_empresa(familia_empresa: FamiliaEmpresaCreate):
    return FamiliaEmpresaBL.create_familia_empresa(familia_empresa)

@familia_empresa_router.put("/{familia_empresa_id}")
def update_familia_empresa(familia_empresa_id: int, familia_empresa: FamiliaEmpresaUpdate):
    FamiliaEmpresaBL.update_familia_empresa(familia_empresa_id, familia_empresa)
    return {"message": "Familia/Empresa actualizada con éxito"}

@familia_empresa_router.delete("/{familia_empresa_id}")
def delete_familia_empresa(familia_empresa_id: int):
    FamiliaEmpresaBL.delete_familia_empresa(familia_empresa_id)
    return {"message": "Familia/Empresa eliminada con éxito"}
