from pydantic import BaseModel
from datetime import date

# Esquema para crear una nueva persona
class PersonaCreate(BaseModel):
    nombre: str
    email: str
    telefono: str
    fecha_nacimiento: date

# Esquema para leer información de una persona
class PersonaRead(BaseModel):
    id: int
    nombre: str
    email: str
    telefono: str
    fecha_nacimiento: date

    class Config:
        orm_mode = True

# Esquema para actualizar una persona
class PersonaUpdate(BaseModel):
    nombre: str | None = None
    email: str | None = None
    telefono: str | None = None
    fecha_nacimiento: date | None = None
