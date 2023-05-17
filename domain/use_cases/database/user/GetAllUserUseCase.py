from data.repository.UserRepository import UserRepository
from domain.model.User import User


class GetAllUsersUseCase:

    def __init__(self, repository: UserRepository):
        self.__repository = repository

    def invoke(self) -> list[User]:
        return self.__repository.get_all_users()
