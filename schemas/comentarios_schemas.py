from pydantic import BaseModel
from datetime import date

# Esquema para crear un nuevo comentario
class ComentariosCreate(BaseModel):
    comentario: str
    fecha_creacion: date
    usuario_id: int
    tarea_id: int

# Esquema para leer información de un comentario (incluye username y nombre de Tarea)
class ComentariosRead(BaseModel):
    id: int
    comentario: str
    fecha_creacion: date
    usuario_id: int
    username: str
    tarea_id: int
    tarea_nombre: str

    class Config:
        orm_mode = True

# Esquema para actualizar un comentario
class ComentariosUpdate(BaseModel):
    comentario: str | None = None
    fecha_creacion: date | None = None
    usuario_id: int | None = None
    tarea_id: int | None = None
