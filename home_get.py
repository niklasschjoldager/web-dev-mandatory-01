from bottle import get, redirect, response, request, view
import jwt

from g import SESSIONS, TWEETS, JSON_WEB_TOKEN_SECRET, USERS
from user_auth import get_user_field

############################################################


@get("/home")
@view("home")
def _():
    encoded_user_session = request.get_cookie("user_session")

    if not encoded_user_session:
        return redirect("/")

    decoded_user_session = jwt.decode(encoded_user_session, JSON_WEB_TOKEN_SECRET, algorithms=["HS256"])
    user_session = decoded_user_session["session_id"]

    if user_session not in SESSIONS:
        response.delete_cookie("user_session")
        return redirect("/")

    user_first_name = decoded_user_session["first_name"]
    user_id = decoded_user_session["id"]

    return dict(
        tweets=TWEETS, users=USERS, user_id=user_id, user_first_name=user_first_name, get_user_field=get_user_field
    )
