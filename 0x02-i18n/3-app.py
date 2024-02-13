#!/usr/bin/env python3
"""basic flask app with babel config"""
from flask import Flask, render_template
from flask_babel import Babel, _, request


class Config(object):
    """Config class for app settings"""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
babel = Babel(app)

app.config.from_object(Config)


@app.route("/")
def index():
    """index page for app"""
    return render_template("3-index.html")


@babel.localeselector
def get_locale():
    """get locale, use accept_languages to determine the best match"""
    return request.accept_languages.best_match(app.config["LANGUAGES"])


if __name__ == "__main__":
    app.run()
