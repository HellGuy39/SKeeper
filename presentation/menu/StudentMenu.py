from domain.model.Student import Student
from presentation.Context import Context
from presentation.ResourceManager import ResourceId
from presentation.menu.DeductStudentMenu import DeductStudentMenu
from presentation.menu.EditStudentMenu import EditStudentMenu
from presentation.menu.TransferStudentMenu import TransferStudentMenu


class StudentMenu:

    def __init__(self, context: Context):
        self.__menu_interpreter = context.menu_interpreter
        self.__context = context
        self.__student = Student()

    def __on_start(self):
        self.__STUDENT_MENU = {
            '0': self.__context.resource_manager.get_localized_string(ResourceId.back),
            '1': self.__context.resource_manager.get_localized_string(ResourceId.edit),
            '2': self.__context.resource_manager.get_localized_string(ResourceId.deduct),
            '3': self.__context.resource_manager.get_localized_string(ResourceId.transfer),
        }

    def run(self, student: Student):
        self.__menu_interpreter.clear()
        self.__student = student
        is_on_screen = True
        while is_on_screen:
            self.__on_start()
            self.__menu_interpreter.print_student(context=self.__context, student=student)
            self.__menu_interpreter.print_menu(self.__STUDENT_MENU)
            item = self.__menu_interpreter.read(
                self.__context, self.__context.resource_manager.get_localized_string(ResourceId.enter_item), int
            )
            is_on_screen = self.__navigate(item)
        self.__on_finish()

    def __navigate(self, item: int):
        if item == 0:
            return False
        elif item == 1:
            EditStudentMenu(self.__context).run(self.__student)
            return True
        elif item == 2:
            DeductStudentMenu(self.__context).run(self.__student)
            return True
        elif item == 3:
            TransferStudentMenu(self.__context).run(self.__student)
            return True
        else:
            self.__menu_interpreter.clear()
            return True

    def __on_finish(self):
        self.__menu_interpreter.clear()

