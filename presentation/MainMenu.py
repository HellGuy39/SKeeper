from presentation.AddMenu import AddMenu
from presentation.Context import Context
from presentation.MenuInterpreter import MenuInterpreter
from presentation.SearchMenu import SearchMenu


class MainMenu:

    __MAIN_MENU = {
        '1': 'Add student',
        '2': 'Search',
        #'3': 'Settings',
        '0': 'Exit'
    }

    def __init__(self, context: Context):
        self.__context = context
        self.__menu_interpreter = MenuInterpreter()
        self.__menu_interpreter.clear()
        pass

    def run(self):
        is_on_screen = True
        while is_on_screen:
            print("Welcome to SKeeper v1.0")
            self.__menu_interpreter.print_menu(self.__MAIN_MENU)
            item = self.__menu_interpreter.read("Enter item: ", int)
            is_on_screen = self.__navigate(item)
            self.__menu_interpreter.clear()
        self.__on_exit()

    def __on_exit(self):
        self.__menu_interpreter.clear()
        self.__menu_interpreter.print_page_title("Bye-bye")

    def __navigate(self, item: int) -> bool:
        if item == 0:
            return False
        if item == 1:
            AddMenu(container=self.__context).run()
            return True
        elif item == 2:
            SearchMenu(context=self.__context).run()
            return True
        elif item == 3:
            return True
        else:
            return True

