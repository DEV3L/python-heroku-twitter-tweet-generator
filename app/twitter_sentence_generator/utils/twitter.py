import os

import tweepy

from app.twitter_sentence_generator.utils.sentence_generator import generate_sentence, FILE_NAME

# Fill in the values noted in previous step here
cfg = {
    'consumer_key': os.environ.get('TWITTER_CONSUMER_KEY'),
    'consumer_secret': os.environ.get('TWITTER_CONSUMER_SECRET'),
    'access_token': os.environ.get('TWITTER_ACCESS_TOKEN'),
    'access_token_secret': os.environ.get('TWITTER_TOKEN_SECRET')
}

twitter_tags = os.environ.get('TWITTER_TAG', '#taylorswift')


def post_to_twitter_account(file_name=None):
    twitter_hashtags = twitter_tags.split(',')
    tweet = generate_sentence(file_name=file_name or FILE_NAME, twitter_hashtags=twitter_hashtags)
    get_api(cfg).update_status(status=tweet)
    return tweet


def get_api(cfg):
    auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
    auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
    return tweepy.API(auth)


if __name__ == '__main__':
    file_name = '..' + os.path.sep + '..' + os.path.sep + 'resources' + os.path.sep + 'scrubbed_file.txt'
    post_to_twitter_account(file_name)
