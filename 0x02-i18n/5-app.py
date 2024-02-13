#!/usr/bin/env python3
"""basic flask app"""
from flask import Flask, render_template, request, g
from flask_babel import Babel, request

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config(object):
    """Config class"""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
babel = Babel(app)

app.config.from_object(Config)


@app.route("/")
def index() -> str:
    """index page"""
    return render_template("3-index.html")


@babel.localeselector
def get_locale() -> str:
    """
    Gets locale from request object
    """
    locale = request.args.get("locale", "").strip()
    if locale and locale in Config.LANGUAGES:
        return locale
    return request.accept_languages.best_match(app.config["LANGUAGES"])


def get_user() -> dict | None:
    """get user"""
    try:
        return users[int(request.args.get("login_as"))]
    except Exception:
        return None


@app.before_request
def before_request():
    """before request"""
    user = get_user()
    if user:
        g.user = user
    else:
        g.user = None


if __name__ == "__main__":
    app.run()
