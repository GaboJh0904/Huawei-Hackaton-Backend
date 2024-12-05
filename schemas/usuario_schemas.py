from pydantic import BaseModel

# Esquema para crear un nuevo usuario
class UsuarioCreate(BaseModel):
    username: str
    password: str
    persona_id: int

# Esquema para leer información de un usuario
class UsuarioRead(BaseModel):
    id: int
    username: str
    nombre_completo: str

    class Config:
        orm_mode = True

# Esquema para actualizar un usuario (la contraseña no es obligatoria)
class UsuarioUpdate(BaseModel):
    username: str | None = None
    password: str | None = None
