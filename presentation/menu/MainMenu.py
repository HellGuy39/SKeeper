from domain.model.Student import StudentStatus
from presentation.Context import Context
from presentation.ResourceManager import ResourceId
from presentation.menu.AddMenu import AddMenu
from presentation.menu.GroupMenu import GroupMenu
from presentation.menu.SearchMenu import SearchMenu
from presentation.menu.SettingsMenu import SettingsMenu
from presentation.menu.SpecialtyMenu import SpecialtyMenu


class MainMenu:

    def __init__(self, context: Context):
        self.__context = context
        self.__menu_interpreter = context.menu_interpreter
        self.__menu_interpreter.clear()

    def run(self):
        is_on_screen = True
        while is_on_screen:
            self.__on_start()
            settings = self.__context.get_application_settings_use_case
            print(f"{self.__context.resource_manager.get_localized_string(ResourceId.welcome)} SKeeper v1.0")
            print('#' * 20)
            print(f"{self.__context.resource_manager.get_localized_string(ResourceId.facility)}: "
                  f"{settings.invoke().nameOfFacility}")
            print(f"{self.__context.resource_manager.get_localized_string(ResourceId.number_of_students)}: "
                  f"{len(self.__context.get_students_by_status_use_case.invoke(StudentStatus.Study))}")
            self.__menu_interpreter.print_menu(self.__MAIN_MENU)
            item = self.__menu_interpreter.read(
                self.__context, self.__context.resource_manager.get_localized_string(ResourceId.enter_item), int
            )
            is_on_screen = self.__navigate(item)
            self.__menu_interpreter.clear()
        self.__on_finish()

    def __on_start(self):
        self.__MAIN_MENU = {
            '1': self.__context.resource_manager.get_localized_string(ResourceId.add_student),
            '2': self.__context.resource_manager.get_localized_string(ResourceId.search),
            '3': self.__context.resource_manager.get_localized_string(ResourceId.groups),
            '4': self.__context.resource_manager.get_localized_string(ResourceId.specialties),
            '5': self.__context.resource_manager.get_localized_string(ResourceId.settings),
            '0': self.__context.resource_manager.get_localized_string(ResourceId.exit)
        }

    def __on_finish(self):
        self.__menu_interpreter.clear()
        self.__menu_interpreter.print_page_title(
            self.__context.resource_manager.get_localized_string(ResourceId.bye_bye)
        )

    def __navigate(self, item: int) -> bool:
        match item:
            case 0:
                return False
            case 1:
                AddMenu(context=self.__context).run()
                return True
            case 2:
                SearchMenu(context=self.__context).run()
                return True
            case 3:
                GroupMenu(context=self.__context).run()
                return True
            case 4:
                SpecialtyMenu(context=self.__context).run()
                return True
            case 5:
                SettingsMenu(context=self.__context).run()
                return True
            case _:
                return True
