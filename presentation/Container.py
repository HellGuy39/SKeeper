from data.repository.StudentRepository import StudentRepository
from database.StudentDatabase import StudentDatabase
from database.dao.StudentDao import StudentDao
from domain.use_cases.AddStudentUseCase import AddStudentUseCase
from domain.use_cases.EditStudentUseCase import EditStudentUseCase
from domain.use_cases.RemoveStudentUseCase import RemoveStudentUseCase


class Container:

    def __init__(self):
        self.__repository = StudentRepository(StudentDao(StudentDatabase()))

        self.addStudentUseCase = AddStudentUseCase(self.__repository)
        self.editStudentUseCase = EditStudentUseCase(self.__repository)
        self.removeStudentUseCase = RemoveStudentUseCase(self.__repository)