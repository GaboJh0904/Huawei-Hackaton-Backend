from fastapi import APIRouter, HTTPException
from bl.comentarios_bl import ComentariosBL
from schemas.comentarios_schemas import ComentariosCreate, ComentariosRead, ComentariosUpdate

comentarios_router = APIRouter()

@comentarios_router.get("/", response_model=list[ComentariosRead])
def get_all_comentarios():
    return ComentariosBL.get_all_comentarios()

@comentarios_router.get("/{comentario_id}", response_model=ComentariosRead)
def get_comentario_by_id(comentario_id: int):
    comentario = ComentariosBL.get_comentario_by_id(comentario_id)
    if not comentario:
        raise HTTPException(status_code=404, detail="Comentario no encontrado")
    return comentario

@comentarios_router.post("/", response_model=int)
def create_comentario(comentario: ComentariosCreate):
    return ComentariosBL.create_comentario(comentario)

@comentarios_router.put("/{comentario_id}")
def update_comentario(comentario_id: int, comentario: ComentariosUpdate):
    ComentariosBL.update_comentario(comentario_id, comentario)
    return {"message": "Comentario actualizado con éxito"}

@comentarios_router.delete("/{comentario_id}")
def delete_comentario(comentario_id: int):
    ComentariosBL.delete_comentario(comentario_id)
    return {"message": "Comentario eliminado con éxito"}
