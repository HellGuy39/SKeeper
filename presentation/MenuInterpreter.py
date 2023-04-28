import os
from domain.model import Student


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
            f"Status: {student.status}"
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
    def clear():
        os.system('clear')
