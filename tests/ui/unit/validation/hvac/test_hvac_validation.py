from core.utilities.generators import gen_long_email, gen_random_persons
from tests.ui.e2e.hvac.hvac_page_methods import perform_user_path

invalid_email_and_errors = [('a@s.i', 'Email address must be at least 6 characters long.'),
                            ('asdssss', 'Must be a valid email address. Example: name@website.com.'),
                            (gen_long_email(256), 'Email address can’t be longer than 255 characters.'),
                            (r'!@#$%^&*()_+`~/\.,', 'Must be a valid email address. Example: name@website.com.'),
                            ('asfssda.com', 'Must be a valid email address. Example: name@website.com.'),
                            ('', 'Email address must be at least 6 characters long.'),
                            ('sdfgdj@asd', 'Must be a valid email address. Example: name@website.com.'),
                            ('asfss@ da.com', 'Must be a valid email address. Example: name@website.com.'),
                            ]


def test_hvac_email_validation(page_factory):
    hvac_page = page_factory.get_page(page_name='hvac_page')
    hvac_page.open_page()
    owner = gen_random_persons()
    user_path = (('zip_code', '10001'), ('project_type', 'replacement'), ('equipment_type', ['ac']),
                 ('equipment_age', 'less 5'), ('property_type', 'detached'),
                 ('property_size', 50), ('changes_auth', 'yes')
                 )
    perform_user_path(hvac_page, user_path)

    hvac_page.owner_info_name_input().send_keys(owner)
    for invalid_email in invalid_email_and_errors:
        email = invalid_email[0]
        expected_error = invalid_email[1]
        hvac_page.set_email(email)
        hvac_page.next_btn().click()
        assert hvac_page.get_email_error(timeout=2), (f'No Error is displayed on hvac page with email input {email}\n'
                                                      f'Expected error: {expected_error}')
        actual_email_error = hvac_page.get_email_error_text()
        assert expected_error == actual_email_error, (f'Actual email input error on HVAC page is incorrect:\n'
                                                      f'Email input: {email}\n'
                                                      f'Actual error: {actual_email_error}\n'
                                                      f'Expected error: {expected_error}')
