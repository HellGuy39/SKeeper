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
    status: int = 0


STUDENT_SCHEMA = """
(
`id` INTEGER PRIMARY KEY, 
`fullname` TEXT NOT NULL, 
`birthday` TEXT NOT NULL, 
`address` TEXT NOT NULL, 
`average` FLOAT NOT NULL, 
`phone` TEXT NOT NULL, 
`group` TEXT NOT NULL, 
`specialty` TEXT NOT NULL, 
`enrollment_order` TEXT NOT NULL, 
`allocation_order` TEXT NOT NULL, 
`allocation_reason` TEXT NOT NULL,
`status` INTEGER NOT NULL
)
"""
