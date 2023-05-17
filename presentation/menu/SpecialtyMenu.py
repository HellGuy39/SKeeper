from domain.model.Specialty import Specialty
from presentation.Context import Context
from presentation.resource.ResourceId import ResourceId


class SpecialtyMenu:

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
        specialties = self.__context.get_all_specialty_use_case.invoke()

        print(self.__context.resource_manager.get_localized_string(ResourceId.specialties))
        print('#' * 20)

        if len(specialties) == 0:
            print(self.__context.resource_manager.get_localized_string(ResourceId.no_specialties))
        else:
            for group in specialties:
                print(group.name)

        self.__menu_interpreter.print_menu(
            {
                '0': self.__context.resource_manager.get_localized_string(ResourceId.back),
                '1': self.__context.resource_manager.get_localized_string(ResourceId.new_specialty),
                '2': self.__context.resource_manager.get_localized_string(ResourceId.remove_specialty),
            }
        )

    def __on_finish(self):
        self.__menu_interpreter.clear()

    def __navigate(self, item: int):
        match item:
            case 0:
                return False
            case 1:
                self.__add_specialty()
                return True
            case 2:
                self.__remove_specialty()
                return True
            case _:
                return True

    def __add_specialty(self):
        self.__menu_interpreter.clear()
        self.__menu_interpreter.print_page_title(
            self.__context.resource_manager.get_localized_string(ResourceId.new_specialty)
        )

        name = self.__menu_interpreter.read_and_format(
            context=self.__context,
            message=self.__context.resource_manager.get_localized_string(ResourceId.specialty),
        )

        specialty = Specialty(
            name=name,
        )

        self.__context.insert_specialty_use_case.invoke(specialty)

    def __remove_specialty(self):
        is_on_screen = True
        while is_on_screen:
            self.__menu_interpreter.clear()
            self.__menu_interpreter.print_page_title(
                self.__context.resource_manager.get_localized_string(ResourceId.remove_specialty)
            )

            specialties = self.__context.get_all_specialty_use_case.invoke()

            print(f"0. {self.__context.resource_manager.get_localized_string(ResourceId.back)}")

            if len(specialties) == 0:
                print(
                    self.__context.resource_manager.get_localized_string(ResourceId.no_specialties)
                )
            else:
                for i in range(len(specialties)):
                    print(
                        f"{i + 1}. {specialties[i].name} ")

            item = self.__menu_interpreter.read(
                context=self.__context,
                message=self.__context.resource_manager.get_localized_string(ResourceId.enter_item),
                required_type=int
            )
            if item in range(0, len(specialties) + 1):
                if item == 0:
                    is_on_screen = False
                else:
                    specialty = specialties[item - 1]
                    self.__context.remove_specialty_use_case.invoke(specialty)
                    is_on_screen = False
            else:
                pass
