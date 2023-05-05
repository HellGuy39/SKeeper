from data.repository.StudentRepository import StudentRepository


class GetAllStudentIdsUseCase:

    def __init__(self, repository: StudentRepository):
        self.__repository = repository

    def invoke(self) -> list[int]:
        students = self.__repository.get_all_students()
        ids = []
        for student in students:
            ids.append(student.id)
        return ids
