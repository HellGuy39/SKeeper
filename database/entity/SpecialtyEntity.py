from dataclasses import dataclass


@dataclass(init=True, frozen=True)
class SpecialtyEntity:
    id: int = 0
    name: str = ""


SPECIALTY_SCHEMA = """
(
`id` INTEGER PRIMARY KEY, 
`name` TEXT NOT NULL
)
"""
