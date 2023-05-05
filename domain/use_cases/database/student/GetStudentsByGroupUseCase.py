from data.repository.StudentRepository import StudentRepository
from domain.model.Group import Group
from domain.model.Student import Student


class GetStudentsByGroupUseCase:

    def __init__(self, repository: StudentRepository):
        self.__repository = repository

    def invoke(self, group: str) -> list[Student]:
        return self.__repository.get_students_by_group(group)
