from app.twitter_sentence_generator.transformers.random_hashtag_transformer import RandomHashtagTransformer


def _build_random_hashtag_transformer(*, tweet='some text', hashtags=None):
    _hashtags = hashtags or ['#hashtag', ]
    return RandomHashtagTransformer(tweet, _hashtags)


def test_create_random_hashtag_transformer():
    random_hashtag = _build_random_hashtag_transformer()

    assert random_hashtag
    assert 'some text' == random_hashtag.tweet
    assert ['#hashtag'] == random_hashtag.hashtags
    assert 140 == RandomHashtagTransformer.MAX_TWEET_LENGTH


def test_append_random_hashtag():
    expected_value = 'some text #hashtag'

    random_hashtag = _build_random_hashtag_transformer()

    random_hashtag.append_random_hashtag()

    assert expected_value == random_hashtag.tweet


def test_do_not_append_duplicate_hashtag():
    expected_value = 'some text #hashtag'

    random_hashtag = _build_random_hashtag_transformer(hashtags=['#hashtag', '#hashtag'])

    random_hashtag.append_random_hashtag()
    assert expected_value == random_hashtag.tweet

    random_hashtag.append_random_hashtag()
    assert expected_value == random_hashtag.tweet


def test_do_not_append_over_max_tweet_length():
    expected_values = [
        (''.ljust(140, 'x'), ''.ljust(140, 'x')),
        (''.ljust(139, 'x'), ''.ljust(139, 'x')),
        (''.ljust(138, 'x'), ''.ljust(138, 'x')),
        (''.ljust(137, 'x') + ' #t', ''.ljust(137, 'x'))
    ]

    for expected_value, tweet in expected_values:
        random_hashtag = _build_random_hashtag_transformer(tweet=tweet, hashtags=['#t'])
        random_hashtag.append_random_hashtag()
        assert expected_value == random_hashtag.tweet


def test_append_attempts_all_possible_hashtags_to_length():
    hashtags = ['1', '22', '333', '4444']
    tweet = ''.ljust(138, 'x')
    expected_value = tweet + ' 1'

    for _ in range(0, 100):
        random_hashtag = _build_random_hashtag_transformer(tweet=tweet, hashtags=hashtags)
        random_hashtag.append_random_hashtag()
        assert expected_value == random_hashtag.tweet


def test_append_does_not_hashtag_when_greater_than_max_length():
    tweet = ''.ljust(140, 'x')
    random_hashtag = _build_random_hashtag_transformer(tweet=tweet)
    random_hashtag.append_random_hashtag()

    assert tweet == random_hashtag.tweet
    assert ['#hashtag'] == random_hashtag.hashtags
