from pydantic import BaseModel
from datetime import date

# Esquema para crear un nuevo tablero
class TableroCreate(BaseModel):
    nombre: str
    descripcion: str
    fecha_creacion: date
    familia_empresa_id: int

# Esquema para leer información de un tablero (incluye Familia_empresa_id y nombre)
class TableroRead(BaseModel):
    id: int
    nombre: str
    descripcion: str
    fecha_creacion: date
    familia_empresa_id: int
    familia_empresa_nombre: str

    class Config:
        orm_mode = True

# Esquema para actualizar un tablero
class TableroUpdate(BaseModel):
    nombre: str | None = None
    descripcion: str | None = None
    fecha_creacion: date | None = None
    familia_empresa_id: int | None = None
