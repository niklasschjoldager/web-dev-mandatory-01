from bottle import get, redirect, response, request
import jwt

from g import SESSIONS, JSON_WEB_TOKEN_SECRET


############################################################
@get("/logout")
def _():
    encoded_user_session = request.get_cookie("user_session")

    if not encoded_user_session:
        return redirect("/")

    decoded_user_session = jwt.decode(encoded_user_session, JSON_WEB_TOKEN_SECRET, algorithms=["HS256"])
    user_session_id = decoded_user_session["session_id"]

    response.delete_cookie("user_session")

    if user_session_id not in SESSIONS:
        redirect("/")

    SESSIONS.remove(user_session_id)

    return redirect("/")
