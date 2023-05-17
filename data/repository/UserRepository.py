from data.mapper.UserMapper import user_to_user_entity, user_entity_to_user
from database.dao.UserDao import UserDao
from database.entity.UserEntity import UserEntity
from domain.model.User import User


class UserRepository:

    def __init__(self, dao: UserDao):
        self.__group_dao = dao

    def insert_user(self, user: User):
        user_entity = user_to_user_entity(user)
        self.__group_dao.insert_user(user_entity)

    def remove_user(self, user: User):
        user_entity = user_to_user_entity(user)
        self.__group_dao.delete_user(user_entity)

    def get_all_users(self) -> list[User]:
        user_entities = self.__group_dao.get_all_users()
        users = self.__map_user_entities_to_user(user_entities)
        return users

    def get_users_by_id(self, user_id: int):
        user_entities = self.__group_dao.get_users_by_id(user_id)
        users = self.__map_user_entities_to_user(user_entities)
        return users

    @staticmethod
    def __map_user_entities_to_user(user_entities: list[UserEntity]) -> list[User]:
        users = []
        for user_entity in user_entities:
            user = user_entity_to_user(user_entity)
            users.append(user)
        return users
