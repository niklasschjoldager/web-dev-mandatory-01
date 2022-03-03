users = [
    {
        "id": "5f5f311d-ca9b-481b-8846-f7db449270f8",
        "username": "niklasschjoldager",
        "first_name": "Niklas",
        "last_name": "Schjoldager",
        "email": "test@mail.dk",
        "password": "1234",
    }
]
sessions = []
tweets = [
    {
        "id": "1f62ebd4-3b6a-4b06-9ff9-24542fca3095",
        "created_at": 1645722067,
        "message": "This is my first tweet. Hello tweeter!",
        "user_id": "5f5f311d-ca9b-481b-8846-f7db449270f8",
    }
]

JSON_WEB_TOKEN_SECRET = "My super token secret"

REGEX_EMAIL = '^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$'
REGEX_PASSWORD = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
