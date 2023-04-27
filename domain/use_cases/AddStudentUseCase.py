from domain.model.Student import Student
from data.repository.StudentRepository import StudentRepository


class AddStudentUseCase:

    def __init__(self, repository: StudentRepository):
        self.__repository = repository

    def invoke(self, student: Student):
        self.__repository.add_student(student)