from data.repository.SpecialtyRepository import SpecialtyRepository
from domain.model.Specialty import Specialty


class InsertSpecialtyUseCase:

    def __init__(self, repository: SpecialtyRepository):
        self.__repository = repository

    def invoke(self, specialty: Specialty):
        return self.__repository.insert_specialty(specialty)
