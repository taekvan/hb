import logging
import allure

logger = logging.getLogger("project")


@allure.step
def select_project_type_by_name_and_next(page, project_type):
    project_type = project_type.lower()
    match project_type:
        case 'replacement':
            page.project_type_replacement_item().click()
            page.next_btn().click()
            page.equipment_ac_checkbox()
        case 'repair':
            raise ValueError(f'{project_type} button is not implemented')
        case 'not sure':
            raise ValueError(f'{project_type} button is not implemented')
        case _:
            raise ValueError(f'Project type should be in [replacement, repair, not sure], but got {project_type}')


@allure.step
def select_equipment_type_and_next(page, equipment_list):
    for equipment in equipment_list:
        equipment = equipment.lower()
        match equipment:
            case 'ac':
                page.equipment_ac_checkbox().click()
            case _:
                raise ValueError(f'{equipment} option is not implemented')
        page.next_btn().click()


@allure.step
def select_equipment_age_and_next(page, age):
    age = age.lower()
    match age:
        case 'less 5':
            page.age_less_5().click()
            page.next_btn().click()
        case _:
            raise ValueError(f'Equipment age {age} in not implemented or not in  [less 5]')


@allure.step
def select_property_type_and_next(page, property_type):
    property_type = property_type.lower()
    match property_type:
        case 'detached':
            page.property_type_detached().click()
            page.next_btn().click()
        case _:
            raise ValueError(f'Property type {property_type} in not implemented or not in  [detached]')


@allure.step
def set_zip_and_next(page, zip_code):
    page.zip_code_input().send_keys(zip_code)
    page.get_estimate_btn().click()
    page.project_type_replacement_item()


@allure.step
def select_property_size_and_next(page, size):
    page.property_size_input().send_keys(size)
    page.next_btn().click()


@allure.step
def select_changes_authorization_and_next(page, value):
    value = value.lower()
    match value:
        case 'yes':
            page.property_changes_yes_btn().click()
            page.next_btn().click()
        case _:
            raise ValueError(f'Changes authorization value is not implemented {value}')


@allure.step
def type_name_email_and_next(page, name, email):
    page.owner_info_name_input().send_keys(name)
    page.owner_info_email_input().send_keys(email)
    page.next_btn().click()


@allure.step
def type_phone_number_and_next(page, phone):
    page.phone_number_input().send_keys(phone)
    page.submit_btn().click()


@allure.step
def confirm_phone_if_needed(page):
    if btn := page.phone_number_is_correct_btn():
        btn.click()
    else:
        logger.info("No confirm phone number button found")


def perform_user_path(page, user_path):
    """
    Method to perform user path on the hvac estimation process
        :param page: instance of HVAC clas object
        :param user_path: user path with input variables
        Example: user_path = [('zip_code', '10001'), ('project_type', 'replacement'),]
                selects 10001 zip code and then selects replacement project type

    """
    for operation in user_path:
        match operation[0]:
            case 'zip_code':
                set_zip_and_next(page, operation[1])
            case 'project_type':
                select_project_type_by_name_and_next(page, operation[1])
            case 'equipment_type':
                select_equipment_type_and_next(page, operation[1])
            case 'equipment_age':
                select_equipment_age_and_next(page, operation[1])
            case 'property_type':
                select_property_type_and_next(page, operation[1])
            case 'property_size':
                select_property_size_and_next(page, operation[1])
            case 'changes_auth':
                select_changes_authorization_and_next(page, operation[1])
            case 'name_and_email':
                type_name_email_and_next(page, name=operation[1]['name'], email=operation[1]['email'])
            case 'phone':
                type_phone_number_and_next(page, operation[1])
            case 'confirm':
                confirm_phone_if_needed(page)
            case _:
                raise ValueError(f'User path option {operation} is not defined')
