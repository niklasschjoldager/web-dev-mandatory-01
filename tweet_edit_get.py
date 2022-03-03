from bottle import get, redirect, response, request, view
import jwt
from g import JSON_WEB_TOKEN_SECRET, sessions, tweets

############################################################
@get("/edit-tweet/<tweet_id>")
@view("edit-tweet")
def _(tweet_id):
    # User validation
    # TODO: Used 3-6 different places. Make it a reusable function
    encoded_user_session = request.get_cookie("user_session")

    if not encoded_user_session:
        return redirect("/")

    decoded_user_session = jwt.decode(encoded_user_session, JSON_WEB_TOKEN_SECRET, algorithms=["HS256"])
    user_session_id = decoded_user_session["session_id"]

    if user_session_id not in sessions:
        response.delete_cookie("user_session")
        return redirect("/")

    # Tweet validation
    if not tweet_id:
        responses.status = 400
        return "Tweet does not exist"

    user_id = decoded_user_session["id"]

    # Delete item if exist
    for index, tweet in enumerate(tweets):
        if tweet["id"] == tweet_id and tweet["user_id"] == user_id:
            return dict(tweet=tweet)
    return redirect("/home")
