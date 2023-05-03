from presentation.Context import Context
from presentation.menu.MainMenu import MainMenu

if __name__ == '__main__':
    container = Context()
    MainMenu(container).run()
