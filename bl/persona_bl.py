from repository.persona_repository import PersonaRepository

class PersonaBL:

    @staticmethod
    def get_all_personas():
        return PersonaRepository.get_all()

    @staticmethod
    def create_persona(persona):
        return PersonaRepository.create(persona)

    @staticmethod
    def update_persona(persona_id, persona):
        PersonaRepository.update(persona_id, persona)

    @staticmethod
    def delete_persona(persona_id):
        PersonaRepository.delete(persona_id)
