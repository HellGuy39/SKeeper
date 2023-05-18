from dataclasses import dataclass


@dataclass(init=True, frozen=True)
class GroupEntity:
    id: int = 0
    name: str = ""


GROUP_SCHEMA = """
(
`id` INTEGER PRIMARY KEY, 
`name` TEXT NOT NULL 
)
"""
