#!/usr/bin/env python3
"""basic flask app"""
from flask import Flask, render_template, request, g
from flask_babel import Babel, _, request

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
    options = [
        request.args.get("locale", "").strip(),
        g.user.get("locale", None) if g.user else None,
        request.accept_languages.best_match(app.config["LANGUAGES"]),
        Config.BABEL_DEFAULT_LOCALE,
    ]
    for locale in options:
        if locale and locale in Config.LANGUAGES:
            return locale


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


def get_timezone() -> str:
    """get timezone"""
    time = [g.user.get("timezone", "").strip(), g.user["timezone"]]
    try:
        for i in time:
            if i:
                return pytz.timezone(i).zone
    except pytz.exceptions.UnknownTimeZoneError:
        return app.config["BABEL_DEFAULT_TIMEZONE"]


if __name__ == "__main__":
    app.run()
