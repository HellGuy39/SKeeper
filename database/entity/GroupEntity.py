from dataclasses import dataclass


@dataclass(init=True, frozen=True)
class GroupEntity:
    id: int = 0
    name: str = ""
