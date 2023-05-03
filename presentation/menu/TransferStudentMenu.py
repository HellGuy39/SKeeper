from dataclasses import replace

from domain.model.Student import Student, StudentStatus
from presentation.Context import Context
from presentation.ResourceManager import ResourceId


class TransferStudentMenu:

    def __init__(self, context: Context):
        self.__menu_interpreter = context.menu_interpreter
        self.__context = context

    def __on_start(self):
        self.__TRANSFER_STUDENT_MENU = {
            '0': self.__context.resource_manager.get_localized_string(ResourceId.back),
            '1': self.__context.resource_manager.get_localized_string(ResourceId.transfer),
        }

    def run(self, student: Student):
        self.__menu_interpreter.clear()
        is_on_screen = True
        while is_on_screen:
            self.__on_start()
            self.__menu_interpreter.print_menu(self.__TRANSFER_STUDENT_MENU)
            item = self.__menu_interpreter.read(
                self.__context, self.__context.resource_manager.get_localized_string(ResourceId.enter_item), int
            )
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
        self.__menu_interpreter.print_page_title(
            self.__context.resource_manager.get_localized_string(ResourceId.transfer)
        )

        allocation_order = self.__menu_interpreter.read(
            self.__context, self.__context.resource_manager.get_localized_string(ResourceId.allocation_order), str
        )
        allocation_reason = self.__menu_interpreter.read(
            self.__context, self.__context.resource_manager.get_localized_string(ResourceId.allocation_reason), str
        )

        specialty = self.__menu_interpreter.read(
            self.__context, self.__context.resource_manager.get_localized_string(ResourceId.specialty), str
        )
        group = self.__menu_interpreter.read(
            self.__context, self.__context.resource_manager.get_localized_string(ResourceId.group), str
        )

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
