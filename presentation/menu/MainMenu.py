from dataclasses import replace

from domain.model.Student import StudentStatus
from presentation.Context import Context
from presentation.menu.CreateStudentMenu import CreateStudentMenu
from presentation.menu.GroupMenu import GroupMenu
from presentation.menu.LoginMenu import LoginMenu
from presentation.menu.SearchMenu import SearchMenu
from presentation.menu.SettingsMenu import SettingsMenu
from presentation.menu.SpecialtyMenu import SpecialtyMenu
from presentation.menu.UserManagerMenu import UserManagerMenu
from presentation.resource.ResourceId import ResourceId


class MainMenu:

    def __init__(self, context: Context):
        self.__context = context
        self.__menu_interpreter = context.menu_interpreter
        self.__menu_interpreter.clear()

    def run(self):

        LoginMenu(self.__context).run()

        is_on_screen = True
        while is_on_screen:
            self.__on_start()
            item = self.__menu_interpreter.read(
                context=self.__context,
                message=self.__context.resource_manager.get_localized_string(ResourceId.enter_item),
                required_type=int
            )
            is_on_screen = self.__navigate(item)
            self.__menu_interpreter.clear()

        self.__on_finish()

    def __on_start(self):
        settings = self.__context.get_application_settings_use_case.invoke()
        user = self.__context.get_user_by_id_use_case.invoke(settings.userId)

        print('#' * 20)
        print(f"{self.__context.resource_manager.get_localized_string(ResourceId.facility)}: "
              f"{settings.nameOfFacility}")
        print(f"{self.__context.resource_manager.get_localized_string(ResourceId.number_of_students)}: "
              f"{len(self.__context.get_students_by_status_use_case.invoke(StudentStatus.Study))}")
        self.__menu_interpreter.print_menu({
            '1': self.__context.resource_manager.get_localized_string(ResourceId.add_student),
            '2': self.__context.resource_manager.get_localized_string(ResourceId.search),
            '3': self.__context.resource_manager.get_localized_string(ResourceId.groups),
            '4': self.__context.resource_manager.get_localized_string(ResourceId.specialties),
            '5': self.__context.resource_manager.get_localized_string(ResourceId.settings),
            '6': self.__context.resource_manager.get_localized_string(ResourceId.user_manager),
            '7': self.__context.resource_manager.get_localized_string(ResourceId.change_user),
            '0': self.__context.resource_manager.get_localized_string(ResourceId.exit_program)
        })

    def __on_finish(self):
        self.__menu_interpreter.clear()
        self.__menu_interpreter.print_page_title(
            self.__context.resource_manager.get_localized_string(ResourceId.bye_bye)
        )

    def __navigate(self, item: int) -> bool:
        match item:
            case 0:
                self.__menu_interpreter.exit_program(context=self.__context)
                return True
            case 1:
                CreateStudentMenu(context=self.__context).run()
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
            case 6:
                UserManagerMenu(context=self.__context).run()
                return True
            case 7:
                settings = self.__context.get_application_settings_use_case.invoke()
                updated_settings = replace(settings, userId=-1)
                self.__context.save_application_settings_use_case.invoke(updated_settings)
                LoginMenu(self.__context).run()
                return True
            case _:
                return True
