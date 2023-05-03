from data.repository.StudentRepository import StudentRepository
from domain.model.Student import Student, StudentStatus


class GetStudentsByStatusUseCase:

    def __init__(self, repository: StudentRepository):
        self.__repository = repository

    def invoke(self, status: StudentStatus) -> list[Student]:
        return self.__repository.get_students_by_status(status)
