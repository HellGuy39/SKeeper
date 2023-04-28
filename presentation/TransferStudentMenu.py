from domain.model.Student import Student
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
            return True
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

