import sqlite3


class StudentDatabase:

    DATABASE_NAME = "student_database"
    STUDENTS_TABLE_NAME = "students_table"

    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()

    def __init__(self):
        self.init_students_table()

    def init_students_table(self):
        self.cursor.execute(
            f"""
            CREATE TABLE IF NOT EXISTS {self.STUDENTS_TABLE_NAME} 
            (
            `id` INTEGER AUTO_INCREMENT PRIMARY KEY, 
            `fullname` TEXT NOT NULL, 
            `birthday` TEXT NOT NULL, 
            `address` TEXT NOT NULL, 
            `average_score` FLOAT NOT NULL, 
            `phone` TEXT NOT NULL, 
            `group` TEXT NOT NULL, 
            `specialty` TEXT NOT NULL, 
            `enrollment_order` TEXT NOT NULL, 
            `allocation_order` TEXT NOT NULL, 
            `allocation_reason` TEXT NOT NULL,
            `status` TEXT NOT NULL
            )
            """
        )
        self.connection.commit()

