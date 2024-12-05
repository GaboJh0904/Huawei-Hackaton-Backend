from pydantic import BaseModel

# Esquema para crear una nueva categoría
class CategoriaCreate(BaseModel):
    categoria: str

# Esquema para leer información de una categoría
class CategoriaRead(BaseModel):
    id: int
    categoria: str

    class Config:
        orm_mode = True

# Esquema para actualizar una categoría
class CategoriaUpdate(BaseModel):
    categoria: str | None = None
