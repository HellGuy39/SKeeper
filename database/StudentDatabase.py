import sqlite3

from common.FileProvider import FileProvider
from database.entity.GroupEntity import GROUP_SCHEMA
from database.entity.SpecialtyEntity import SPECIALTY_SCHEMA
from database.entity.StudentEntity import STUDENT_SCHEMA
from database.entity.UserEntity import USER_SCHEMA


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
            CREATE TABLE IF NOT EXISTS {self.STUDENTS_TABLE_NAME} {STUDENT_SCHEMA}
            """
        )
        self.connection.commit()

    def init_group_table(self):
        self.cursor.execute(
            f"""
            CREATE TABLE IF NOT EXISTS {self.GROUPS_TABLE_NAME} {GROUP_SCHEMA}
            """
        )
        self.connection.commit()

    def init_specialties_table(self):
        self.cursor.execute(
            f"""
            CREATE TABLE IF NOT EXISTS {self.SPECIALTIES_TABLE_NAME} {SPECIALTY_SCHEMA}
            """
        )
        self.connection.commit()

    def init_user_table(self):
        self.cursor.execute(
            f"""
            CREATE TABLE IF NOT EXISTS {self.USERS_TABLE_NAME} {USER_SCHEMA}
            """
        )
        self.connection.commit()
