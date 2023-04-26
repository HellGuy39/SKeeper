from data.mapper.StudentMapper import student_to_student_entity
from database.dao.StudentDao import StudentDao
from domain.model import Student


class StudentRepository:
    student_dao = StudentDao()

    def add_student(self, student: Student):
        student_entity = student_to_student_entity(student)
        self.student_dao.insert_student(student_entity)

    def remove_student(self, student: Student):
        pass

    def edit_student(self, student: Student):
        pass

    def search_students(self, student: Student):
        pass
