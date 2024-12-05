from fastapi import APIRouter, HTTPException
from bl.tablero_bl import TableroBL
from schemas.tablero_schemas import TableroCreate, TableroRead, TableroUpdate

tablero_router = APIRouter()

@tablero_router.get("/", response_model=list[TableroRead])
def get_all_tableros():
    return TableroBL.get_all_tableros()

@tablero_router.get("/{tablero_id}", response_model=TableroRead)
def get_tablero_by_id(tablero_id: int):
    tablero = TableroBL.get_tablero_by_id(tablero_id)
    if not tablero:
        raise HTTPException(status_code=404, detail="Tablero no encontrado")
    return tablero

@tablero_router.post("/", response_model=int)
def create_tablero(tablero: TableroCreate):
    return TableroBL.create_tablero(tablero)

@tablero_router.put("/{tablero_id}")
def update_tablero(tablero_id: int, tablero: TableroUpdate):
    TableroBL.update_tablero(tablero_id, tablero)
    return {"message": "Tablero actualizado con éxito"}

@tablero_router.delete("/{tablero_id}")
def delete_tablero(tablero_id: int):
    TableroBL.delete_tablero(tablero_id)
    return {"message": "Tablero eliminado con éxito"}
