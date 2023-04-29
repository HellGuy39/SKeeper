from domain.model.Student import Student
from presentation.Context import Context
from presentation.DeductStudentMenu import DeductStudentMenu
from presentation.EditStudentMenu import EditStudentMenu
from presentation.MenuInterpreter import MenuInterpreter
from presentation.TransferStudentMenu import TransferStudentMenu


class StudentMenu:

    __STUDENT_MENU = {
        '0': 'Back',
        '1': 'Edit',
        '2': 'Deduct',
        '3': 'Transfer',
    }

    def __init__(self, context: Context):
        self.__menu_interpreter = MenuInterpreter()
        self.__context = context
        self.__student = Student()
        pass

    def run(self, student: Student):
        self.__menu_interpreter.clear()
        self.__student = student
        is_on_screen = True
        while is_on_screen:
            self.__menu_interpreter.print_student(student)
            self.__menu_interpreter.print_menu(self.__STUDENT_MENU)
            item = self.__menu_interpreter.read("Enter item: ", int)
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

