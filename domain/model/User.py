import enum
from dataclasses import dataclass


class UserRole(enum.Enum):
    Edit = 1
    Readonly = 2


def int_to_user_role(value: int) -> UserRole:
    if value == 1:
        return UserRole.Edit
    else:
        return UserRole.Readonly


def user_role_to_int(role: UserRole) -> int:
    return role.value


@dataclass(init=True, frozen=True)
class User:
    id: int = 0
    login: str = ""
    password: str = ""
    role: UserRole = UserRole.Readonly

