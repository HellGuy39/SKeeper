import enum


class ResourceId(enum.Enum):
    # Global
    back = 1
    enter_item = 2
    enter_value = 3
    exit_program = 4

    # Main
    welcome = 100
    facility = 101
    number_of_students = 102
    add_student = 103
    search = 104
    settings = 105
    exit = 106
    bye_bye = 107
    groups = 108
    specialties = 109
    sign_as = 110
    change_user = 111
    user_manager = 112

    # Settings
    change_facility_name = 200
    change_language = 201
    new_facility_name = 202
    language = 203
    color_schema = 204
    change_color_schema = 205
    color_list = 206
    language_list = 207

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
    search_by_group = 402
    search_by_specialty = 403
    search_by_status = 404

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
    student_with_this_id_is_already_exist = 10003
    this_group_does_not_exist = 10004
    this_specialty_does_not_exist = 10005

    # Specialty menu
    no_specialties = 800
    new_specialty = 801
    remove_specialty = 802

    # Group menu
    no_groups = 900
    new_group = 901
    remove_group = 902

    # Create user menu
    first_user_message = 1000

    # Login menu
    authorization = 1100
    enter_login = 1101
    enter_password = 1102

    # User manager menu
    list_of_users = 1300
    add_user = 1301
    remove_user = 1302
