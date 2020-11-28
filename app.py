from flask import Flask
from flask_script import Manager

from twitter_sentence_generator.utils.logging_wrapper import log_exception
from twitter_sentence_generator.utils.sentence_generator import generate_sentence
from twitter_sentence_generator.utils.twitter import post_to_twitter_account

app = Flask(__name__)
manager = Manager(app)


@app.route("/")
def index():
    return generate_sentence()


@app.route("/twitter")
def twitter():
    return post_to_twitter_account()


@app.errorhandler(Exception)
def handle_error(e):
    log_exception(e)

    message = str(e)

    return message


if __name__ == "__main__":
    manager.run()
