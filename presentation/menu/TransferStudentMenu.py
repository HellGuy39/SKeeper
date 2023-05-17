from dataclasses import replace

from domain.model.Student import StudentStatus
from presentation.Context import Context
from presentation.resource.ResourceId import ResourceId


class TransferStudentMenu:

    def __init__(self, context: Context):
        self.__student_id = None
        self.__menu_interpreter = context.menu_interpreter
        self.__context = context

    def __on_start(self):
        self.__menu_interpreter.clear()
        self.__TRANSFER_STUDENT_MENU = {
            '0': self.__context.resource_manager.get_localized_string(ResourceId.back),
            '1': self.__context.resource_manager.get_localized_string(ResourceId.transfer),
        }

    def run(self, student_id: int):
        self.__student_id = student_id
        is_on_screen = True
        while is_on_screen:
            self.__on_start()
            self.__menu_interpreter.print_menu(self.__TRANSFER_STUDENT_MENU)
            item = self.__menu_interpreter.read(
                self.__context, self.__context.resource_manager.get_localized_string(ResourceId.enter_item), int
            )
            is_on_screen = self.__navigate(item)
        self.__on_finish()

    def __on_finish(self):
        self.__menu_interpreter.clear()

    def __navigate(self, item: int):
        if item == 0:
            return False
        elif item == 1:
            self.__transfer()
            return False
        else:
            self.__menu_interpreter.clear()
            return True

    def __transfer(self):
        self.__menu_interpreter.clear()
        self.__menu_interpreter.print_page_title(
            self.__context.resource_manager.get_localized_string(ResourceId.transfer)
        )
        student = self.__context.get_student_by_id_use_case.invoke(self.__student_id)

        allocation_order = self.__menu_interpreter.read(
            context=self.__context,
            message=self.__context.resource_manager.get_localized_string(ResourceId.allocation_order),
            required_type=str
        )
        allocation_reason = self.__menu_interpreter.read(
            context=self.__context,
            message=self.__context.resource_manager.get_localized_string(ResourceId.allocation_reason),
            required_type=str
        )

        groups = self.__context.get_all_groups_use_case.invoke()
        group_names = []
        for group in groups:
            group_names.append(group.name)

        group = self.__menu_interpreter.read_existed_in_list(
            context=self.__context,
            message=self.__context.resource_manager.get_localized_string(ResourceId.group),
            required_type=str,
            value_list=group_names,
            error_message=self.__context.resource_manager.get_localized_string(ResourceId.this_group_does_not_exist)
        )

        specialties = self.__context.get_all_specialty_use_case.invoke()
        specialty_names = []
        for specialty in specialties:
            specialty_names.append(specialty.name)

        specialty = self.__menu_interpreter.read_existed_in_list(
            context=self.__context,
            message=self.__context.resource_manager.get_localized_string(ResourceId.specialty),
            required_type=str,
            value_list=specialty_names,
            error_message=self.__context.resource_manager.get_localized_string(ResourceId.this_specialty_does_not_exist)
        )

        old_student = replace(
            student,
            allocation_order=allocation_order,
            allocation_reason=allocation_reason,
            status=StudentStatus.Transferred
        )
        new_student = replace(student, id=0, specialty=specialty, group=group)

        self.__context.edit_student_use_case.invoke(old_student)
        self.__context.add_student_use_case.invoke(new_student)
        self.__menu_interpreter.clear()
