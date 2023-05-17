from data.repository.UserRepository import UserRepository
from domain.model.User import User


class InsertUserUseCase:

    def __init__(self, repository: UserRepository):
        self.__repository = repository

    def invoke(self, user: User):
        self.__repository.insert_user(user)
