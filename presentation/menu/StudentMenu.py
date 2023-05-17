from presentation.Context import Context
from presentation.menu.DeductStudentMenu import DeductStudentMenu
from presentation.menu.EditStudentMenu import EditStudentMenu
from presentation.menu.TransferStudentMenu import TransferStudentMenu
from presentation.resource.ResourceId import ResourceId


class StudentMenu:

    def __init__(self, context: Context):
        self.__student_id = None
        self.__menu_interpreter = context.menu_interpreter
        self.__context = context

    def __on_start(self):
        self.__menu_interpreter.clear()
        self.__STUDENT_MENU = {
            '0': self.__context.resource_manager.get_localized_string(ResourceId.back),
            '1': self.__context.resource_manager.get_localized_string(ResourceId.edit),
            '2': self.__context.resource_manager.get_localized_string(ResourceId.deduct),
            '3': self.__context.resource_manager.get_localized_string(ResourceId.transfer),
        }
        student = self.__context.get_student_by_id_use_case.invoke(self.__student_id)
        self.__menu_interpreter.print_student(context=self.__context, student=student)
        self.__menu_interpreter.print_menu(self.__STUDENT_MENU)

    def run(self, student_id: int):
        self.__student_id = student_id
        is_on_screen = True
        while is_on_screen:
            self.__on_start()
            item = self.__menu_interpreter.read(
                self.__context, self.__context.resource_manager.get_localized_string(ResourceId.enter_item), int
            )
            is_on_screen = self.__navigate(item)
        self.__on_finish()

    def __navigate(self, item: int):
        if item == 0:
            return False
        elif item == 1:
            EditStudentMenu(self.__context).run(self.__student_id)
            return True
        elif item == 2:
            DeductStudentMenu(self.__context).run(self.__student_id)
            return True
        elif item == 3:
            TransferStudentMenu(self.__context).run(self.__student_id)
            return True
        else:
            self.__menu_interpreter.clear()
            return True

    def __on_finish(self):
        self.__menu_interpreter.clear()

