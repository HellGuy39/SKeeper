from data.mapper.SpecialtyMapper import specialty_to_specialty_entity, specialty_entity_to_specialty
from database.dao.SpecialtyDao import SpecialtyDao
from database.entity.SpecialtyEntity import SpecialtyEntity
from domain.model.Specialty import Specialty


class SpecialtyRepository:

    def __init__(self, dao: SpecialtyDao):
        self.__specialty_dao = dao

    def insert_specialty(self, specialty: Specialty):
        student_entity = specialty_to_specialty_entity(specialty)
        self.__specialty_dao.insert_specialty(student_entity)

    def remove_specialty(self, specialty: Specialty):
        student_entity = specialty_to_specialty_entity(specialty)
        self.__specialty_dao.delete_specialty(student_entity)

    def get_all_specialties(self):
        specialty_entities = self.__specialty_dao.get_specialties()
        specialties = self.__map_specialty_entities_to_specialty(specialty_entities)
        return specialties

    @staticmethod
    def __map_specialty_entities_to_specialty(specialty_entities: list[SpecialtyEntity]) -> list[Specialty]:
        specialties = []
        for specialty_entity in specialty_entities:
            specialty = specialty_entity_to_specialty(specialty_entity)
            specialties.append(specialty)
        return specialties
