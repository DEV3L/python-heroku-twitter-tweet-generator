import random


class RandomHashtagTransformer():
    MAX_TWEET_LENGTH = 140

    def __init__(self, tweet, hashtags):
        self.tweet = tweet
        self.hashtags = list(hashtags)
        random.shuffle(hashtags)

    def append_random_hashtag(self):
        if not len(self.hashtags):
            return

        hashtag = self.hashtags.pop()

        if hashtag in self.tweet:
            return

        tweet = '{tweet} {hashtag}'.format(tweet=self.tweet, hashtag=hashtag)

        if len(tweet) > RandomHashtagTransformer.MAX_TWEET_LENGTH:
            return self.append_random_hashtag()

        self.tweet = tweet
