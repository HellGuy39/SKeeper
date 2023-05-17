from presentation.resource.ResourceId import ResourceId

resources_en = {
    # Global
    ResourceId.back.value: "Back",
    ResourceId.enter_item.value: 'Enter item: ',
    ResourceId.enter_value.value: 'Enter value: ',
    ResourceId.exit_program.value: 'Exit program',

    # Main
    ResourceId.welcome.value: 'Welcome to',
    ResourceId.facility.value: 'Facility',
    ResourceId.number_of_students.value: 'Number of students',
    ResourceId.add_student.value: 'Add student',
    ResourceId.search.value: 'Search',
    ResourceId.settings.value: 'Settings',
    ResourceId.exit.value: 'Exit',
    ResourceId.bye_bye.value: 'Bye-bye',
    ResourceId.groups.value: 'Groups',
    ResourceId.specialties.value: 'Specialties',
    ResourceId.sign_as.value: 'Sign as',
    ResourceId.change_user.value: 'Change user',
    ResourceId.user_manager.value: 'User manager',

    # Settings
    ResourceId.change_facility_name.value: 'Change facility name',
    ResourceId.change_language.value: 'Change language',
    ResourceId.new_facility_name.value: 'New facility name',
    ResourceId.language.value: 'Language',
    ResourceId.color_list.value: "0 - Default\n" +
                           "1 - Gray & Dark Blue\n" +
                           "2 - Green & White\n" +
                           "3 - White & Black\n" +
                           "4 - White & Dark Blue\n" +
                           "5 - Dark Blue & White\n" +
                           "6 - Dark Green & Black\n" +
                           "7 - Dark Yellow & Dark Blue",
    ResourceId.language_list.value: "1 - Russian\n" +
                              "2 - English",
    ResourceId.color_schema.value: 'Color schema',
    ResourceId.change_color_schema.value: 'Change color schema',

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
    ResourceId.search_by_group.value: 'Search by group',
    ResourceId.search_by_specialty.value: 'Search by specialty',
    ResourceId.search_by_status.value: 'Search by status',

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

    # Specialty menu
    ResourceId.no_specialties.value: 'No specialties',
    ResourceId.new_specialty.value: 'New specialty',
    ResourceId.remove_specialty.value: 'Remove specialty',

    # Group menu
    ResourceId.no_groups.value: 'No groups',
    ResourceId.new_group.value: 'New group',
    ResourceId.remove_group.value: 'Remove group',

    # Create user menu
    ResourceId.first_user_message.value: '* The first user will be created with the highest access level by default',

    # Login menu
    ResourceId.authorization.value: 'Authorization',
    ResourceId.enter_login.value: 'Enter login: ',
    ResourceId.enter_password.value: 'Enter password: ',

    # User manager menu
    ResourceId.list_of_users.value: 'List of users',
    ResourceId.add_user.value: 'Add user',
    ResourceId.remove_user.value: 'Remove user',
}
