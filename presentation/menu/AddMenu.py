from domain.model.Student import Student, int_to_student_status
from presentation.Context import Context
from presentation.ResourceManager import ResourceId


class AddMenu:

    def __init__(self, context: Context):
        self.__context = context
        self.__menu_interpreter = context.menu_interpreter

    def run(self):
        self.__menu_interpreter.clear()
        is_on_screen = True
        while is_on_screen:
            self.__on_start()
            self.__menu_interpreter.print_menu(self.__ADD_MENU)
            item = self.__menu_interpreter.read(
                self.__context, self.__context.resource_manager.get_localized_string(ResourceId.enter_item), int
            )
            is_on_screen = self.__navigate(item)
        self.__on_finish()

    def __on_start(self):
        self.__ADD_MENU = {
            '0': self.__context.resource_manager.get_localized_string(ResourceId.back),
            '1': self.__context.resource_manager.get_localized_string(ResourceId.add_student)
        }

    def __on_finish(self):
        self.__menu_interpreter.clear()

    def __navigate(self, item: int):
        if item == 0:
            return False
        elif item == 1:
            self.__add_student()
            return True
        else:
            self.__menu_interpreter.clear()
            return True

    def __add_student(self):
        self.__menu_interpreter.clear()
        self.__menu_interpreter.print_page_title(
            self.__context.resource_manager.get_localized_string(ResourceId.new_student)
        )
        fullname = self.__menu_interpreter.read(
            self.__context, self.__context.resource_manager.get_localized_string(ResourceId.fullname), str
        )
        birthday = self.__menu_interpreter.read_with_regex(
            context=self.__context,
            message=self.__context.resource_manager.get_localized_string(ResourceId.birthday),
            regex=r'\d{2}.\d{2}.\d{4}'
        )
        address = self.__menu_interpreter.read(
            self.__context, self.__context.resource_manager.get_localized_string(ResourceId.address), str
        )
        average = self.__menu_interpreter.read(
            self.__context, self.__context.resource_manager.get_localized_string(ResourceId.average), float
        )
        phone = self.__menu_interpreter.read(
            self.__context, self.__context.resource_manager.get_localized_string(ResourceId.phone), str
        )
        group = self.__menu_interpreter.read(
            self.__context, self.__context.resource_manager.get_localized_string(ResourceId.group), str
        )
        specialty = self.__menu_interpreter.read(
            self.__context, self.__context.resource_manager.get_localized_string(ResourceId.specialty), str
        )
        enrollment_order = self.__menu_interpreter.read(
            self.__context, self.__context.resource_manager.get_localized_string(ResourceId.enrollment_order), str
        )
        status = self.__menu_interpreter.read_ranged_int(
            context=self.__context,
            message=self.__context.resource_manager.get_localized_string(ResourceId.status),
            start=1,
            end=3
        )
        self.__menu_interpreter.clear()

        student = Student(
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
            status=int_to_student_status(status),
        )

        self.__context.add_student_use_case.invoke(student)
