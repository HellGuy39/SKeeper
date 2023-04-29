import os
from domain.model import Student
import re


class MenuInterpreter:

    def __init__(self):
        pass

    @staticmethod
    def print_student(student: Student):
        print('#' * 20)
        print(
            f"ID: {student.id}\n"
            f"Fullname: {student.fullname}\n"
            f"Birthday: {student.birthday}\n"
            f"Address: {student.address}\n"
            f"Average: {student.average}\n"
            f"Phone: {student.phone}\n"
            f"Group: {student.group}\n"
            f"Specialty: {student.specialty}\n"
            f"Enrollment_order: {student.enrollment_order}\n"
            f"Allocation_order: {student.allocation_order}\n"
            f"Allocation_reason: {student.allocation_reason}\n"
            f"Status: {student.status.name}"
        )

    @staticmethod
    def print_menu(menu: dict[str, str]):
        print('#' * 20)
        for key, value in menu.items():
            print(f"{key}. {value}")
        print('#' * 20)

    @staticmethod
    def print_page_title(title: str):
        print('#' * 20)
        print(title)
        print('#' * 20)

    @staticmethod
    def read(message: str, type: type):

        while True:
            command = input(message)
            try:
                if type == int:
                    result = int(command)
                elif type == float:
                    result = float(command)
                else:
                    result = command
                return result
            except ValueError:
                print("Invalid value. Try Again")

    @staticmethod
    def read_with_regex(message: str, regex: str):

        while True:
            command = input(message)
            try:
                result = str(command)
                pattern = re.compile(regex)

                if pattern.match(result):
                    return result
                else:
                    print("Value does not match the required format")
            except ValueError:
                print("Invalid value. Try Again")

    @staticmethod
    def read_ranged_int(message: str, start: int, end: int) -> int:

        while True:
            command = input(message)
            try:
                result = int(command)

                if result not in range(start, end):
                    print("The value should be from 1 to 3")
                else:
                    return result
            except ValueError:
                print("Invalid value. Try Again")

    @staticmethod
    def clear():
        os.system('cls||clear')
