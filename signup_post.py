from bottle import post, redirect, request, response
from g import USERS
from user_auth import create_user_session
from form_validation import (
    is_user_value_unique,
    is_valid_email_address,
    is_valid_name,
    is_valid_password,
    user_exist,
)
import uuid


############################################################
@post("/signup")
def _():
    user_username = request.forms.get("user-username")
    user_email = request.forms.get("user-email")
    user_password = request.forms.get("user-password")
    user_first_name = request.forms.get("user-first-name")
    user_last_name = request.forms.get("user-last-name")

    # Validation
    if not is_valid_name(user_username):
        response.status = 400
        return "Please enter a valid username"

    if not is_user_value_unique("username", user_username):
        response.status = 400
        return "Your chosen username is taken, please try another one"

    if not is_valid_email_address(user_email):
        response.status = 400
        return "Please enter an emailaddress"

    if user_exist("email", user_email):
        response.status = 400
        return "Email already exists. Forgot your password?"

    if user_exist("username", user_username):
        response.status = 400
        return "Username already exists. Forgot your password?"

    if not is_valid_password(user_password):
        response.status = 400
        return "Please enter a valid password"

    if not is_valid_name(user_first_name):
        response.status = 400
        return "Please enter your first name"

    if not is_valid_name(user_last_name):
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
    create_user_session(user)

    return redirect("/home")
