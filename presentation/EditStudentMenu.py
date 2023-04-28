from dataclasses import replace

from domain.model.Student import Student
from presentation.Context import Context
from presentation.MenuInterpreter import MenuInterpreter


class EditStudentMenu:

    __EDIT_STUDENT_MENU = {
        '0': 'Back',
        '1': 'Change Fullname',
        '2': 'Change Birthday',
        '3': 'Change Address',
        '4': 'Change Phone'
    }

    def __init__(self, context: Context):
        self.__menu_interpreter = MenuInterpreter()
        self.__context = context

    def run(self, student: Student):
        is_on_screen = True

        while is_on_screen:
            self.__menu_interpreter.clear()
            self.__menu_interpreter.print_menu(self.__EDIT_STUDENT_MENU)
            item = self.__menu_interpreter.read("Enter item: ", int)
            is_on_screen = self.__navigate(item, student)

        self.__on_finish()

    def __navigate(self, item: int, student: Student) -> bool:
        if item == 0:
            return False
        elif item == 1:
            self.__change_fullname(student)
            return True
        elif item == 2:
            self.__change_birthday(student)
            return True
        elif item == 3:
            self.__change_address(student)
            return True
        elif item == 4:
            self.__change_phone(student)
            return True
        else:
            return True

    def __change_fullname(self, student: Student):
        self.__menu_interpreter.clear()
        self.__menu_interpreter.print_page_title("Change fullname")
        fullname = self.__menu_interpreter.read("Enter fullname: ", str)
        edited_student = replace(student, fullname=fullname)
        self.__context.edit_student_use_case.invoke(edited_student)

    def __change_birthday(self, student: Student):
        self.__menu_interpreter.clear()
        self.__menu_interpreter.print_page_title("Change birthday")
        birthday = self.__menu_interpreter.read("Enter birthday: ", str)
        edited_student = replace(student, birthday=birthday)
        self.__context.edit_student_use_case.invoke(edited_student)

    def __change_address(self, student: Student):
        self.__menu_interpreter.clear()
        self.__menu_interpreter.print_page_title("Change address")
        address = self.__menu_interpreter.read("Enter address: ", str)
        edited_student = replace(student, address=address)
        self.__context.edit_student_use_case.invoke(edited_student)

    def __change_phone(self, student: Student):
        self.__menu_interpreter.clear()
        self.__menu_interpreter.print_page_title("Change phone")
        phone = self.__menu_interpreter.read("Enter phone: ", str)
        edited_student = replace(student, phone=phone)
        self.__context.edit_student_use_case.invoke(edited_student)

    def __on_finish(self):
        self.__menu_interpreter.clear()
