from database.StudentDatabase import StudentDatabase
from database.entity.GroupEntity import GroupEntity


class GroupDao:

    def __init__(self, database: StudentDatabase):
        self.__database = database

    def insert_group(self, groupEntity: GroupEntity):
        self.__database.cursor.execute(
            f"""
            INSERT INTO {self.__database.GROUPS_TABLE_NAME} 
            (`name`) 
            VALUES (?);
            """,
            (groupEntity.name,)
        )
        self.__database.connection.commit()

    def delete_group(self, groupEntity: GroupEntity):
        self.__database.cursor.execute(f"""
            DELETE FROM {self.__database.GROUPS_TABLE_NAME} WHERE `id` = ?
        """, (groupEntity.id,))
        self.__database.connection.commit()

    def get_groups(self):
        self.__database.cursor.execute(f"""
            SELECT * FROM {self.__database.GROUPS_TABLE_NAME} 
        """)
        specialties = []
        table_rows = self.__database.cursor.fetchall()
        for row in table_rows:
            specialty = self.__table_row_to_group(row)
            specialties.append(specialty)
        return specialties

    @staticmethod
    def __table_row_to_group(row):
        return GroupEntity(
            id=row[0],
            name=row[1],
        )
