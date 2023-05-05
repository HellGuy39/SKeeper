from dataclasses import dataclass


@dataclass(init=True, frozen=True)
class Specialty:
    id: int = 0
    name: str = ""
