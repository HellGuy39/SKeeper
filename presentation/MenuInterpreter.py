import os
from domain.model import Student
import re

from presentation.ResourceManager import ResourceId


class MenuInterpreter:

    def __init__(self):
        pass

    def print_student(self, context, student: Student):
        resource_manager = context.resource_manager
        print('#' * 20)
        print(
            f"{resource_manager.get_localized_string(ResourceId.id)}{student.id}\n"
            f"{resource_manager.get_localized_string(ResourceId.fullname)}{student.fullname}\n"
            f"{resource_manager.get_localized_string(ResourceId.birthday)}{student.birthday}\n"
            f"{resource_manager.get_localized_string(ResourceId.address)}{student.address}\n"
            f"{resource_manager.get_localized_string(ResourceId.average)}{student.average}\n"
            f"{resource_manager.get_localized_string(ResourceId.phone)}{student.phone}\n"
            f"{resource_manager.get_localized_string(ResourceId.group)}{student.group}\n"
            f"{resource_manager.get_localized_string(ResourceId.specialty)}{student.specialty}\n"
            f"{resource_manager.get_localized_string(ResourceId.enrollment_order)}{student.enrollment_order}\n"
            f"{resource_manager.get_localized_string(ResourceId.allocation_order)}{student.allocation_order}\n"
            f"{resource_manager.get_localized_string(ResourceId.allocation_reason)}{student.allocation_reason}\n"
            f"{resource_manager.get_localized_string(ResourceId.status)}{student.status.value}"
        )

    def print_menu(self, menu: dict[str, str]):
        print('#' * 20)
        for key, value in menu.items():
            print(f"{key}. {value}")
        print('#' * 20)

    def print_page_title(self, title: str):
        print('#' * 20)
        print(title)
        print('#' * 20)

    def read(self, context, message: str, type: type):
        resource_manager = context.resource_manager
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
                print(resource_manager.get_localized_string(ResourceId.invalid_value))

    def read_with_regex(self, context, message: str, regex: str):
        resource_manager = context.resource_manager
        while True:
            command = input(message)
            try:
                result = str(command)
                pattern = re.compile(regex)

                if pattern.match(result):
                    return result
                else:
                    print(resource_manager.get_localized_string(ResourceId.value_does_not_match))
            except ValueError:
                print(resource_manager.get_localized_string(ResourceId.invalid_value))

    def read_ranged_int(self, context, message: str, start: int, end: int) -> int:
        resource_manager = context.resource_manager
        while True:
            command = input(message)
            try:
                result = int(command)

                if result not in range(start, end + 1):
                    print(f"{resource_manager.get_localized_string(ResourceId.value_should_be_in_range)}"
                          f": {start} - {end}")
                else:
                    return result
            except ValueError:
                print(resource_manager.get_localized_string(ResourceId.invalid_value))

    def clear(self):
        os.system('cls||clear')
