import sqlite3

from common.FileProvider import FileProvider


class StudentDatabase:

    DATABASE_NAME = "student_database"
    USERS_TABLE_NAME = "users_table"
    STUDENTS_TABLE_NAME = "students_table"
    GROUPS_TABLE_NAME = "groups_table"
    SPECIALTIES_TABLE_NAME = "specialties_table"

    def __init__(self):

        self.connection = sqlite3.connect(FileProvider.get_file_path(filename=self.DATABASE_NAME))

        self.cursor = self.connection.cursor()
        self.init_students_table()
        self.init_group_table()
        self.init_specialties_table()
        self.init_user_table()

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

    def init_group_table(self):
        self.cursor.execute(
            f"""
            CREATE TABLE IF NOT EXISTS {self.GROUPS_TABLE_NAME} 
            (
            `id` INTEGER PRIMARY KEY, 
            `name` TEXT NOT NULL 
            )
            """
        )
        self.connection.commit()

    def init_specialties_table(self):
        self.cursor.execute(
            f"""
            CREATE TABLE IF NOT EXISTS {self.SPECIALTIES_TABLE_NAME} 
            (
            `id` INTEGER PRIMARY KEY, 
            `name` TEXT NOT NULL
            )
            """
        )
        self.connection.commit()

    def init_user_table(self):
        self.cursor.execute(
            f"""
            CREATE TABLE IF NOT EXISTS {self.USERS_TABLE_NAME} 
            (
            `id` INTEGER PRIMARY KEY, 
            `login` TEXT NOT NULL,
            `password` TEXT NOT NULL,
            `role` INTEGER NOT NULL
            )
            """
        )
        self.connection.commit()

