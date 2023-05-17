from data.repository.UserRepository import UserRepository
from domain.model.User import User


class GetUserByIdUseCase:

    def __init__(self, repository: UserRepository):
        self.__repository = repository

    def invoke(self, user_id: int) -> User | None:
        users = self.__repository.get_users_by_id(user_id)

        if len(users) > 0:
            return users[0]
        else:
            return None
