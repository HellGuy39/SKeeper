from presentation.Context import Context
from presentation.MenuInterpreter import MenuInterpreter
from presentation.ResourceManager import ResourceId
from presentation.StudentListMenu import StudentListMenu


class SearchMenu:

    def __init__(self, context: Context):
        self.__menu_interpreter = MenuInterpreter()
        self.__context = context
        self.__SEARCH_MENU = {
            '0': self.__context.resource_manager.get_localized_string(ResourceId.back),
            '1': 'Search by fullname',
            '2': 'Search by id'
        }

    def run(self):
        self.__menu_interpreter.clear()
        is_on_screen = True
        while is_on_screen:
            self.__menu_interpreter.print_menu(self.__SEARCH_MENU)
            item = self.__menu_interpreter.read("Enter item: ", int)
            is_on_screen = self.__navigate(item)
        self.__on_finish()

    def __on_finish(self):
        self.__menu_interpreter.clear()

    def __navigate(self, item: int):
        if item == 0:
            return False
        elif item == 1:
            self.__search_by_fullname()
            return True
        elif item == 2:
            self.__search_by_id()
            return True
        else:
            self.__menu_interpreter.clear()
            return True

    def __search_by_fullname(self):
        self.__menu_interpreter.clear()
        self.__menu_interpreter.print_page_title("Search")
        fullname = self.__menu_interpreter.read("Fullname: ", str)
        students = self.__context.search_students_by_fullname_use_case.invoke(fullname=fullname)
        StudentListMenu(self.__context).run(students)

    def __search_by_id(self):
        self.__menu_interpreter.clear()
        self.__menu_interpreter.print_page_title("Search")
        id = self.__menu_interpreter.read("Id: ", int)
        students = self.__context.search_students_by_id_use_case.invoke(id=id)
        StudentListMenu(self.__context).run(students)