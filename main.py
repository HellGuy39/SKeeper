from common.Colorizer import Colorizer
from presentation.Context import Context
from presentation.menu.MainMenu import MainMenu

if __name__ == '__main__':
    context = Context()
    
    settings = context.get_application_settings_use_case.invoke()
    Colorizer.set_terminal_color(schema=settings.colorSchema)

    MainMenu(context=context).run()
