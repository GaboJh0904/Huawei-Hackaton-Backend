from fastapi import APIRouter, HTTPException
from bl.miembros_bl import MiembrosBL
from schemas.miembros_schemas import MiembrosCreate, MiembrosRead, MiembrosUpdate

miembros_router = APIRouter()

@miembros_router.get("/", response_model=list[MiembrosRead])
def get_all_miembros():
    return MiembrosBL.get_all_miembros()

@miembros_router.get("/{miembro_id}", response_model=MiembrosRead)
def get_miembro_by_id(miembro_id: int):
    miembro = MiembrosBL.get_miembro_by_id(miembro_id)
    if not miembro:
        raise HTTPException(status_code=404, detail="Miembro no encontrado")
    return miembro

@miembros_router.post("/", response_model=int)
def create_miembro(miembro: MiembrosCreate):
    return MiembrosBL.create_miembro(miembro)

@miembros_router.put("/{miembro_id}")
def update_miembro(miembro_id: int, miembro: MiembrosUpdate):
    MiembrosBL.update_miembro(miembro_id, miembro)
    return {"message": "Miembro actualizado con éxito"}

@miembros_router.delete("/{miembro_id}")
def delete_miembro(miembro_id: int):
    MiembrosBL.delete_miembro(miembro_id)
    return {"message": "Miembro eliminado con éxito"}
