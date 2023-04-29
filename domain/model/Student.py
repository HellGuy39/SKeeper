import enum
from dataclasses import dataclass


class StudentStatus(enum.Enum):
    Study = 1
    Enrolled = 2
    Transferred = 3


@dataclass(init=True, frozen=True)
class Student:
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
    status: StudentStatus = StudentStatus.Study


def int_to_student_status(value: int) -> StudentStatus:
    if value == 1:
        return StudentStatus.Study
    elif value == 2:
        return StudentStatus.Enrolled
    else:
        return StudentStatus.Transferred


def student_status_to_int(state: StudentStatus) -> int:
    if state is StudentStatus.Study:
        return 1
    elif state is StudentStatus.Enrolled:
        return 2
    else:
        return 3
