from domain.model.Student import Student, StudentStatus
from presentation.Context import Context
from presentation.MenuInterpreter import MenuInterpreter
from presentation.StudentMenu import StudentMenu


class StudentListMenu:

    def __init__(self, context: Context):
        self.__menu_interpreter = MenuInterpreter()
        self.__context = context

    def run(self, students: list[Student]):
        is_on_screen = True

        sorted_students = self.__sort_student_list(students)

        while is_on_screen:
            self.__menu_interpreter.clear()
            self.__menu_interpreter.print_page_title("Results")

            print("0. Back")

            if len(students) == 0:
                print("Nothing was found...")
            else:
                for i in range(len(sorted_students)):
                    print(
                        f"{i + 1}. {sorted_students[i].status.name} | {sorted_students[i].group} | {sorted_students[i].fullname} ")

            item = self.__menu_interpreter.read("Enter item: ", int)
            if item in range(0, len(sorted_students) + 1):
                if item == 0:
                    is_on_screen = False
                else:
                    student = sorted_students[item - 1]
                    StudentMenu(self.__context).run(student)
            else:
                pass

        self.__menu_interpreter.clear()

    def __on_finish(self):
        self.__menu_interpreter.clear()

    @staticmethod
    def __sort_student_list(students: list[Student]) -> list[Student]:
        enrolled_students = []
        studying_students = []
        transferred_students = []

        for i in range(len(students)):
            student = students[i]

            if student.status is StudentStatus.Study:
                studying_students.append(student)
            elif student.status is StudentStatus.Enrolled:
                enrolled_students.append(student)
            elif student.status is StudentStatus.Transferred:
                transferred_students.append(student)

        studying_students.extend(transferred_students)
        studying_students.extend(enrolled_students)

        return studying_students
