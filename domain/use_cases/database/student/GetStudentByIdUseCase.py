from data.repository.StudentRepository import StudentRepository
from domain.model.Student import Student


class GetStudentByIdUseCase:

    def __init__(self, repository: StudentRepository):
        self.__repository = repository

    def invoke(self, id: int) -> Student | None:
        students = self.__repository.get_students_by_id(id)
        if len(students) > 0:
            return students[0]
        else:
            return None
