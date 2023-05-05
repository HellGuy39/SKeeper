from domain.model.Group import Group
from presentation.Context import Context
from presentation.ResourceManager import ResourceId


class GroupMenu:

    def __init__(self, context: Context):
        self.__menu_interpreter = context.menu_interpreter
        self.__context = context

    def run(self):
        is_on_screen = True
        while is_on_screen:
            self.__on_start()
            item = self.__menu_interpreter.read(
                self.__context, self.__context.resource_manager.get_localized_string(ResourceId.enter_item), int
            )
            is_on_screen = self.__navigate(item)
        self.__on_finish()

    def __on_start(self):
        self.__menu_interpreter.clear()
        groups = self.__context.get_all_groups_use_case.invoke()

        print(self.__context.resource_manager.get_localized_string(ResourceId.groups))
        print('#' * 20)

        if len(groups) == 0:
            print(self.__context.resource_manager.get_localized_string(ResourceId.no_groups))
        else:
            for group in groups:
                print(group.name)

        self.__menu_interpreter.print_menu(
            {
                '0': self.__context.resource_manager.get_localized_string(ResourceId.back),
                '1': self.__context.resource_manager.get_localized_string(ResourceId.new_group),
                '2': self.__context.resource_manager.get_localized_string(ResourceId.remove_group),
            }
        )

    def __on_finish(self):
        self.__menu_interpreter.clear()

    def __navigate(self, item: int):
        match item:
            case 0:
                return False
            case 1:
                self.__add_group()
                return True
            case 2:
                self.__remove_group()
                return True
            case _:
                return True

    def __add_group(self):
        self.__menu_interpreter.clear()
        self.__menu_interpreter.print_page_title(
            self.__context.resource_manager.get_localized_string(ResourceId.new_group))

        name = self.__menu_interpreter.read_and_format(
            context=self.__context,
            message=self.__context.resource_manager.get_localized_string(ResourceId.group),
        )

        group = Group(
            name=name,
        )

        self.__context.insert_group_use_case.invoke(group)

    def __remove_group(self):
        is_on_screen = True
        while is_on_screen:
            self.__menu_interpreter.clear()
            self.__menu_interpreter.print_page_title(
                self.__context.resource_manager.get_localized_string(ResourceId.remove_group))

            groups = self.__context.get_all_groups_use_case.invoke()

            print(f"0. {self.__context.resource_manager.get_localized_string(ResourceId.back)}")

            if len(groups) == 0:
                print(self.__context.resource_manager.get_localized_string(ResourceId.no_groups))
            else:
                for i in range(len(groups)):
                    print(
                        f"{i + 1}. {groups[i].name} ")

            item = self.__menu_interpreter.read(
                context=self.__context,
                message=self.__context.resource_manager.get_localized_string(ResourceId.enter_item),
                required_type=int
            )
            if item in range(0, len(groups) + 1):
                if item == 0:
                    is_on_screen = False
                else:
                    group = groups[item - 1]
                    self.__context.remove_group_use_case.invoke(group)
                    is_on_screen = False
            else:
                pass
