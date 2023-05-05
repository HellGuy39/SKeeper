from data.repository.StudentRepository import StudentRepository
from domain.model.Student import Student


class SearchStudentsByFullnameUseCase:

    def __init__(self, repository: StudentRepository):
        self.__repository = repository

    def invoke(self, fullname: str) -> list[Student]:
        return self.__repository.get_students_by_fullname(fullname)
