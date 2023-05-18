import os
import re

from domain.model import Student
from presentation.resource.ResourceId import ResourceId


class MenuInterpreter:

    def __init__(self):
        pass

    def print_student(self, context, student: Student):
        resource_manager = context.resource_manager
        self.print_divider()
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
        self.print_divider()
        for key, value in menu.items():
            print(f"{key}. {value}")
        self.print_divider()

    def print_menu_with_title(self, title: str, menu: dict[str, str]):
        self.print_divider()
        print(title)
        self.print_divider()
        for key, value in menu.items():
            print(f"{key}. {value}")
        self.print_divider()

    def print_page_title(self, title: str):
        self.print_divider()
        print(title)
        self.print_divider()

    def read(self, context, message: str, required_type: type):
        resource_manager = context.resource_manager
        while True:
            command = input(message)
            try:
                if required_type == int:
                    result = int(command)
                elif required_type == float:
                    result = float(command)
                else:
                    result = command
                return result
            except ValueError:
                print(resource_manager.get_localized_string(ResourceId.invalid_value))

    def read_and_format(self, context, message: str):
        resource_manager = context.resource_manager
        while True:
            command = input(message)
            try:
                result = command

                result.strip()

                return re.sub(' +', ' ', result)
            except ValueError:
                print(resource_manager.get_localized_string(ResourceId.invalid_value))

    def read_not_existed_in_list(self, context, message: str, required_type: type, value_list, error_message: str):
        resource_manager = context.resource_manager
        while True:
            command = input(message)
            try:
                if required_type == int:
                    result = int(command)
                elif required_type == float:
                    result = float(command)
                else:
                    result = command

                if not value_list.__contains__(result):
                    return result
                else:
                    print(error_message)
            except ValueError:
                print(resource_manager.get_localized_string(ResourceId.invalid_value))

    def read_existed_in_list(self, context, message: str, required_type: type, value_list, error_message: str):
        resource_manager = context.resource_manager
        while True:
            command = input(message)
            try:
                if required_type == int:
                    result = int(command)
                elif required_type == float:
                    result = float(command)
                else:
                    result = command

                if value_list.__contains__(result):
                    return result
                else:
                    print(error_message)
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

    def print_divider(self):
        print('#' * 20)

    def clear(self):
        os.system('cls||clear')

    def exit_program(self, context):
        resource_manager = context.resource_manager
        self.clear()
        self.print_page_title(
            resource_manager.get_localized_string(ResourceId.bye_bye)
        )
        exit()
