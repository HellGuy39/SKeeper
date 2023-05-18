import json
from dataclasses import replace

from presentation.Context import Context
from presentation.resource.ResourceId import ResourceId


class SubjectEventEditMenu:

    def __init__(self, context: Context):
        self.__event_id = None
        self.__subject = None
        self.__menu_interpreter = context.menu_interpreter
        self.__context = context

    def __on_start(self):
        self.__menu_interpreter.clear()
        subject_event = self.__context.get_subject_event_by_id_use_case.invoke(self.__subject, self.__event_id)

        self.__menu_interpreter.print_divider()

        marks = json.loads(subject_event.marks)

        for key, value in marks.items():
            student = self.__context.get_student_by_id_use_case.invoke(key)
            print(f"{student.fullname} - {value}")

        self.__menu_interpreter.print_menu(
            {
                '0': self.__context.resource_manager.get_localized_string(ResourceId.back),
                '1': self.__context.resource_manager.get_localized_string(ResourceId.add_mark),
            }
        )

    def run(self, subject: str, event_id: int):
        self.__subject = subject
        self.__event_id = event_id

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
                self.__add_mark()
                return True

            case _:
                self.__menu_interpreter.clear()
                return True

    def __on_finish(self):
        self.__menu_interpreter.clear()

    def __add_mark(self):
        self.__menu_interpreter.clear()

        self.__menu_interpreter.print_page_title(
            self.__context.resource_manager.get_localized_string(ResourceId.add_mark)
        )

        ids = self.__context.get_all_student_ids_use_case.invoke()
        student_id = self.__menu_interpreter.read_existed_in_list(
            context=self.__context,
            message=self.__context.resource_manager.get_localized_string(ResourceId.enter_student_id),
            required_type=int,
            value_list=ids,
            error_message=self.__context.resource_manager.get_localized_string(ResourceId.student_with_this_id_does_not_exist),
        )
        mark = self.__menu_interpreter.read(
            context=self.__context,
            message=self.__context.resource_manager.get_localized_string(ResourceId.enter_mark),
            required_type=int
        )
        subject_event = self.__context.get_subject_event_by_id_use_case.invoke(self.__subject, self.__event_id)
        marks = json.loads(subject_event.marks)
        marks.update({student_id: mark})
        edited_marks = json.dumps(marks)

        edited_subject_event = replace(subject_event, marks=edited_marks)

        self.__context.update_subject_event_use_case.invoke(self.__subject, edited_subject_event)
