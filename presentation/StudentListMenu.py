from domain.model.Student import Student
from presentation.Context import Context
from presentation.MenuInterpreter import MenuInterpreter
from presentation.StudentMenu import StudentMenu


class StudentListMenu:

    def __init__(self, context: Context):
        self.__menu_interpreter = MenuInterpreter()
        self.__context = context

    def run(self, students: list[Student]):
        is_on_screen = True

        while is_on_screen:
            self.__menu_interpreter.clear()
            self.__menu_interpreter.print_page_title("Results")

            if len(students) == 0:
                print("Nothing was found...")

            print("0. Back")

            for i in range(len(students)):
                print(f"{i + 1}. {students[i].id} | {students[i].group} | {students[i].fullname} ")

            item = self.__menu_interpreter.read("Enter item: ", int)
            if item in range(0, len(students) + 1):
                if item == 0:
                    is_on_screen = False
                else:
                    student = students[item - 1]
                    StudentMenu(self.__context).run(student)
            else:
                pass

        self.__menu_interpreter.clear()

    def __on_finish(self):
        self.__menu_interpreter.clear()