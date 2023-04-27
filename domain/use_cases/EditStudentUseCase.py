from data.repository.StudentRepository import StudentRepository
from domain.model.Student import Student


class EditStudentUseCase:

    def __init__(self, repository: StudentRepository):
        self.__repository = repository

    def invoke(self, student: Student):
        pass