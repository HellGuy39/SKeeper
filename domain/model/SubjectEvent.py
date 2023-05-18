from dataclasses import dataclass


@dataclass(init=True, frozen=True)
class SubjectEvent:
    id: int = 0
    name_of_event: str = ""
    date: str = ""
    marks: str = ""
