from dataclasses import replace

from presentation.Context import Context
from presentation.ResourceManager import ResourceId


class EditStudentMenu:

    def __init__(self, context: Context):
        self.__student_id = None
        self.__menu_interpreter = context.menu_interpreter
        self.__context = context

    def run(self, student_id: int):
        self.__student_id = student_id
        is_on_screen = True
        while is_on_screen:
            self.__on_start()
            self.__menu_interpreter.print_menu(self.__EDIT_STUDENT_MENU)
            item = self.__menu_interpreter.read(
                self.__context, self.__context.resource_manager.get_localized_string(ResourceId.enter_item), int
            )
            is_on_screen = self.__navigate(item)

        self.__on_finish()

    def __navigate(self, item: int) -> bool:
        if item == 0:
            return False
        elif item == 1:
            self.__change_fullname()
            return True
        elif item == 2:
            self.__change_birthday()
            return True
        elif item == 3:
            self.__change_address()
            return True
        elif item == 4:
            self.__change_phone()
            return True
        else:
            return True

    def __change_fullname(self):
        self.__menu_interpreter.clear()
        self.__menu_interpreter.print_page_title(
            self.__context.resource_manager.get_localized_string(ResourceId.change_fullname)
        )
        student = self.__context.get_student_by_id_use_case.invoke(self.__student_id)

        fullname = self.__menu_interpreter.read(
            self.__context, self.__context.resource_manager.get_localized_string(ResourceId.fullname), str
        )
        edited_student = replace(student, fullname=fullname)
        self.__context.edit_student_use_case.invoke(edited_student)

    def __change_birthday(self):
        self.__menu_interpreter.clear()
        self.__menu_interpreter.print_page_title(
            self.__context.resource_manager.get_localized_string(ResourceId.change_birthday)
        )
        student = self.__context.get_student_by_id_use_case.invoke(self.__student_id)

        birthday = self.__menu_interpreter.read(
            self.__context, self.__context.resource_manager.get_localized_string(ResourceId.deduct), str
        )
        edited_student = replace(student, birthday=birthday)
        self.__context.edit_student_use_case.invoke(edited_student)

    def __change_address(self):
        self.__menu_interpreter.clear()
        self.__menu_interpreter.print_page_title(
            self.__context.resource_manager.get_localized_string(ResourceId.change_address)
        )
        student = self.__context.get_student_by_id_use_case.invoke(self.__student_id)

        address = self.__menu_interpreter.read(
            self.__context, self.__context.resource_manager.get_localized_string(ResourceId.address), str
        )

        edited_student = replace(student, address=address)
        self.__context.edit_student_use_case.invoke(edited_student)

    def __change_phone(self):
        self.__menu_interpreter.clear()
        self.__menu_interpreter.print_page_title(
            self.__context.resource_manager.get_localized_string(ResourceId.change_phone)
        )
        student = self.__context.get_student_by_id_use_case.invoke(self.__student_id)

        phone = self.__menu_interpreter.read(
            self.__context, self.__context.resource_manager.get_localized_string(ResourceId.phone), str
        )
        edited_student = replace(student, phone=phone)
        self.__context.edit_student_use_case.invoke(edited_student)

    def __on_start(self):
        self.__menu_interpreter.clear()
        self.__EDIT_STUDENT_MENU = {
            '0': self.__context.resource_manager.get_localized_string(ResourceId.back),
            '1': self.__context.resource_manager.get_localized_string(ResourceId.change_fullname),
            '2': self.__context.resource_manager.get_localized_string(ResourceId.change_birthday),
            '3': self.__context.resource_manager.get_localized_string(ResourceId.change_address),
            '4': self.__context.resource_manager.get_localized_string(ResourceId.change_phone)
        }

    def __on_finish(self):
        self.__menu_interpreter.clear()
