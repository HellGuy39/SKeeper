from data.repository.StudentRepository import StudentRepository
from domain.model.Student import Student


class SearchStudentsByIdUseCase:

    def __init__(self, repository: StudentRepository):
        self.__repository = repository

    def invoke(self, id: int) -> list[Student]:
        return self.__repository.search_students_by_id(id)