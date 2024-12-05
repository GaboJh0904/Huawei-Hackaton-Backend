from pydantic import BaseModel

# Esquema para crear un nuevo miembro
class MiembrosCreate(BaseModel):
    usuario_id: int
    familia_empresa_id: int
    rol: str  # admin o miembro

# Esquema para leer información de un miembro (incluye username y nombre de Familia_empresa)
class MiembrosRead(BaseModel):
    id: int
    usuario_id: int
    username: str
    familia_empresa_id: int
    familia_empresa_nombre: str
    rol: str

    class Config:
        orm_mode = True

# Esquema para actualizar un miembro
class MiembrosUpdate(BaseModel):
    usuario_id: int | None = None
    familia_empresa_id: int | None = None
    rol: str | None = None
