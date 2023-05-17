from presentation.Context import Context
from presentation.resource.ResourceId import ResourceId


# unfinished for technical reasons
class DeleteUserMenu:

    def __init__(self, context: Context):
        self.__menu_interpreter = context.menu_interpreter
        self.__context = context

    def run(self):
        is_on_screen = True
        while is_on_screen:
            self.__on_start()

            users = self.__context.get_all_users_use_case.invoke()

            print(f"0. {self.__context.resource_manager.get_localized_string(ResourceId.back)}")

            for i in range(len(users)):
                print(f"{i + 1}. {users[i].role.name} | {users[i].login}")

            item = self.__menu_interpreter.read(
                context=self.__context,
                message=self.__context.resource_manager.get_localized_string(ResourceId.enter_item),
                required_type=int
            )
            if item in range(0, len(users) + 1):
                if item == 0:
                    is_on_screen = False
                else:
                    pass
            else:
                pass

        self.__on_finish()

    def __on_start(self):
        self.__menu_interpreter.clear()
        self.__menu_interpreter.print_page_title(
            "Удалить пользователя"
        )

    def __on_finish(self):
        self.__menu_interpreter.clear()
