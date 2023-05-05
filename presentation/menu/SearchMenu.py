from domain.model.Student import Student, int_to_student_status
from presentation.Context import Context
from presentation.ResourceManager import ResourceId
from presentation.menu.StudentListMenu import StudentListMenu


class SearchMenu:

    def __init__(self, context: Context):
        self.__menu_interpreter = context.menu_interpreter
        self.__context = context

    def run(self):
        is_on_screen = True
        while is_on_screen:
            self.__on_start()
            self.__menu_interpreter.print_menu(self.__SEARCH_MENU)
            item = self.__menu_interpreter.read(
                self.__context, self.__context.resource_manager.get_localized_string(ResourceId.enter_item), int
            )
            is_on_screen = self.__navigate(item)
        self.__on_finish()

    def __on_start(self):
        self.__menu_interpreter.clear()
        self.__SEARCH_MENU = {
            '0': self.__context.resource_manager.get_localized_string(ResourceId.back),
            '1': self.__context.resource_manager.get_localized_string(ResourceId.search_by_fullname),
            '2': self.__context.resource_manager.get_localized_string(ResourceId.search_by_group),
            '3': self.__context.resource_manager.get_localized_string(ResourceId.search_by_specialty),
            '4': self.__context.resource_manager.get_localized_string(ResourceId.search_by_status),
        }

    def __on_finish(self):
        self.__menu_interpreter.clear()

    def __navigate(self, item: int):
        if item == 0:
            return False
        elif item == 1:
            self.__search_by_fullname()
            return True
        elif item == 2:
            self.__search_by_group()
            return True
        elif item == 3:
            self.__search_by_specialty()
            return True
        elif item == 4:
            self.__search_by_status()
            return True
        else:
            self.__menu_interpreter.clear()
            return True

    def __search_by_fullname(self):
        self.__menu_interpreter.clear()
        self.__menu_interpreter.print_page_title(
            self.__context.resource_manager.get_localized_string(ResourceId.search)
        )
        fullname = self.__menu_interpreter.read(
            context=self.__context,
            message=self.__context.resource_manager.get_localized_string(ResourceId.fullname),
            required_type=str
        )
        students = self.__context.get_students_by_fullname_use_case.invoke(fullname=fullname)
        StudentListMenu(self.__context).run(self.__student_to_ids(students))

    def __search_by_group(self):
        self.__menu_interpreter.clear()
        self.__menu_interpreter.print_page_title(
            self.__context.resource_manager.get_localized_string(ResourceId.search)
        )
        group_name = self.__menu_interpreter.read(
            context=self.__context,
            message=self.__context.resource_manager.get_localized_string(ResourceId.group),
            required_type=str
        )
        students = self.__context.get_student_by_group_use_case.invoke(group=group_name)
        StudentListMenu(self.__context).run(self.__student_to_ids(students))

    def __search_by_specialty(self):
        self.__menu_interpreter.clear()
        self.__menu_interpreter.print_page_title(
            self.__context.resource_manager.get_localized_string(ResourceId.search)
        )
        specialty_name = self.__menu_interpreter.read(
            context=self.__context,
            message=self.__context.resource_manager.get_localized_string(ResourceId.specialty),
            required_type=str
        )
        students = self.__context.get_student_by_specialty_use_case.invoke(specialty=specialty_name)
        StudentListMenu(self.__context).run(self.__student_to_ids(students))

    def __search_by_status(self):
        self.__menu_interpreter.clear()
        self.__menu_interpreter.print_page_title(
            self.__context.resource_manager.get_localized_string(ResourceId.search)
        )
        status_value = self.__menu_interpreter.read_ranged_int(
            context=self.__context,
            message=self.__context.resource_manager.get_localized_string(ResourceId.status),
            start=1,
            end=3
        )
        students = self.__context.get_students_by_status_use_case.invoke(status=int_to_student_status(status_value))
        StudentListMenu(self.__context).run(self.__student_to_ids(students))

    @staticmethod
    def __student_to_ids(students: list[Student]):
        ids = []
        for student in students:
            ids.append(student.id)
        return ids
