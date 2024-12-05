from fastapi import FastAPI
from api.persona_api import persona_router
from api.usuario_api import usuario_router
from api.familia_empresa_api import familia_empresa_router
from api.tablero_api import tablero_router
from api.tarea_api import tarea_router
from api.asignacion_api import asignacion_router
from api.comentarios_api import comentarios_router
from api.miembros_api import miembros_router
from api.categoria_api import categoria_router

from api.auth_api import auth_router









app = FastAPI()

# Registrar rutas
app.include_router(persona_router, prefix="/personas", tags=["Personas"])
app.include_router(usuario_router, prefix="/usuarios", tags=["Usuarios"])
app.include_router(familia_empresa_router, prefix="/familias_empresas", tags=["Familias/Empresas"])
app.include_router(tablero_router, prefix="/tableros", tags=["Tableros"])
app.include_router(tarea_router, prefix="/tareas", tags=["Tareas"])
app.include_router(asignacion_router, prefix="/asignaciones", tags=["Asignaciones"])
app.include_router(comentarios_router, prefix="/comentarios", tags=["Comentarios"])
app.include_router(miembros_router, prefix="/miembros", tags=["Miembros"])
app.include_router(categoria_router, prefix="/categorias", tags=["Categorías"])
app.include_router(auth_router, prefix="/auth", tags=["Autenticación"])

@app.get("/")
def read_root():
    return {"message": "Bienvenido al Gestor de Tareas"}
