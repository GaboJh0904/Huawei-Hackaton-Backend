from fastapi import APIRouter, HTTPException
from bl.persona_bl import PersonaBL
from schemas.persona_schemas import PersonaCreate, PersonaRead, PersonaUpdate

persona_router = APIRouter()

@persona_router.get("/", response_model=list[PersonaRead])
def get_all_personas():
    return PersonaBL.get_all_personas()

@persona_router.post("/", response_model=int)
def create_persona(persona: PersonaCreate):
    return PersonaBL.create_persona(persona)

@persona_router.put("/{persona_id}")
def update_persona(persona_id: int, persona: PersonaUpdate):
    PersonaBL.update_persona(persona_id, persona)
    return {"message": "Persona actualizada con éxito"}

@persona_router.delete("/{persona_id}")
def delete_persona(persona_id: int):
    PersonaBL.delete_persona(persona_id)
    return {"message": "Persona eliminada con éxito"}
