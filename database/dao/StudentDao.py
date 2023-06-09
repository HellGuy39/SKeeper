from database.StudentDatabase import StudentDatabase
from database.entity.StudentEntity import StudentEntity


class StudentDao:

    def __init__(self, database: StudentDatabase):
        self.__database = database

    def insert_student(self, studentEntity: StudentEntity):
        self.__database.cursor.execute(
            f"""
            INSERT INTO {self.__database.STUDENTS_TABLE_NAME} 
            (`id`,`fullname`, `birthday`, `address`, `average`, `phone`, `group`, 
            `specialty`, `enrollment_order`, `allocation_order`, `allocation_reason`, `status`) 
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?) 
            """,
            (studentEntity.id, studentEntity.fullname, studentEntity.birthday, studentEntity.address,
             studentEntity.average, studentEntity.phone, studentEntity.group, studentEntity.specialty,
             studentEntity.enrollment_order, studentEntity.allocation_order, studentEntity.allocation_reason,
             studentEntity.status)
        )
        self.__database.connection.commit()

    def update_student(self, studentEntity: StudentEntity):
        self.__database.cursor.execute(
            f"""
            UPDATE {self.__database.STUDENTS_TABLE_NAME} 
            set `fullname` = ?, `birthday` = ?, `address` = ?, `average` = ?, `phone` = ?, `group` = ?, 
            `specialty` = ?, `enrollment_order` = ?, `allocation_order` = ?, `allocation_reason` = ?, 
            `status` = ? WHERE `id` = ? 
            """,
            (studentEntity.fullname, studentEntity.birthday, studentEntity.address,
             studentEntity.average, studentEntity.phone, studentEntity.group, studentEntity.specialty,
             studentEntity.enrollment_order, studentEntity.allocation_order, studentEntity.allocation_reason,
             studentEntity.status, studentEntity.id)
        )
        self.__database.connection.commit()

    def delete_student(self, studentEntity: StudentEntity):
        self.__database.cursor.execute(
            f"""
            DELETE FROM {self.__database.STUDENTS_TABLE_NAME} WHERE `id` = ?
            """,
            (studentEntity.id,)
        )
        self.__database.connection.commit()

    def get_students_by_id(self, student_id):
        self.__database.cursor.execute(
            f"""
            SELECT * FROM {self.__database.STUDENTS_TABLE_NAME} WHERE `id` = ?
            """,
            (student_id,)
        )
        table_rows = self.__database.cursor.fetchall()
        students = self.__table_rows_to_students(table_rows)
        return students

    def get_students_by_fullname(self, fullname):
        self.__database.cursor.execute(
            f"""
            SELECT * FROM {self.__database.STUDENTS_TABLE_NAME} WHERE `fullname` LIKE '%' || ? || '%' 
            """,
            (fullname,)
        )
        table_rows = self.__database.cursor.fetchall()
        students = self.__table_rows_to_students(table_rows)
        return students

    def get_students_by_status(self, status_value):
        self.__database.cursor.execute(
            f"""
            SELECT * FROM {self.__database.STUDENTS_TABLE_NAME} WHERE `status` = ? 
            """,
            (status_value,)
        )
        table_rows = self.__database.cursor.fetchall()
        students = self.__table_rows_to_students(table_rows)
        return students

    def get_students_by_specialty(self, specialty):
        self.__database.cursor.execute(
            f"""
            SELECT * FROM {self.__database.STUDENTS_TABLE_NAME} WHERE `specialty` = ? 
            """,
            (specialty,)
        )
        table_rows = self.__database.cursor.fetchall()
        students = self.__table_rows_to_students(table_rows)
        return students

    def get_students_by_group(self, group):
        self.__database.cursor.execute(
            f"""
            SELECT * FROM {self.__database.STUDENTS_TABLE_NAME} WHERE `group` = ? 
            """, (group,)
        )
        table_rows = self.__database.cursor.fetchall()
        students = self.__table_rows_to_students(table_rows)
        return students

    def get_all_students(self):
        self.__database.cursor.execute(
            f"""
            SELECT * FROM {self.__database.STUDENTS_TABLE_NAME}
            """
        )
        table_rows = self.__database.cursor.fetchall()
        students = self.__table_rows_to_students(table_rows)
        return students

    def __table_rows_to_students(self, table_rows):
        students = []
        for row in table_rows:
            student = self.__table_row_to_student(row)
            students.append(student)
        return students

    @staticmethod
    def __table_row_to_student(row):
        return StudentEntity(
                id=row[0],
                fullname=row[1],
                birthday=row[2],
                address=row[3],
                average=row[4],
                phone=row[5],
                group=row[6],
                specialty=row[7],
                enrollment_order=row[8],
                allocation_order=row[9],
                allocation_reason=row[10],
                status=row[11],
            )
