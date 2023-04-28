from data.repository.StudentRepository import StudentRepository
from database.StudentDatabase import StudentDatabase
from database.dao.StudentDao import StudentDao
from domain.use_cases.AddStudentUseCase import AddStudentUseCase
from domain.use_cases.EditStudentUseCase import EditStudentUseCase
from domain.use_cases.RemoveStudentUseCase import RemoveStudentUseCase
from domain.use_cases.SearchStudentsByFullnameUseCase import SearchStudentsByFullnameUseCase
from domain.use_cases.SearchStudentsByIdUseCase import SearchStudentsByIdUseCase
from presentation.ResourceManager import ResourceManager


class Context:

    def __init__(self):
        self.__repository = StudentRepository(StudentDao(StudentDatabase()))

        self.resource_manager = ResourceManager()

        self.add_student_use_case = AddStudentUseCase(self.__repository)
        self.edit_student_use_case = EditStudentUseCase(self.__repository)
        self.remove_student_use_case = RemoveStudentUseCase(self.__repository)
        self.search_students_by_fullname_use_case = SearchStudentsByFullnameUseCase(self.__repository)
        self.search_students_by_id_use_case = SearchStudentsByIdUseCase(self.__repository)