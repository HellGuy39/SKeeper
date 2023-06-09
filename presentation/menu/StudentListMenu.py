from domain.model.Student import Student, StudentStatus
from presentation.Context import Context
from presentation.resource.ResourceId import ResourceId
from presentation.menu.StudentMenu import StudentMenu


class StudentListMenu:

    def __init__(self, context: Context):
        self.__menu_interpreter = context.menu_interpreter
        self.__context = context

    def run(self, ids: list[int]):
        is_on_screen = True
        while is_on_screen:
            self.__on_start()

            students = []
            for i in range(len(ids)):
                student = self.__context.get_student_by_id_use_case.invoke(ids[i])
                students.append(student)

            sorted_students = self.__sort_student_list(students)

            print(f"0. {self.__context.resource_manager.get_localized_string(ResourceId.back)}")

            if len(students) == 0:
                print(self.__context.resource_manager.get_localized_string(ResourceId.nothing_was_found))
            else:
                for i in range(len(sorted_students)):

                    message = f"{i + 1}. {sorted_students[i].status.name} | " \
                              f"{sorted_students[i].group} | " \
                              f"{sorted_students[i].fullname}"

                    if sorted_students[i].status == StudentStatus.Study:
                        print(message)
                    elif sorted_students[i].status == StudentStatus.Enrolled:
                        print(message)
                    elif sorted_students[i].status == StudentStatus.Transferred:
                        print(message)

            item = self.__menu_interpreter.read(
                context=self.__context,
                message=self.__context.resource_manager.get_localized_string(ResourceId.enter_item),
                required_type=int
            )
            if item in range(0, len(sorted_students) + 1):
                if item == 0:
                    is_on_screen = False
                else:
                    student = sorted_students[item - 1]
                    StudentMenu(self.__context).run(student.id)
            else:
                pass

        self.__on_finish()

    def __on_start(self):
        self.__menu_interpreter.clear()
        self.__menu_interpreter.print_page_title(
            self.__context.resource_manager.get_localized_string(ResourceId.results)
        )

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
