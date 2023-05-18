from presentation.Context import Context
from presentation.menu.SubjectMenu import SubjectMenu
from presentation.resource.ResourceId import ResourceId


class JournalMenu:

    def __init__(self, context: Context):
        self.__menu_interpreter = context.menu_interpreter
        self.__context = context

    def __on_start(self):
        self.__menu_interpreter.clear()
        self.__menu_interpreter.print_menu_with_title(
            title=self.__context.resource_manager.get_localized_string(ResourceId.journal),
            menu={
                '0': self.__context.resource_manager.get_localized_string(ResourceId.back),
                '1': self.__context.resource_manager.get_localized_string(ResourceId.subjects),
                '2': self.__context.resource_manager.get_localized_string(ResourceId.add_subject),
                '3': self.__context.resource_manager.get_localized_string(ResourceId.remove_subject),
            }
        )

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

    def __navigate(self, item: int):
        match item:

            case 0:
                return False

            case 1:
                self.__subject_list()
                return True

            case 2:
                self.__add_subject()
                return True

            case 3:
                self.__remove_subject()
                return True

            case _:
                self.__menu_interpreter.clear()
                return True

    def __on_finish(self):
        self.__menu_interpreter.clear()

    def __remove_subject(self):
        self.__menu_interpreter.clear()
        self.__menu_interpreter.print_page_title(
            self.__context.resource_manager.get_localized_string(ResourceId.remove_subject)
        )

        subjects = self.__context.get_all_subjects_use_case.invoke()

        print(f"0. {self.__context.resource_manager.get_localized_string(ResourceId.back)}")

        if len(subjects) == 0:
            print(self.__context.resource_manager.get_localized_string(ResourceId.you_do_not_have_any_subjects))
        else:
            for i in range(len(subjects)):
                print(f"{i + 1}. {subjects[i]}")

        item = self.__menu_interpreter.read(
            context=self.__context,
            message=self.__context.resource_manager.get_localized_string(ResourceId.enter_item),
            required_type=int
        )
        if item in range(0, len(subjects) + 1):
            if item == 0:
                pass
            else:
                subject = subjects[item - 1]
                self.__context.remove_subject_use_case.invoke(subject)
        else:
            pass

    def __add_subject(self):
        self.__menu_interpreter.clear()
        self.__menu_interpreter.print_page_title(
            self.__context.resource_manager.get_localized_string(ResourceId.add_subject)
        )
        subject_name = self.__menu_interpreter.read(
            context=self.__context,
            message=self.__context.resource_manager.get_localized_string(ResourceId.enter_subject_name),
            required_type=str
        )
        self.__context.insert_subject_use_case.invoke(subject_name)

    def __subject_list(self):
        self.__menu_interpreter.clear()
        self.__menu_interpreter.print_page_title(
            self.__context.resource_manager.get_localized_string(ResourceId.subjects)
        )

        subjects = self.__context.get_all_subjects_use_case.invoke()

        print(f"0. {self.__context.resource_manager.get_localized_string(ResourceId.back)}")

        if len(subjects) == 0:
            print(self.__context.resource_manager.get_localized_string(ResourceId.you_do_not_have_any_subjects))
        else:
            for i in range(len(subjects)):
                print(f"{i + 1}. {subjects[i]}")

        item = self.__menu_interpreter.read(
            context=self.__context,
            message=self.__context.resource_manager.get_localized_string(ResourceId.enter_item),
            required_type=int
        )
        if item in range(0, len(subjects) + 1):
            if item == 0:
                pass
            else:
                subject = subjects[item - 1]
                SubjectMenu(self.__context).run(subject)
        else:
            pass
