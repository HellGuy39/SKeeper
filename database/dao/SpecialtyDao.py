from database.StudentDatabase import StudentDatabase
from database.entity.SpecialtyEntity import SpecialtyEntity


class SpecialtyDao:

    def __init__(self, database: StudentDatabase):
        self.__database = database

    def insert_specialty(self, specialtyEntity: SpecialtyEntity):
        self.__database.cursor.execute(
            f"""
            INSERT INTO {self.__database.SPECIALTIES_TABLE_NAME} 
            (`name`) 
            VALUES (?);
            """,
            (specialtyEntity.name, )
        )
        self.__database.connection.commit()

    def delete_specialty(self, specialtyEntity: SpecialtyEntity):
        self.__database.cursor.execute(f"""
            DELETE FROM {self.__database.SPECIALTIES_TABLE_NAME} WHERE `id` = ?
        """, (specialtyEntity.id,))
        self.__database.connection.commit()

    def get_specialties(self):
        self.__database.cursor.execute(f"""
            SELECT * FROM {self.__database.SPECIALTIES_TABLE_NAME} 
        """)
        specialties = []
        table_rows = self.__database.cursor.fetchall()
        for row in table_rows:
            specialty = self.__table_row_to_specialty(row)
            specialties.append(specialty)
        return specialties

    @staticmethod
    def __table_row_to_specialty(row):
        return SpecialtyEntity(
                id=row[0],
                name=row[1],
            )
