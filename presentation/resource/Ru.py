from presentation.resource.ResourceId import ResourceId

resources_ru = {
    # Global
    ResourceId.back.value: 'Назад',
    ResourceId.enter_item.value: 'Выберите пункт: ',
    ResourceId.enter_value.value: 'Введите значение',
    ResourceId.exit_program.value: 'Выйти из программы',

    # Error
    ResourceId.invalid_value.value: 'Недопустимое значение. Попробуй ещё раз',
    ResourceId.value_does_not_match.value: 'Значение не соответствует необходимому формату',
    ResourceId.value_should_be_in_range.value: 'Значение должно быть в радиусе',
    ResourceId.student_with_this_id_is_already_exist.value: 'Студент с таким идентификатором уже существует',
    ResourceId.this_group_does_not_exist.value: 'Такой группы не существует',
    ResourceId.this_specialty_does_not_exist.value: 'Такой специальности не существует',

    # Main
    ResourceId.welcome.value: 'Добро пожаловать в',
    ResourceId.facility.value: 'Учреждение',
    ResourceId.number_of_students.value: 'Количество обучающихся',
    ResourceId.add_student.value: 'Добавить студента',
    ResourceId.search.value: 'Поиск',
    ResourceId.settings.value: 'Настройки',
    ResourceId.exit.value: 'Выйти',
    ResourceId.bye_bye.value: 'До свидания!',
    ResourceId.groups.value: 'Группы',
    ResourceId.specialties.value: 'Специальности',
    ResourceId.sign_as.value: 'Войти как',
    ResourceId.change_user.value: 'Сменить пользователя',
    ResourceId.user_manager.value: 'Менеджер пользователей',

    # Settings
    ResourceId.change_facility_name.value: 'Изменить название учреждения',
    ResourceId.change_language.value: 'Изменить язык',
    ResourceId.new_facility_name.value: 'Новое название учреждения',
    ResourceId.color_schema.value: 'Цветовая схема',
    ResourceId.change_color_schema.value: 'Изменить цветовую схему',
    ResourceId.language.value: 'Язык',
    ResourceId.color_list.value: "0 - По умолчанию\n" +
                           "1 - Серый и Тёмно-синий\n" +
                           "2 - Зелёный и Белый\n" +
                           "3 - Белый и Чёрный\n" +
                           "4 - Белый и Тёмно-синий\n" +
                           "5 - Тёмно-синий и Белый\n" +
                           "6 - Тёмно-зелёный и Чёрный\n" +
                           "7 - Тёмно-жёлтый и Тёмно-синий",
    ResourceId.language_list.value: "1 - Русский\n" +
                              "2 - Английский",
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
    ResourceId.search_by_group.value: 'Поиск по группе',
    ResourceId.search_by_specialty.value: 'Поиск по специальности',
    ResourceId.search_by_status.value: 'Поиск по статусу',

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

    # Specialty menu
    ResourceId.no_specialties.value: 'Нет специальностей',
    ResourceId.new_specialty.value: 'Новая специальность',
    ResourceId.remove_specialty.value: 'Удалить специальность',

    # Group menu
    ResourceId.no_groups.value: 'Нет групп',
    ResourceId.new_group.value: 'Новая группа',
    ResourceId.remove_group.value: 'Удалить группу',

    # Create user menu
    ResourceId.first_user_message.value: '* Первый пользователь по умолчанию будет создан с наивысшим уровнем доступа',

    # Login menu
    ResourceId.authorization.value: 'Авторизация',
    ResourceId.enter_login.value: 'Введите логин: ',
    ResourceId.enter_password.value: 'Введите пароль: ',

    # User manager menu
    ResourceId.list_of_users.value: 'Список пользователей',
    ResourceId.add_user.value: 'Добавить пользователя',
    ResourceId.remove_user.value: 'Удалить пользователя',

    # Journal
    ResourceId.journal.value: 'Журнал',
    ResourceId.subjects.value: 'Предметы',
    ResourceId.add_subject.value: 'Добавить предмет',
    ResourceId.remove_subject.value: 'Удалить предмет',
    ResourceId.you_do_not_have_any_subjects.value: "У вас нет никаких предметов",
    ResourceId.enter_subject_name.value: 'Введите имя предмета: ',

    # Subject
    ResourceId.events.value: 'События',
    ResourceId.add_event.value: 'Добавить событие',
    ResourceId.remove_event.value: 'Удалить событие',
    ResourceId.you_do_not_have_any_events.value: "У вас нет никаких событий",
    ResourceId.enter_event_name.value: 'Введите имя события: ',
    ResourceId.enter_event_date.value: 'Введите дату события (дд.мм.гггг): ',

    # Subject event edit
    ResourceId.add_mark.value: 'Добавить оценку',
    ResourceId.enter_student_id: 'Введите идентификатор студента: ',
    ResourceId.student_with_this_id_does_not_exist: "Студента с данным идентификатором не сущесвует",
    ResourceId.enter_mark.value: 'Введите оценку: '

}
