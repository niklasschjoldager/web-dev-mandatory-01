from bottle import get, view, redirect, request
import jwt
from g import JSON_WEB_TOKEN_SECRET, sessions

############################################################
@get("/")
@view("index")
def _():
    encoded_user_session = request.get_cookie("user_session")

    if not encoded_user_session:
        return

    decoded_user_session = jwt.decode(encoded_user_session, JSON_WEB_TOKEN_SECRET, algorithms=["HS256"])
    user_session = decoded_user_session["session_id"]

    if user_session in sessions:
        return redirect("/home")

    return
