from data.repository.SettingsRepository import SettingsRepository
from data.repository.StudentRepository import StudentRepository
from database.StudentDatabase import StudentDatabase
from database.dao.StudentDao import StudentDao
from domain.use_cases.database.AddStudentUseCase import AddStudentUseCase
from domain.use_cases.database.EditStudentUseCase import EditStudentUseCase
from domain.use_cases.database.GetStudentsByStatusUseCase import GetStudentsByStatusUseCase
from domain.use_cases.database.RemoveStudentUseCase import RemoveStudentUseCase
from domain.use_cases.database.SearchStudentsByFullnameUseCase import SearchStudentsByFullnameUseCase
from domain.use_cases.database.SearchStudentsByIdUseCase import SearchStudentsByIdUseCase
from domain.use_cases.file.GetApplicatonSettignsUseCase import GetApplicationSettingsUseCase
from domain.use_cases.file.SaveApplicationSettingsUseCase import SaveApplicationSettingsUseCase
from presentation.MenuInterpreter import MenuInterpreter
from presentation.ResourceManager import ResourceManager


class Context:

    def __init__(self):
        self.__student_repository = StudentRepository(StudentDao(StudentDatabase()))
        self.__settings_repository = SettingsRepository()

        self.resource_manager = ResourceManager(
            GetApplicationSettingsUseCase(self.__settings_repository).invoke().language
        )

        self.menu_interpreter = MenuInterpreter()

        self.get_students_by_status_use_case = GetStudentsByStatusUseCase(self.__student_repository)
        self.add_student_use_case = AddStudentUseCase(self.__student_repository)
        self.edit_student_use_case = EditStudentUseCase(self.__student_repository)
        self.remove_student_use_case = RemoveStudentUseCase(self.__student_repository)
        self.search_students_by_fullname_use_case = SearchStudentsByFullnameUseCase(self.__student_repository)
        self.search_students_by_id_use_case = SearchStudentsByIdUseCase(self.__student_repository)

        self.get_application_settings_use_case = GetApplicationSettingsUseCase(self.__settings_repository)
        self.save_application_settings_use_case = SaveApplicationSettingsUseCase(self.__settings_repository)
