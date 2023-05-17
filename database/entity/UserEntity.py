from dataclasses import dataclass


@dataclass(init=True, frozen=True)
class UserEntity:
    id: int = 0
    login: str = ""
    password: str = ""
    role: int = 1
