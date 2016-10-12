from flask import Flask
from flask.ext.runner import Runner
from heroku_random_taylor_swift_lyrics.utils.facebook import post_to_page
from heroku_random_taylor_swift_lyrics.utils.sentence_generator import generate_sentence

app = Flask(__name__)
runner = Runner(app)


@app.route("/")
def index():
    return generate_sentence()


@app.route("/facebook")
def facebook():
    sentence = generate_sentence()
    try:
        post_to_page(sentence)
    except Exception as e:
        print(e)
        sentence = "!" + sentence

    return sentence


if __name__ == "__main__":
    runner.run()
