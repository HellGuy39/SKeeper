from data.mapper.StudentMapper import student_to_student_entity
from data.mapper.StudentMapper import student_entity_to_student
from database.dao.StudentDao import StudentDao
from database.entity.StudentEntity import StudentEntity
from domain.model.Student import Student


class StudentRepository:

    def __init__(self, dao: StudentDao):
        self.__student_dao = dao

    def add_student(self, student: Student):
        student_entity = student_to_student_entity(student)
        self.__student_dao.insert_student(student_entity)

    def remove_student(self, student: Student):
        student_entity = student_to_student_entity(student)
        self.__student_dao.delete_student(student_entity)

    def edit_student(self, student: Student):
        student_entity = student_to_student_entity(student)
        self.__student_dao.update_student(student_entity)

    def get_students_by_status(self, status):
        student_entities = self.__student_dao.get_students_by_status(status.value)
        students = self.__map_student_entities_to_students(student_entities)
        return students

    def get_students_by_id(self, id: int):
        student_entities = self.__student_dao.get_students_by_id(id)
        students = self.__map_student_entities_to_students(student_entities)
        return students

    def get_students_by_fullname(self, fullname: str):
        student_entities = self.__student_dao.get_students_by_fullname(fullname)
        students = self.__map_student_entities_to_students(student_entities)
        return students

    def get_students_by_group(self, group: str):
        student_entities = self.__student_dao.get_students_by_group(group)
        students = self.__map_student_entities_to_students(student_entities)
        return students

    def get_students_by_specialty(self, specialty: str):
        student_entities = self.__student_dao.get_students_by_specialty(specialty)
        students = self.__map_student_entities_to_students(student_entities)
        return students

    def get_all_students(self):
        student_entities = self.__student_dao.get_all_students()
        students = self.__map_student_entities_to_students(student_entities)
        return students

    @staticmethod
    def __map_student_entities_to_students(student_entities: list[StudentEntity]) -> list[Student]:
        students = []
        for student_entity in student_entities:
            student = student_entity_to_student(student_entity)
            students.append(student)
        return students
