from fastapi import APIRouter, HTTPException
from bl.categoria_bl import CategoriaBL
from schemas.categoria_schemas import CategoriaCreate, CategoriaRead, CategoriaUpdate

categoria_router = APIRouter()

@categoria_router.get("/", response_model=list[CategoriaRead])
def get_all_categorias():
    return CategoriaBL.get_all_categorias()

@categoria_router.get("/{categoria_id}", response_model=CategoriaRead)
def get_categoria_by_id(categoria_id: int):
    categoria = CategoriaBL.get_categoria_by_id(categoria_id)
    if not categoria:
        raise HTTPException(status_code=404, detail="Categoría no encontrada")
    return categoria

@categoria_router.post("/", response_model=int)
def create_categoria(categoria: CategoriaCreate):
    return CategoriaBL.create_categoria(categoria)

@categoria_router.put("/{categoria_id}")
def update_categoria(categoria_id: int, categoria: CategoriaUpdate):
    CategoriaBL.update_categoria(categoria_id, categoria)
    return {"message": "Categoría actualizada con éxito"}

@categoria_router.delete("/{categoria_id}")
def delete_categoria(categoria_id: int):
    CategoriaBL.delete_categoria(categoria_id)
    return {"message": "Categoría eliminada con éxito"}
