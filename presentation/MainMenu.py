from presentation.AddMenu import AddMenu
from presentation.Container import Container
from presentation.MenuInterpreter import MenuInterpreter


class MainMenu:

    __MAIN_MENU = {
        '1': 'Add student',
        '2': 'Edit student',
        '3': 'Search',
        '4': 'Deduction',
        '5': 'Transfer',
        '6': 'Exit'
    }

    def __init__(self, container: Container):
        self.__container = container
        self.__menu_interpreter = MenuInterpreter()
        self.__menu_interpreter.clear()
        pass

    def run(self):
        is_on_screen = True
        while is_on_screen:
            print("Welcome to 'program name'")
            self.__menu_interpreter.print_menu(self.__MAIN_MENU)
            item = self.__menu_interpreter.read("Enter item: ", int)
            is_on_screen = self.__navigate(item)
            self.__menu_interpreter.clear()
        self.__on_exit()

    def __on_exit(self):
        self.__menu_interpreter.clear()
        self.__menu_interpreter.print_page_title("Bye-bye")

    def __navigate(self, item: int) -> bool:
        if item == 1:
            AddMenu(container=self.__container).run()
            return True
        elif item == 2:
            return True
        elif item == 3:
            return True
        elif item == 4:
            return True
        elif item == 5:
            return True
        elif item == 6:
            return False
        else:
            return True

