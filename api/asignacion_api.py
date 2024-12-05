from fastapi import APIRouter, HTTPException
from bl.asignacion_bl import AsignacionBL
from schemas.asignacion_schemas import AsignacionCreate, AsignacionRead, AsignacionUpdate

asignacion_router = APIRouter()

@asignacion_router.get("/", response_model=list[AsignacionRead])
def get_all_asignaciones():
    return AsignacionBL.get_all_asignaciones()

@asignacion_router.get("/{asignacion_id}", response_model=AsignacionRead)
def get_asignacion_by_id(asignacion_id: int):
    asignacion = AsignacionBL.get_asignacion_by_id(asignacion_id)
    if not asignacion:
        raise HTTPException(status_code=404, detail="Asignación no encontrada")
    return asignacion

@asignacion_router.post("/", response_model=int)
def create_asignacion(asignacion: AsignacionCreate):
    return AsignacionBL.create_asignacion(asignacion)

@asignacion_router.put("/{asignacion_id}")
def update_asignacion(asignacion_id: int, asignacion: AsignacionUpdate):
    AsignacionBL.update_asignacion(asignacion_id, asignacion)
    return {"message": "Asignación actualizada con éxito"}

@asignacion_router.delete("/{asignacion_id}")
def delete_asignacion(asignacion_id: int):
    AsignacionBL.delete_asignacion(asignacion_id)
    return {"message": "Asignación eliminada con éxito"}
