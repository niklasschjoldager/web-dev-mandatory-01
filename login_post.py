from bottle import post, redirect, response, request
import jwt
import uuid
import time

from g import sessions, users
from form_validation import is_valid_email_address, is_user_value_unique
from user_auth import create_user_session, get_user_data


############################################################
@post("/login")
def _():
    user_email = request.forms.get("user-email")
    user_password = request.forms.get("user-password")

    # Validation
    # TODO: user email or username, instead of only email to login
    if not is_valid_email_address(user_email):
        response.status = 400
        return "Please enter your email address"

    if not user_password:
        response.status = 400
        return "Please enter your password"

    user = get_user_data(user_email)

    if not user:
        response.status = 400
        return "Email does not exist, please try again"

    if not user["password"] == user_password:
        response.status = 400
        return "Wrong password, please try again"

    create_user_session(user)

    return redirect("/home")
