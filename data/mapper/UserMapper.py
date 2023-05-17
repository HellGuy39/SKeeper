from database.entity.UserEntity import UserEntity
from domain.model.User import int_to_user_role, user_role_to_int, User


def user_to_user_entity(user: User) -> UserEntity:
    return UserEntity(
            id=user.id,
            login=user.login,
            password=user.password,
            role=user_role_to_int(user.role)
        )


def user_entity_to_user(userEntity: UserEntity) -> User:
    return User(
            id=userEntity.id,
            login=userEntity.login,
            password=userEntity.password,
            role=int_to_user_role(userEntity.role)
        )
