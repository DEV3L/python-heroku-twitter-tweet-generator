import tweepy

# Twitter src keys
cfg = {
    'consumer_key': 'KjtDKHqlanK2XukWwOjz1Bl1O',
    'consumer_secret': 'GHwPYcWLcVyX6ZiUd2HW3Esov8d8wl48d8Gh1jnJ1AXvlt7rPq',
    'access_token': '788934655928045568-QCyqDhe0BH8OKGHtkCUUfzQ9YDiJgW9',
    'access_token_secret': 'c24Fi8aAzszEOANmHhx3XQQNfRiICnc3YkolEZRl1SQ35'
}


def post_to_twitter_account():
    get_api(cfg).update_status(status='Hello world!')


def get_api(cfg):
    auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
    auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
    return tweepy.API(auth)


if __name__ == '__main__':
    post_to_twitter_account()
