from fastapi import APIRouter, HTTPException
from bl.tarea_bl import TareaBL
from schemas.tarea_schemas import TareaCreate, TareaRead, TareaUpdate

tarea_router = APIRouter()

@tarea_router.get("/", response_model=list[TareaRead])
def get_all_tareas():
    return TareaBL.get_all_tareas()

@tarea_router.get("/{tarea_id}", response_model=TareaRead)
def get_tarea_by_id(tarea_id: int):
    tarea = TareaBL.get_tarea_by_id(tarea_id)
    if not tarea:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return tarea

@tarea_router.post("/", response_model=int)
def create_tarea(tarea: TareaCreate):
    return TareaBL.create_tarea(tarea)

@tarea_router.put("/{tarea_id}")
def update_tarea(tarea_id: int, tarea: TareaUpdate):
    TareaBL.update_tarea(tarea_id, tarea)
    return {"message": "Tarea actualizada con éxito"}

@tarea_router.delete("/{tarea_id}")
def delete_tarea(tarea_id: int):
    TareaBL.delete_tarea(tarea_id)
    return {"message": "Tarea eliminada con éxito"}
