from database.StudentDatabase import StudentDatabase
from database.entity.StudentEntity import StudentEntity


class StudentDao:

    def __init__(self):
        self.__database = StudentDatabase()

    def insert_student(self, studentEntity: StudentEntity):
        self.__database.cursor.execute(f"""
            INSERT INTO {self.__database.STUDENTS_TABLE_NAME} 
            (id, name, email, joining_date, salary) 
            VALUES (?, ?, ?, ?, ?);
        """, (0, 0))
        self.__database.connection.commit()
