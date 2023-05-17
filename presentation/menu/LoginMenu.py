from dataclasses import replace

from presentation.Context import Context
from presentation.menu.CreateUserMenu import CreateUserMenu
from presentation.resource.ResourceId import ResourceId


class LoginMenu:

    def __init__(self, context: Context):
        self.__context = context
        self.__menu_interpreter = context.menu_interpreter

    def run(self):
        users = self.__context.get_all_users_use_case.invoke()

        if len(users) == 0:
            CreateUserMenu(self.__context).run(is_first_user=True)

        is_on_screen = True
        while is_on_screen:
            self.__on_start()

            item = self.__menu_interpreter.read(
                context=self.__context,
                message=self.__context.resource_manager.get_localized_string(ResourceId.enter_item),
                required_type=int
            )

            is_on_screen = self.__navigate(item)

        self.__on_finish()

    def __on_start(self):
        self.__menu_interpreter.clear()
        print(self.__context.resource_manager.get_localized_string(ResourceId.welcome) + " SKeeper 3.0")
        self.__LOGIN_MENU = {
            '1': self.__context.resource_manager.get_localized_string(ResourceId.authorization),
            '0': self.__context.resource_manager.get_localized_string(ResourceId.exit_program)
        }
        self.__menu_interpreter.print_menu(self.__LOGIN_MENU)

    def __on_finish(self):
        self.__menu_interpreter.clear()

    def __semi_auth(self, user_id: int) -> bool:
        user = self.__context.get_user_by_id_use_case.invoke(user_id=user_id)

        self.__menu_interpreter.clear()
        self.__menu_interpreter.print_page_title(
            f"{self.__context.resource_manager.get_localized_string(ResourceId.sign_as)} {user.login}"
        )
        password = self.__menu_interpreter.read(
            context=self.__context,
            message=self.__context.resource_manager.get_localized_string(ResourceId.enter_password),
            required_type=str
        )
        if password == user.password:
            return True
        else:
            return False

    def __auth(self) -> bool:
        self.__menu_interpreter.clear()
        self.__menu_interpreter.print_page_title(
            self.__context.resource_manager.get_localized_string(ResourceId.authorization)
        )
        login = self.__menu_interpreter.read(
            context=self.__context,
            message=self.__context.resource_manager.get_localized_string(ResourceId.enter_login),
            required_type=str
        )
        password = self.__menu_interpreter.read(
            context=self.__context,
            message=self.__context.resource_manager.get_localized_string(ResourceId.enter_password),
            required_type=str
        )

        users = self.__context.get_all_users_use_case.invoke()
        for user in users:
            if login == user.login and password == user.password:
                settings = self.__context.get_application_settings_use_case.invoke()
                updated_settings = replace(settings, userId=user.id)
                self.__context.save_application_settings_use_case.invoke(updated_settings)
                return True

        return False

    def __navigate(self, item: int) -> bool:
        match item:
            case 0:
                self.__menu_interpreter.exit_program(self.__context)
                return True
            case 1:
                settings = self.__context.get_application_settings_use_case.invoke()

                if settings.userId != -1:
                    return not self.__semi_auth(settings.userId)
                else:
                    return not self.__auth()

            case _:
                return True
