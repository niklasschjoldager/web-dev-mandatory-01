from bottle import redirect, response, request, post
import jwt
from g import JSON_WEB_TOKEN_SECRET, sessions, tweets

############################################################
@post("/delete-tweet")
def _():
    # User validation
    encoded_user_session = request.get_cookie("user_session")

    if not encoded_user_session:
        return redirect("/")

    decoded_user_session = jwt.decode(encoded_user_session, JSON_WEB_TOKEN_SECRET, algorithms=["HS256"])
    user_session_id = decoded_user_session["session_id"]

    if user_session_id not in sessions:
        response.delete_cookie("user_session")
        return redirect("/")

    # Tweet validation
    tweet_id = request.forms.get("tweet-id")

    if not tweet_id:
        responses.status = 400
        return "Tweet does not exist"

    user_id = decoded_user_session["id"]

    # Delete item if exist
    for index, tweet in enumerate(tweets):
        if tweet["id"] != tweet_id:
            return

        if tweet["user_id"] == user_id:
            tweets.pop(index)
            return redirect("/home")
        else:
            response.status = 400
            return redirect("/home")

    return redirect("/home")
