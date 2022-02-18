from bottle import post, redirect, request, response
from g import USERS
from form_validation import (
    is_user_value_unique,
    is_valid_email_address_string,
    is_valid_name_string,
    is_valid_password_string,
)
import uuid


User = {
    "id",
    "username",
    "first_name",
    "last_name",
    "email",
    "password",
}

############################################################
@post("/signup")
def _():
    user_username = request.forms.get("user-username")
    user_email = request.forms.get("user-email")
    user_password = request.forms.get("user-password")
    user_first_name = request.forms.get("user-first-name")
    user_last_name = request.forms.get("user-last-name")

    print(USERS)

    # Validation
    if not is_valid_name_string(user_username):
        response.status = 400
        return "Please enter a valid username"

    if not is_user_value_unique("username", user_username):
        response.status = 400
        return "Your chosen username is taken, please try another one"

    if not is_valid_email_address_string(user_email):
        response.status = 400
        return "Please enter an emailaddress"

    if is_user_value_unique("email", user_email):
        response.status = 400
        return "Email already exists. Forgot your password?"

    if not is_valid_password_string(user_password):
        response.status = 400
        return "Please enter a valid password"

    if not is_valid_name_string(user_first_name):
        response.status = 400
        return "Please enter your first name"

    if not is_valid_name_string(user_last_name):
        response.status = 400
        return "Please enter your last name"

    user = {
        "id": str(uuid.uuid4()),
        "username": user_username,
        "first_name": user_first_name,
        "last_name": user_last_name,
        "email": user_email,
        "password": user_password,
    }
    USERS.append(user)

    return f"{USERS}"
