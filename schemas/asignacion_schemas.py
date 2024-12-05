from pydantic import BaseModel
from datetime import date

# Esquema para crear una nueva asignación
class AsignacionCreate(BaseModel):
    fecha_asignacion: date
    usuario_id: int
    tarea_id: int

# Esquema para leer información de una asignación (incluye username y nombre de Tarea)
class AsignacionRead(BaseModel):
    id: int
    fecha_asignacion: date
    usuario_id: int
    username: str
    tarea_id: int
    tarea_nombre: str

    class Config:
        orm_mode = True

# Esquema para actualizar una asignación
class AsignacionUpdate(BaseModel):
    fecha_asignacion: date | None = None
    usuario_id: int | None = None
    tarea_id: int | None = None
