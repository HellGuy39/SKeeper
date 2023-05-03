import enum


class LanguageState(enum.Enum):
    ru = 1
    en = 2


def int_to_language_state(value):
    if value == 1:
        return LanguageState.ru
    else:
        return LanguageState.en


class ResourceId(enum.Enum):
    # Global
    back = 1
    enter_item = 2
    enter_value = 3

    # Main
    welcome = 100
    facility = 101
    number_of_students = 102
    add_student = 103
    search = 104
    settings = 105
    exit = 106
    bye_bye = 107

    # Settings
    change_facility_name = 200
    change_language = 201
    new_facility_name = 202
    language = 203

    # Add
    add = 300
    new_student = 301
    fullname = 302
    birthday = 303
    address = 304
    average = 305
    phone = 306
    group = 307
    specialty = 308
    enrollment_order = 309
    status = 310
    id = 311
    allocation_order = 312
    allocation_reason = 313

    # Search
    search_by_fullname = 400
    search_by_id = 401

    # Student list
    results = 500
    nothing_was_found = 501

    # Student menu
    edit = 600
    deduct = 601
    transfer = 602

    # Student edit
    change_fullname = 700
    change_birthday = 701
    change_address = 702
    change_phone = 703

    # Error
    invalid_value = 10000
    value_does_not_match = 10001
    value_should_be_in_range = 10002


class ResourceManager:
    __resources_ru = {
        # Global
        ResourceId.back.value: 'Назад',
        ResourceId.enter_item.value: 'Выберите пункт: ',
        ResourceId.enter_value.value: 'Введите значение',

        # Error
        ResourceId.invalid_value.value: 'Недопустимое значение. Попробуй ещё раз',
        ResourceId.value_does_not_match.value: 'Значение не соответствует необходимому формату',
        ResourceId.value_should_be_in_range.value: 'Значение должно быть в радиусе',

        # Main
        ResourceId.welcome.value: 'Добро пожаловать в',
        ResourceId.facility.value: 'Учреждение',
        ResourceId.number_of_students.value: 'Количество обучающихся',
        ResourceId.add_student.value: 'Добавить студента',
        ResourceId.search.value: 'Поиск',
        ResourceId.settings.value: 'Настройки',
        ResourceId.exit.value: 'Выйти',
        ResourceId.bye_bye.value: 'До свидания!',

        # Settings
        ResourceId.change_facility_name.value: 'Изменить название учреждения',
        ResourceId.change_language.value: 'Изменить язык',
        ResourceId.new_facility_name.value: 'Новое название учреждения',
        ResourceId.language.value: 'Язык',

        # Add
        ResourceId.add.value: 'Добавить',
        ResourceId.new_student.value: 'Новый студент',
        ResourceId.fullname.value: 'Полное имя: ',
        ResourceId.birthday.value: 'Дата рождения (дд.мм.гггг): ',
        ResourceId.address.value: 'Адрес: ',
        ResourceId.average.value: 'Средний балл: ',
        ResourceId.phone.value: 'Телефон: ',
        ResourceId.group.value: 'Группа: ',
        ResourceId.allocation_order.value: 'Приказ об отчислении: ',
        ResourceId.allocation_reason.value: 'Причина отчисления: ',
        ResourceId.specialty.value: 'Специальность: ',
        ResourceId.enrollment_order.value: 'Приказ о зачислении: ',
        ResourceId.status.value: 'Статус (1 - Обучается, 2 - Отчислен, 3 - Переведён): ',
        ResourceId.id.value: 'Идентификатор: ',

        # Search
        ResourceId.search_by_fullname.value: 'Поиск по имени',
        ResourceId.search_by_id.value: 'Поиск по идентификатору',

        # Student list
        ResourceId.results.value: 'Результаты',
        ResourceId.nothing_was_found.value: 'Ничего не нашлось',

        # Student menu
        ResourceId.edit.value: 'Редактировать',
        ResourceId.deduct.value: 'Отчислить',
        ResourceId.transfer.value: 'Перевести',

        # Student edit
        ResourceId.change_birthday.value: 'Изменить дату рождения',
        ResourceId.change_fullname.value: 'Изменить полное имя',
        ResourceId.change_address.value: 'Изменить адрес',
        ResourceId.change_phone.value: 'Изменить телефон',
    }

    __resources_en = {
        ResourceId.back.value: "Back",
        ResourceId.enter_item.value: 'Enter item: ',
        ResourceId.enter_value.value: 'Enter value: ',

        # Main
        ResourceId.welcome.value: 'Welcome to',
        ResourceId.facility.value: 'Facility',
        ResourceId.number_of_students.value: 'Number of students',
        ResourceId.add_student.value: 'Add student',
        ResourceId.search.value: 'Search',
        ResourceId.settings.value: 'Settings',
        ResourceId.exit.value: 'Exit',
        ResourceId.bye_bye.value: 'Bye-bye',

        # Settings
        ResourceId.change_facility_name.value: 'Change facility name',
        ResourceId.change_language.value: 'Change language',
        ResourceId.new_facility_name.value: 'New facility name',
        ResourceId.language.value: 'Language',

        # Add
        ResourceId.add.value: 'Add',
        ResourceId.new_student.value: 'New student',
        ResourceId.fullname.value: 'Fullname: ',
        ResourceId.birthday.value: 'Birthday (dd.mm.yyyy): ',
        ResourceId.address.value: 'Address: ',
        ResourceId.average.value: 'Average score: ',
        ResourceId.phone.value: 'Phone: ',
        ResourceId.group.value: 'Group: ',
        ResourceId.allocation_order.value: 'Allocation order: ',
        ResourceId.allocation_reason.value: 'Allocation reason: ',
        ResourceId.specialty.value: 'Specialty: ',
        ResourceId.enrollment_order.value: 'Enrollment order: ',
        ResourceId.status.value: 'Status (1 - Study, 2 - Enrolled, 3 - Transferred): ',
        ResourceId.id.value: 'Id: ',

        # Search
        ResourceId.search_by_fullname.value: 'Search by fullname',
        ResourceId.search_by_id.value: 'Search by id',

        # Student list
        ResourceId.results.value: 'Results',
        ResourceId.nothing_was_found.value: 'Nothing was found',

        # Student menu
        ResourceId.edit.value: 'Edit',
        ResourceId.deduct.value: 'Deduct',
        ResourceId.transfer.value: 'Transfer',

        # Student edit
        ResourceId.change_birthday.value: 'Change birthday',
        ResourceId.change_fullname.value: 'Change fullname',
        ResourceId.change_address.value: 'Change address',
        ResourceId.change_phone.value: 'Change phone',

        # Error
        ResourceId.invalid_value.value: 'Invalid value. Try Again',
        ResourceId.value_does_not_match.value: 'Value does not match the required format',
        ResourceId.value_should_be_in_range.value: 'The value should be in range',

    }

    def __init__(self, language_state):
        self.__language = language_state

    def set_language(self, language_state: LanguageState):
        self.__language = language_state

    def get_localized_string(self, id: ResourceId) -> str:
        if self.__language is LanguageState.ru:
            return self.__resources_ru[id.value]
        else:
            return self.__resources_en[id.value]
