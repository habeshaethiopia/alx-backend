#!/usr/bin/env python3
"""
basic flask app
"""
from flask import Flask, render_template, request
from flask_babel import Babel, _, request


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


if __name__ == "__main__":
    app.run()
