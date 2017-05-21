from flask import Flask
from flask.ext.runner import Runner

from twitter_sentence_generator.utils.facebook import post_to_facebook_page
from twitter_sentence_generator.utils.logging_wrapper import log_exception
from twitter_sentence_generator.utils.sentence_generator import generate_sentence
from twitter_sentence_generator.utils.twitter import post_to_twitter_account

app = Flask(__name__)
runner = Runner(app)


@app.route("/")
def index():
    return generate_sentence()


@app.route("/facebook")
def facebook():
    return post_to_facebook_page(generate_sentence())


@app.route("/twitter")
def twitter():
    try:
        return post_to_twitter_account()
    except Exception as exception:
        log_exception('Could not post to Twitter')
        return exception


if __name__ == "__main__":
    runner.run()
