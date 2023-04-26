from domain.model.Student import Student
from database.entity.StudentEntity import StudentEntity


def student_to_student_entity(student: Student) -> StudentEntity:
    return StudentEntity(
        id=student.id,
        fullname=student.fullname,
        birthday=student.birthday,
        address=student.address,
        average=student.average,
        phone=student.phone,
        group=student.group,
        specialty=student.specialty,
        enrollment_order=student.enrollment_order,
        allocation_order=student.allocation_order,
        allocation_reason=student.allocation_reason,
        status=student.status,
    )


def student_entity_to_student(studentEntity: StudentEntity) -> Student:
    return Student(
        id=studentEntity.id,
        fullname=studentEntity.fullname,
        birthday=studentEntity.birthday,
        address=studentEntity.address,
        average=studentEntity.average,
        phone=studentEntity.phone,
        group=studentEntity.group,
        specialty=studentEntity.specialty,
        enrollment_order=studentEntity.enrollment_order,
        allocation_order=studentEntity.allocation_order,
        allocation_reason=studentEntity.allocation_reason,
        status=studentEntity.status,
    )
