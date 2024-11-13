from decouple import config


auth_provider = "flower.views.auth.GithubLoginHandler"
auth = config("AUTH")
oauth2_key = config("OAUTH2_KEY")
oauth2_secret = config("OAUTH2_SECRET")
oauth2_redirect_uri = config("OAUTH2_REDIRECT_URI")

