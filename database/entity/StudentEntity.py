from dataclasses import dataclass


@dataclass(init=True, frozen=True)
class StudentEntity:
    id: int = 0
    fullname: str = ""
    birthday: str = ""
    address: str = ""
    average: float = 1.0
    phone: str = ""
    group: str = ""
    specialty: str = ""
    enrollment_order: str = ""
    allocation_order: str = ""
    allocation_reason: str = ""
    status: str = ""
