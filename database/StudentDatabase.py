import sqlite3
import platform
import os


class StudentDatabase:

    DATABASE_NAME = "student_database"
    STUDENTS_TABLE_NAME = "students_table"

    def __init__(self):
        if platform.system() == 'Windows':
            dir = os.getenv('APPDATA')
            path = os.path.join(dir, 'SKeeper')
            os.makedirs(path, exist_ok=True)

            self.connection = sqlite3.connect(os.getenv('APPDATA') + '/SKeeper/' + self.DATABASE_NAME)
        else:
            self.connection = sqlite3.connect(self.DATABASE_NAME)

        self.cursor = self.connection.cursor()
        self.init_students_table()

    def init_students_table(self):
        self.cursor.execute(
            f"""
            CREATE TABLE IF NOT EXISTS {self.STUDENTS_TABLE_NAME} 
            (
            `id` INTEGER PRIMARY KEY, 
            `fullname` TEXT NOT NULL, 
            `birthday` TEXT NOT NULL, 
            `address` TEXT NOT NULL, 
            `average` FLOAT NOT NULL, 
            `phone` TEXT NOT NULL, 
            `group` TEXT NOT NULL, 
            `specialty` TEXT NOT NULL, 
            `enrollment_order` TEXT NOT NULL, 
            `allocation_order` TEXT NOT NULL, 
            `allocation_reason` TEXT NOT NULL,
            `status` INTEGER NOT NULL
            )
            """
        )
        self.connection.commit()
