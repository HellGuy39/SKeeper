from domain.model.Student import Student
from presentation.Container import Container
from presentation.MenuInterpreter import MenuInterpreter


class AddMenu:
    __ADD_MENU = {
        '0': 'Back',
        '1': 'Add'
    }

    def __init__(self, container: Container):
        self.__menu_interpreter = MenuInterpreter()
        self.__container = container
        pass

    def run(self):
        self.__menu_interpreter.clear()
        is_on_screen = True
        while is_on_screen:
            self.__menu_interpreter.print_menu(self.__ADD_MENU)
            item = self.__menu_interpreter.read("Enter item: ", int)
            is_on_screen = self.__navigate(item)
        self.__on_finish()

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
        self.__menu_interpreter.print_page_title("New student")
        fullname = self.__menu_interpreter.read("Enter fullname: ", str)
        birthday = self.__menu_interpreter.read("Enter birthday: ", str)
        address = self.__menu_interpreter.read("Enter address: ", str)
        average = self.__menu_interpreter.read("Enter average: ", float)
        phone = self.__menu_interpreter.read("Enter phone: ", str)
        group = self.__menu_interpreter.read("Enter group: ", str)
        specialty = self.__menu_interpreter.read("Enter specialty: ", str)
        enrollment_order = self.__menu_interpreter.read("Enter enrollment_order: ", str)
        allocation_order = self.__menu_interpreter.read("Enter allocation_order: ", str)
        allocation_reason = self.__menu_interpreter.read("Enter allocation_reason: ", str)
        status = self.__menu_interpreter.read("Enter status: ", str)
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
            allocation_order=allocation_order,
            allocation_reason=allocation_reason,
            status=status,
        )

        self.__container.addStudentUseCase.invoke(student)