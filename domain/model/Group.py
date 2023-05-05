from dataclasses import dataclass


@dataclass(init=True, frozen=True)
class Group:
    id: int = 0
    name: str = ""
