from pydantic import BaseModel
from datetime import date

# Esquema para crear una nueva tarea
class TareaCreate(BaseModel):
    nombre: str
    descripcion: str
    estado: str  # pendiente, en_progreso, completada
    prioridad: str  # alta, media, baja
    fecha_creacion: date
    fecha_fin: date
    tablero_id: int
    categoria_id: int

# Esquema para leer información de una tarea (incluye nombres de Tablero y Categoria)
class TareaRead(BaseModel):
    id: int
    nombre: str
    descripcion: str
    estado: str
    prioridad: str
    fecha_creacion: date
    fecha_fin: date
    tablero_id: int
    tablero_nombre: str
    categoria_id: int
    categoria_nombre: str

    class Config:
        orm_mode = True

# Esquema para actualizar una tarea
class TareaUpdate(BaseModel):
    nombre: str | None = None
    descripcion: str | None = None
    estado: str | None = None
    prioridad: str | None = None
    fecha_creacion: date | None = None
    fecha_fin: date | None = None
    tablero_id: int | None = None
    categoria_id: int | None = None
