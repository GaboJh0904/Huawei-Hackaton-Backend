from pydantic import BaseModel
from datetime import date

# Esquema para crear una nueva familia/empresa
class FamiliaEmpresaCreate(BaseModel):
    nombre: str
    detalle: str
    fecha_creacion: date

# Esquema para leer información de una familia/empresa
class FamiliaEmpresaRead(BaseModel):
    id: int
    nombre: str
    detalle: str
    fecha_creacion: date

    class Config:
        orm_mode = True

# Esquema para actualizar una familia/empresa
class FamiliaEmpresaUpdate(BaseModel):
    nombre: str | None = None
    detalle: str | None = None
    fecha_creacion: date | None = None
