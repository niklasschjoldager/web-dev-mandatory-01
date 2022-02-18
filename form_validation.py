from g import REGEX_EMAIL, REGEX_PASSWORD, USERS
import re

############################################################


def is_valid_name_string(name_string):
    if not name_string:
        return False
    if not isinstance(name_string, str):
        return False
    if len(name_string) < 2:
        return False

    return True


def is_valid_email_address_string(email_string):
    if not email_string:
        return False
    if not isinstance(email_string, str):
        return False
    if not re.match(REGEX_EMAIL, email_string):
        return False

    return True


def is_valid_password_string(password_string):
    if not password_string:
        return False
    if not isinstance(password_string, str):
        return False
    # TODO: Validate password requirements
    # if not re.match(REGEX_PASSWORD, password_string):
    #     return False

    return True


def is_user_value_unique(property_name, value):
    if not value or not property_name:
        return False

    for user in USERS:
        if user[property_name] == value:
            return False

    return True
