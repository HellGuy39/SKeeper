from data.mapper.StudentMapper import student_to_student_entity
from data.mapper.StudentMapper import student_entity_to_student
from database.dao.StudentDao import StudentDao
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

    def search_students_by_id(self, id: int):
        student_entities = self.__student_dao.search_students_by_id(id)
        students = []
        for student_entity in student_entities:
            student = student_entity_to_student(student_entity)
            students.append(student)
        return students

    def search_students_by_fullname(self, fullname: str):
        student_entities = self.__student_dao.search_students_by_fullname(fullname)
        students = []
        for student_entity in student_entities:
            student = student_entity_to_student(student_entity)
            students.append(student)
        return students
