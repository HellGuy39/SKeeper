from domain.model.Student import Student, int_to_student_status, StudentStatus
from presentation.Context import Context
from presentation.ResourceManager import ResourceId


class AddMenu:

    def __init__(self, context: Context):
        self.__context = context
        self.__menu_interpreter = context.menu_interpreter

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
        self.__ADD_MENU = {
            '0': self.__context.resource_manager.get_localized_string(ResourceId.back),
            '1': self.__context.resource_manager.get_localized_string(ResourceId.add_student)
        }
        self.__menu_interpreter.print_menu(self.__ADD_MENU)

    def __on_finish(self):
        self.__menu_interpreter.clear()

    def __navigate(self, item: int):
        match item:
            case 0:
                return False
            case 1:
                self.__add_student()
                return True
            case _:
                return True

    def __add_student(self):
        self.__menu_interpreter.clear()
        self.__menu_interpreter.print_page_title(
            self.__context.resource_manager.get_localized_string(ResourceId.new_student)
        )

        ids = self.__context.get_all_student_ids_use_case.invoke()
        id = self.__menu_interpreter.read_not_existed_in_list(
            context=self.__context,
            message=self.__context.resource_manager.get_localized_string(ResourceId.id),
            required_type=int,
            value_list=ids,
            error_message=self.__context.resource_manager.get_localized_string(
                ResourceId.student_with_this_id_is_already_exist)
        )

        fullname = self.__menu_interpreter.read_and_format(
            context=self.__context,
            message=self.__context.resource_manager.get_localized_string(ResourceId.fullname),
        )
        birthday = self.__menu_interpreter.read_with_regex(
            context=self.__context,
            message=self.__context.resource_manager.get_localized_string(ResourceId.birthday),
            regex=r'\d{2}.\d{2}.\d{4}'
        )
        address = self.__menu_interpreter.read(
            context=self.__context,
            message=self.__context.resource_manager.get_localized_string(ResourceId.address),
            required_type=str
        )
        average = self.__menu_interpreter.read(
            context=self.__context,
            message=self.__context.resource_manager.get_localized_string(ResourceId.average),
            required_type=float
        )
        phone = self.__menu_interpreter.read(
            context=self.__context,
            message=self.__context.resource_manager.get_localized_string(ResourceId.phone),
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
            error_message=self.__context.resource_manager.get_localized_string(
                ResourceId.this_specialty_does_not_exist)
        )
        enrollment_order = self.__menu_interpreter.read(
            context=self.__context,
            message=self.__context.resource_manager.get_localized_string(ResourceId.enrollment_order),
            required_type=str
        )

        student = Student(
            id=id,
            fullname=fullname,
            birthday=birthday,
            address=address,
            average=average,
            phone=phone,
            group=group,
            specialty=specialty,
            enrollment_order=enrollment_order,
            allocation_order="",
            allocation_reason="",
            status=StudentStatus.Study,
        )

        self.__context.add_student_use_case.invoke(student)
