from domain.model.SubjectEvent import SubjectEvent
from presentation.Context import Context
from presentation.menu.SubjectEventEditMenu import SubjectEventEditMenu
from presentation.resource.ResourceId import ResourceId


class SubjectMenu:

    def __init__(self, context: Context):
        self.__subject = None
        self.__menu_interpreter = context.menu_interpreter
        self.__context = context

    def __on_start(self):
        self.__menu_interpreter.clear()
        self.__menu_interpreter.print_menu_with_title(
            title=self.__subject,
            menu={
                '0': self.__context.resource_manager.get_localized_string(ResourceId.back),
                '1': self.__context.resource_manager.get_localized_string(ResourceId.events),
                '2': self.__context.resource_manager.get_localized_string(ResourceId.add_event),
                '3': self.__context.resource_manager.get_localized_string(ResourceId.remove_event),
            }
        )

    def run(self, subject: str):
        self.__subject = subject
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

        if item == 0:
            return False

        elif item == 1:
            self.__event_list()
            return True

        elif item == 2:
            self.__add_event()
            return True

        elif item == 3:
            self.__remove_event()
            return True

        else:
            self.__menu_interpreter.clear()
            return True

    def __on_finish(self):
        self.__menu_interpreter.clear()

    def __event_list(self):
        self.__menu_interpreter.clear()
        self.__menu_interpreter.print_page_title(
            self.__context.resource_manager.get_localized_string(ResourceId.events)
        )

        subject_events = self.__context.get_all_subject_events_use_case.invoke(self.__subject)

        print(f"0. {self.__context.resource_manager.get_localized_string(ResourceId.back)}")

        if len(subject_events) == 0:
            print(
                self.__context.resource_manager.get_localized_string(ResourceId.you_do_not_have_any_events)
            )
        else:
            for i in range(len(subject_events)):
                print(f"{i + 1}. {subject_events[i].date} | {subject_events[i].name_of_event}")

        item = self.__menu_interpreter.read(
            context=self.__context,
            message=self.__context.resource_manager.get_localized_string(ResourceId.enter_item),
            required_type=int
        )
        if item in range(0, len(subject_events) + 1):
            if item == 0:
                pass
            else:
                subject_event = subject_events[item - 1]
                SubjectEventEditMenu(self.__context).run(self.__subject, subject_event.id)
        else:
            pass

    def __add_event(self):
        self.__menu_interpreter.clear()

        self.__menu_interpreter.print_page_title(
            self.__context.resource_manager.get_localized_string(ResourceId.add_event)
        )

        event_name = self.__menu_interpreter.read(
            context=self.__context,
            message=self.__context.resource_manager.get_localized_string(ResourceId.enter_event_name),
            required_type=str
        )
        date = self.__menu_interpreter.read_with_regex(
            context=self.__context,
            message=self.__context.resource_manager.get_localized_string(ResourceId.enter_event_date),
            regex=r'\d{2}.\d{2}.\d{4}'
        )

        subject_event = SubjectEvent(
            name_of_event=event_name,
            date=date,
            marks="{}"
        )

        self.__context.insert_subject_event_use_case.invoke(self.__subject, subject_event)

    def __remove_event(self):
        self.__menu_interpreter.clear()
        self.__menu_interpreter.print_page_title(
            self.__context.resource_manager.get_localized_string(ResourceId.remove_event)
        )

        subject_events = self.__context.get_all_subject_events_use_case.invoke(self.__subject)

        print(f"0. {self.__context.resource_manager.get_localized_string(ResourceId.back)}")

        if len(subject_events) == 0:
            print(
                self.__context.resource_manager.get_localized_string(ResourceId.you_do_not_have_any_events)
            )
        else:
            for i in range(len(subject_events)):
                print(f"{i + 1}. {subject_events[i].date} | {subject_events[i].name_of_event}")

        item = self.__menu_interpreter.read(
            context=self.__context,
            message=self.__context.resource_manager.get_localized_string(ResourceId.enter_item),
            required_type=int
        )
        if item in range(0, len(subject_events) + 1):
            if item == 0:
                pass
            else:
                subject_event = subject_events[item - 1]
                self.__context.remove_subject_event_use_case.invoke(self.__subject, subject_event)
        else:
            pass
