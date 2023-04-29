from dataclasses import replace

from domain.model.Student import Student, StudentStatus
from presentation.Context import Context
from presentation.MenuInterpreter import MenuInterpreter
from presentation.ResourceManager import ResourceId


class TransferStudentMenu:

    def __init__(self, context: Context):
        self.__menu_interpreter = MenuInterpreter()
        self.__context = context
        self.__TRANSFER_STUDENT_MENU = {
            '0': self.__context.resource_manager.get_localized_string(ResourceId.back),
            '1': 'Transfer',
        }

    def run(self, student: Student):
        self.__menu_interpreter.clear()
        is_on_screen = True
        while is_on_screen:
            self.__menu_interpreter.print_menu(self.__TRANSFER_STUDENT_MENU)
            item = self.__menu_interpreter.read("Enter item: ", int)
            is_on_screen = self.__navigate(item, student)
        self.__on_finish()

    def __on_finish(self):
        self.__menu_interpreter.clear()

    def __navigate(self, item: int, student: Student):
        if item == 0:
            return False
        elif item == 1:
            self.__transfer(student)
            return False
        else:
            self.__menu_interpreter.clear()
            return True

    def __transfer(self, student: Student):
        self.__menu_interpreter.clear()
        self.__menu_interpreter.print_page_title("Transfer")

        allocation_order = self.__menu_interpreter.read("Allocation order: ", str)
        allocation_reason = self.__menu_interpreter.read("Allocation reason: ", str)

        specialty = self.__menu_interpreter.read("Specialty: ", str)
        group = self.__menu_interpreter.read("Group: ", str)

        old_student = replace(
            student,
            allocation_order=allocation_order,
            allocation_reason=allocation_reason,
            status=StudentStatus.Transferred
        )
        new_student = replace(student, id=0, specialty=specialty, group=group)

        self.__context.edit_student_use_case.invoke(old_student)
        self.__context.add_student_use_case.invoke(new_student)
        self.__menu_interpreter.clear()
