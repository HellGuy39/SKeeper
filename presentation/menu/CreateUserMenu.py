from domain.model.User import int_to_user_role, User
from presentation.Context import Context
from presentation.resource.ResourceId import ResourceId


class CreateUserMenu:

    def __init__(self, context: Context):
        self.__context = context
        self.__menu_interpreter = context.menu_interpreter

    def run(self, is_first_user):
        is_on_screen = True
        while is_on_screen:
            self.__on_start()

            if is_first_user:
                print(self.__context.resource_manager.get_localized_string(ResourceId.first_user_message))

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
            if is_first_user:
                role_value = 1
            else:
                role_value = self.__menu_interpreter.read_ranged_int(
                    context=self.__context,
                    message="Enter role (1 - Edit, 2 - Readonly): ",
                    start=1,
                    end=2
                )

            user = User(
                login=login,
                password=password,
                role=int_to_user_role(role_value)
            )

            self.__context.insert_user_use_case.invoke(user)
            is_on_screen = False

        self.__on_finish()

    def __on_start(self):
        self.__menu_interpreter.clear()
        self.__menu_interpreter.print_page_title("New user")

    def __on_finish(self):
        self.__menu_interpreter.clear()
