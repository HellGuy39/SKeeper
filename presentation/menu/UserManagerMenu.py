from presentation.Context import Context
from presentation.menu.CreateUserMenu import CreateUserMenu
from presentation.menu.UserListMenu import UserListMenu
from presentation.resource.ResourceId import ResourceId


class UserManagerMenu:

    def __init__(self, context: Context):
        self.__menu_interpreter = context.menu_interpreter
        self.__context = context

    def run(self):
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
        self.__menu_interpreter.print_menu({
                '0': self.__context.resource_manager.get_localized_string(ResourceId.back),
                '1': self.__context.resource_manager.get_localized_string(ResourceId.list_of_users),
                '2': self.__context.resource_manager.get_localized_string(ResourceId.add_user),
                # '3': "Удалить пользователя",
            })

    def __on_finish(self):
        self.__menu_interpreter.clear()

    def __navigate(self, item: int):
        match item:
            case 0:
                return False
            case 1:
                UserListMenu(context=self.__context).run()
                return True
            case 2:
                CreateUserMenu(context=self.__context).run(is_first_user=False)
                return True
            case 3:

                return True
            case _:
                return True
