from fastapi import APIRouter, HTTPException
from bl.usuario_bl import UsuarioBL
from schemas.usuario_schemas import UsuarioCreate, UsuarioRead, UsuarioUpdate

usuario_router = APIRouter()

@usuario_router.get("/", response_model=list[UsuarioRead])
def get_all_usuarios():
    return UsuarioBL.get_all_usuarios()

@usuario_router.get("/{usuario_id}", response_model=UsuarioRead)
def get_usuario_by_id(usuario_id: int):
    usuario = UsuarioBL.get_usuario_by_id(usuario_id)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario

@usuario_router.post("/", response_model=int)
def create_usuario(usuario: UsuarioCreate):
    return UsuarioBL.create_usuario(usuario)

@usuario_router.put("/{usuario_id}")
def update_usuario(usuario_id: int, usuario: UsuarioUpdate):
    UsuarioBL.update_usuario(usuario_id, usuario)
    return {"message": "Usuario actualizado con éxito"}

@usuario_router.delete("/{usuario_id}")
def delete_usuario(usuario_id: int):
    UsuarioBL.delete_usuario(usuario_id)
    return {"message": "Usuario eliminado con éxito"}
