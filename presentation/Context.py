from data.repository.GroupRepository import GroupRepository
from data.repository.SettingsRepository import SettingsRepository
from data.repository.SpecialtyRepository import SpecialtyRepository
from data.repository.StudentRepository import StudentRepository
from database.StudentDatabase import StudentDatabase
from database.dao.GroupDao import GroupDao
from database.dao.SpecialtyDao import SpecialtyDao
from database.dao.StudentDao import StudentDao
from domain.use_cases.database.group.InsertGroupUseCase import InsertGroupUseCase
from domain.use_cases.database.group.RemoveGroupUseCase import RemoveGroupUseCase
from domain.use_cases.database.specialty.InsertSpecialtyUseCase import InsertSpecialtyUseCase
from domain.use_cases.database.specialty.RemoveSpecialtyUseCase import RemoveSpecialtyUseCase
from domain.use_cases.database.student.AddStudentUseCase import AddStudentUseCase
from domain.use_cases.database.student.EditStudentUseCase import EditStudentUseCase
from domain.use_cases.database.student.GetAllStudentIdsUseCase import GetAllStudentIdsUseCase
from domain.use_cases.database.student.GetStudentsByGroupUseCase import GetStudentsByGroupUseCase
from domain.use_cases.database.student.GetStudentsBySpecialtyUseCase import GetStudentsBySpecialtyUseCase
from domain.use_cases.database.student.GetStudentsByStatusUseCase import GetStudentsByStatusUseCase
from domain.use_cases.database.student.RemoveStudentUseCase import RemoveStudentUseCase
from domain.use_cases.database.student.GetStudentsByFullnameUseCase import SearchStudentsByFullnameUseCase
from domain.use_cases.database.student.GetStudentByIdUseCase import GetStudentByIdUseCase
from domain.use_cases.database.group.GetAllGroupsUseCase import GetAllGroupsUseCase
from domain.use_cases.database.specialty.GetAllSpecialtyUseCase import GetAllSpecialtyUseCase
from domain.use_cases.file.GetApplicatonSettignsUseCase import GetApplicationSettingsUseCase
from domain.use_cases.file.SaveApplicationSettingsUseCase import SaveApplicationSettingsUseCase
from presentation.MenuInterpreter import MenuInterpreter
from presentation.ResourceManager import ResourceManager


class Context:

    def __init__(self):
        database = StudentDatabase()

        student_dao = StudentDao(database)
        group_dao = GroupDao(database)
        specialty_dao = SpecialtyDao(database)

        student_repository = StudentRepository(student_dao)
        group_repository = GroupRepository(group_dao)
        specialty_repository = SpecialtyRepository(specialty_dao)
        settings_repository = SettingsRepository()

        self.resource_manager = ResourceManager(
            GetApplicationSettingsUseCase(settings_repository).invoke().language
        )

        self.menu_interpreter = MenuInterpreter()

        self.get_students_by_status_use_case = GetStudentsByStatusUseCase(student_repository)
        self.add_student_use_case = AddStudentUseCase(student_repository)
        self.edit_student_use_case = EditStudentUseCase(student_repository)
        self.remove_student_use_case = RemoveStudentUseCase(student_repository)
        self.get_students_by_fullname_use_case = SearchStudentsByFullnameUseCase(student_repository)
        self.get_student_by_id_use_case = GetStudentByIdUseCase(student_repository)
        self.get_all_student_ids_use_case = GetAllStudentIdsUseCase(student_repository)
        self.get_student_by_group_use_case = GetStudentsByGroupUseCase(student_repository)
        self.get_student_by_specialty_use_case = GetStudentsBySpecialtyUseCase(student_repository)

        self.get_application_settings_use_case = GetApplicationSettingsUseCase(settings_repository)
        self.save_application_settings_use_case = SaveApplicationSettingsUseCase(settings_repository)

        self.get_all_groups_use_case = GetAllGroupsUseCase(group_repository)
        self.remove_group_use_case = RemoveGroupUseCase(group_repository)
        self.insert_group_use_case = InsertGroupUseCase(group_repository)

        self.get_all_specialty_use_case = GetAllSpecialtyUseCase(specialty_repository)
        self.remove_specialty_use_case = RemoveSpecialtyUseCase(specialty_repository)
        self.insert_specialty_use_case = InsertSpecialtyUseCase(specialty_repository)
