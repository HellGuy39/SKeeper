import os


class MenuInterpreter:

    def __init__(self):
        pass

    @staticmethod
    def print_menu(menu: dict[str, str]):
        print('#' * 20)
        for key, value in menu.items():
            print(f"{key}. {value}")
        print('#' * 20)

    @staticmethod
    def print_page_title(title: str):
        print('#' * 20)
        print(title)
        print('#' * 20)

    @staticmethod
    def read(message: str, type: type):

        while True:
            command = input(message)
            try:
                if type == int:
                    result = int(command)
                elif type == float:
                    result = float(command)
                else:
                    result = command
                return result
            except ValueError:
                print("Invalid value. Try Again")

    @staticmethod
    def clear():
        os.system('clear')
