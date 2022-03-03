from bottle import post, redirect, response, request
import jwt
import uuid
import time

from g import JSON_WEB_TOKEN_SECRET, sessions, tweets, users
from form_validation import is_valid_email_address, is_user_value_unique
from user_auth import create_user_session


############################################################
@post("/create-tweet")
def _():
    encoded_user_session = request.get_cookie("user_session")

    if not encoded_user_session:
        return redirect("/")

    decoded_user_session = jwt.decode(encoded_user_session, JSON_WEB_TOKEN_SECRET, algorithms=["HS256"])
    user_session_id = decoded_user_session["session_id"]

    if user_session_id not in sessions:
        response.delete_cookie("user_session")
        return redirect("/")

    tweet_message = request.forms.get("tweet-message")

    if not tweet_message:
        response.status = 400
        return "Please enter a tweet message"

    if len(tweet_message) < 3:
        response.status = 400
        return "Your tweet must be at least 3 characters or longer"

    tweet_id = str(uuid.uuid4())
    tweet_created_at = int(time.time())
    tweet_user_id = decoded_user_session["id"]

    tweet = {
        "id": tweet_id,
        "created_at": tweet_created_at,
        "message": tweet_message,
        "user_id": tweet_user_id,
    }

    tweets.insert(0, tweet)

    return redirect("/home")
