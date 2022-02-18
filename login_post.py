from bottle import post, redirect, request
from form_validation import is_valid_email_address_string

############################################################


@post("/login")
def _():
    user_email = request.forms.get("user-email")
    user_password = request.forms.get("user-password")

    # Validation
    if not is_valid_email_address_string(user_email):
        return "Please enter your emailaddress"

    if not user_password:
        return "Please enter your password"

    return "Nice"
