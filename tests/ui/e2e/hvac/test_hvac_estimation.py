import pytest
from tests.ui.e2e.hvac.hvac_page_methods import perform_user_path
from core.utilities.generators import gen_random_email, gen_phone_number, gen_random_persons

owner = gen_random_persons()
user_path_whole = [('zip_code', '10001'), ('project_type', 'replacement'), ('equipment_type', ['ac']),
                   ('equipment_age', 'less 5'), ('property_type', 'detached'),
                   ('property_size', 50), ('changes_auth', 'yes'),
                   ('name_and_email', {'name': owner, 'email': gen_random_email()}),
                   ('phone', gen_phone_number()), ('confirm', 'yes')]


def test_hvac_estimation_process_happy_path(page_factory):
    hvac_page = page_factory.get_page(page_name='hvac_page')
    hvac_page.open_page()

    # Go to the thank-you page with valid inouts
    perform_user_path(hvac_page, user_path_whole)
    # Check the thank-you page is displayed
    thank_you_page = page_factory.get_loaded_page(page_name='thank_you_page')
    # Check the title
    actual_title = thank_you_page.get_title_text()
    owner_first_name = owner.split()[0]
    expected_title = f'Thank you {owner_first_name}, your contractor QA company will call soon!'
    assert actual_title == expected_title, ('Thank you page title is not correct\n'
                                            f'Expected title:{expected_title}\n'
                                            f'Actual title: {actual_title}')


user_paths = [(user_path_whole[0:1]),
              (user_path_whole[0:2])
              ]


@pytest.mark.parametrize("user_path", user_paths)
def test_user_can_cancel_hvac_estimation(user_path, page_factory):
    hvac_page = page_factory.get_page(page_name='hvac_page')
    hvac_page.open_page()
    # Go to the thank-you page with valid inouts
    perform_user_path(hvac_page, user_path)
    hvac_page.stop_estimation_process()
    assert hvac_page.surprise_section(), 'HVAC Replacement & Installation section should be visible'
