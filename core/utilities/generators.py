import random
import string
from faker import Faker


def gen_phone_number(length: int = 10) -> str:
    """This method generates phone number with different length
        :param length: amount of numbers in the number
        :return: phone number
    """
    phone_number = '5' + ''.join(random.choice(string.digits) for _ in range(length - 1))
    return phone_number


def gen_random_email() -> str:
    """This method generates random valid email
        :return: random email
    """
    fake = Faker()
    return fake.email()


def gen_random_persons():
    """This method generates random person Name and Surname
        :return: random person Name and Surname
    """
    fake = Faker()
    return fake.name()


def gen_long_email(length: int = 300) -> str:
    """This method generates random email with specific length
        :param length: len of the user email
        :return: random email with specific length
    """
    if length < 6:
        raise ValueError(f"Can't generate long email with a length < 6. Requested length: {length}")
    too_long_email = ''.join(random.choice(string.ascii_letters) for _ in range(length - 6))
    return too_long_email + '@gm.co'
