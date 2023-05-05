from data.repository.StudentRepository import StudentRepository
from domain.model.Group import Group
from domain.model.Specialty import Specialty
from domain.model.Student import Student


class GetStudentsBySpecialtyUseCase:

    def __init__(self, repository: StudentRepository):
        self.__repository = repository

    def invoke(self, specialty: str) -> list[Student]:
        return self.__repository.get_students_by_specialty(specialty)
