from dataclasses import replace

from presentation.Context import Context
from presentation.ResourceManager import ResourceId, int_to_language_state


class SettingsMenu:

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
        self.__menu_interpreter.print_menu(
            {
                '0': self.__context.resource_manager.get_localized_string(ResourceId.back),
                '1': self.__context.resource_manager.get_localized_string(ResourceId.change_facility_name),
                '2': self.__context.resource_manager.get_localized_string(ResourceId.change_language)
            }
        )

    def __on_finish(self):
        self.__menu_interpreter.clear()

    def __navigate(self, item: int):
        if item == 0:
            return False
        elif item == 1:
            self.__change_facility_name()
            return True
        elif item == 2:
            self.__change_language()
            return True
        else:
            self.__menu_interpreter.clear()
            return True

    def __change_facility_name(self):
        self.__menu_interpreter.clear()
        self.__menu_interpreter.print_page_title(
            self.__context.resource_manager.get_localized_string(ResourceId.new_facility_name)
        )
        name_of_facility = self.__menu_interpreter.read(self.__context, "> ", str)

        settings = self.__context.get_application_settings_use_case.invoke()
        edited_settings = replace(settings, nameOfFacility=name_of_facility)
        self.__context.save_application_settings_use_case.invoke(edited_settings)

        self.__menu_interpreter.clear()

    def __change_language(self):
        self.__menu_interpreter.clear()
        self.__menu_interpreter.print_page_title(
            self.__context.resource_manager.get_localized_string(ResourceId.language)
        )
        value = self.__menu_interpreter.read_ranged_int(
            context=self.__context,
            message=f"{self.__context.resource_manager.get_localized_string(ResourceId.enter_value)} "
            f"(1 - Русский, 2 - English): ",
            start=1,
            end=2
        )
        language_state = int_to_language_state(value)

        settings = self.__context.get_application_settings_use_case.invoke()
        edited_settings = replace(settings, language=language_state)
        self.__context.save_application_settings_use_case.invoke(edited_settings)

        self.__context.resource_manager.set_language(language_state)

        self.__menu_interpreter.clear()
