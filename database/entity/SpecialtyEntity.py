from dataclasses import dataclass


@dataclass(init=True, frozen=True)
class SpecialtyEntity:
    id: int = 0
    name: str = ""
