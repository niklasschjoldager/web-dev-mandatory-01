from bottle import response
import time
import jwt
import uuid
from g import SESSIONS, JSON_WEB_TOKEN_SECRET, USERS

############################################################
def create_user_session(user):
    user_session_id = str(uuid.uuid4())

    user_session = {
        "id": user["id"],
        "session_id": user_session_id,
        "first_name": user["first_name"],
        "last_name": user["last_name"],
        "issued_at": int(time.time()),
    }

    encoded_jwt = jwt.encode(user_session, JSON_WEB_TOKEN_SECRET, algorithm="HS256")
    response.set_cookie("user_session", encoded_jwt)

    SESSIONS.append(user_session_id)

    return user_session


def get_user_data(username_or_email):
    if not username_or_email:
        return False

    for index, user in enumerate(USERS):
        if user["email"] == username_or_email:
            return USERS[index]
        if user["username"] == username_or_email:
            return USERS[index]
        if user["id"] == username_or_email:
            return USERS[index]

    return False


def get_user_field(property_to_search_by, value_to_search_after, value_to_get_back):
    if not property_to_search_by or not value_to_search_after or not value_to_get_back:
        return False

    for index, user in enumerate(USERS):
        if user[property_to_search_by] == value_to_search_after:
            return USERS[index][value_to_get_back]

    return False
