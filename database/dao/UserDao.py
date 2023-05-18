from database.StudentDatabase import StudentDatabase
from database.entity.UserEntity import UserEntity


class UserDao:

    def __init__(self, database: StudentDatabase):
        self.__database = database

    def insert_user(self, userEntity: UserEntity):
        self.__database.cursor.execute(
            f"""
            INSERT INTO {self.__database.USERS_TABLE_NAME} 
            (`login`, `password`, `role`) 
            VALUES (?, ?, ?)
            """,
            (userEntity.login, userEntity.password, userEntity.role, )
        )
        self.__database.connection.commit()

    def delete_user(self, userEntity: UserEntity):
        self.__database.cursor.execute(f"""
            DELETE FROM {self.__database.GROUPS_TABLE_NAME} 
            WHERE `id` = ?
        """, (userEntity.id,))
        self.__database.connection.commit()

    def get_all_users(self):
        self.__database.cursor.execute(f"""
            SELECT * FROM {self.__database.USERS_TABLE_NAME} 
        """)
        users = []
        table_rows = self.__database.cursor.fetchall()
        for row in table_rows:
            user = self.__table_row_to_user(row)
            users.append(user)
        return users

    def get_users_by_id(self, user_id: int):
        self.__database.cursor.execute(f"""
            SELECT * FROM {self.__database.USERS_TABLE_NAME} 
            WHERE `id` = ? 
        """, (user_id, ))
        users = []
        table_rows = self.__database.cursor.fetchall()
        for row in table_rows:
            user = self.__table_row_to_user(row)
            users.append(user)
        return users

    @staticmethod
    def __table_row_to_user(row):
        return UserEntity(
                id=row[0],
                login=row[1],
                password=row[2],
                role=row[3]
        )
