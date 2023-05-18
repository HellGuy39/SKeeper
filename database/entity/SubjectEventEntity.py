from dataclasses import dataclass


@dataclass(init=True, frozen=True)
class SubjectEventEntity:
    id: int = 0
    name_of_event: str = ""
    date: str = ""
    marks: str = ""


SUBJECT_EVENT_SCHEMA = """
(
`id` INTEGER PRIMARY KEY, 
`name_of_event` TEXT NOT NULL, 
`date` TEXT NOT NULL, 
`marks` TEXT NOT NULL
)
"""
