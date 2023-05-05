from data.repository.SpecialtyRepository import SpecialtyRepository
from domain.model.Specialty import Specialty


class GetAllSpecialtyUseCase:

    def __init__(self, repository: SpecialtyRepository):
        self.__repository = repository

    def invoke(self) -> list[Specialty]:
        return self.__repository.get_all_specialties()
