registration_page_locators = {
    'registration_form': {
        'first_name': 'customer.firstName',
        'last_name': 'customer.lastName',
        'address': 'customer.address.street',
        'city': 'customer.address.city',
        'state': 'customer.address.state',
        'zip_code': 'customer.address.zipCode',
        'phone': 'customer.phoneNumber',
        'ssn': 'customer.ssn',
        'username': 'customer.username',
        'password': 'customer.password',
        'confirm_password': 'repeatedPassword'
    },

    'login_form': {
        'username': 'username',
        'password': 'password'
    },

    'registration_button': 'Register',
    'login_button': 'Log In'
}
