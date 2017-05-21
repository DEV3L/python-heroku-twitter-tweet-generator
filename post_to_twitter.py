import os
from datetime import datetime

from twitter_sentence_generator.utils.twitter import post_to_twitter_account


def tweet():
    if os.environ.get('HEROKU_HOUR_MODULO') \
            and datetime.now().hour % int(os.environ.get('HEROKU_HOUR_MODULO')) != 0:
        return
    post_to_twitter_account()


if __name__ == "__main__":
    tweet()
