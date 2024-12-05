from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from security.jwt_handler import create_access_token
from repository.usuario_repository import UsuarioRepository

auth_router = APIRouter()


class LoginRequest(BaseModel):
    username: str
    password: str


class LoginResponse(BaseModel):
    access_token: str
    token_type: str = "Bearer"


@auth_router.post("/login", response_model=LoginResponse)
def login(login_request: LoginRequest):
    """Autenticación de usuario y generación de JWT."""
    usuario = UsuarioRepository.get_user_by_username(login_request.username)

    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    if not UsuarioRepository.verify_password(login_request.password, usuario["password"]):
        raise HTTPException(status_code=401, detail="Credenciales incorrectas")

    # Crear el token JWT
    access_token = create_access_token(data={"sub": usuario["username"], "id": usuario["id"]})
    return {"access_token": access_token, "token_type": "Bearer"}
