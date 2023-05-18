from dataclasses import dataclass


@dataclass(init=True, frozen=True)
class UserEntity:
    id: int = 0
    login: str = ""
    password: str = ""
    role: int = 1


USER_SCHEMA = """
(
`id` INTEGER PRIMARY KEY, 
`login` TEXT NOT NULL,
`password` TEXT NOT NULL,
`role` INTEGER NOT NULL
)
"""
