import os

from heroku_twitter_random_sentence_generator.transformers.random_hashtag_transformer import RandomHashtagTransformer
from heroku_twitter_random_sentence_generator.utils.markov_sentence_generator import buildMapping, genSentence, wordlist

CHAIN_LENGTH = os.environ.get('MARKOV_CHAIN_LENGTH', '2')
FILE_NAME = os.environ.get('MARKOV_FILE_NAME', '.' + os.path.sep + 'resources' + os.path.sep + 'scrubbed_file.txt')
MAX_HASHTAGS = int(os.environ.get('TWITTER_MAX_HASHTAGS', '5'))

def _generate_sentence(*, file_name=FILE_NAME, chain_length=CHAIN_LENGTH):
    return genSentence(int(chain_length))


def generate_sentence(*, file_name=FILE_NAME, chain_length=CHAIN_LENGTH, twitter_hashtags=None):
    sentence = None
    lines = []
    with open(file_name, 'r') as file_handler:
        for line in file_handler:
            lines.append(line)

    is_continue = False
    buildMapping(wordlist(file_name), int(chain_length))

    while True:
        sentence = _generate_sentence(file_name=file_name, chain_length=chain_length)
        if len(sentence) > RandomHashtagTransformer.MAX_TWEET_LENGTH:
            continue
        for line in lines:
            if sentence == line:
                is_continue = True
                break

        if is_continue:
            is_continue = False
            continue

        random_hashtag_transformer = RandomHashtagTransformer(sentence, twitter_hashtags)
        random_hashtag_transformer.append_random_hashtag()
        sentence = random_hashtag_transformer.tweet
        break

    return sentence


if __name__ == "__main__":
    file_name = '..' + os.path.sep + '..' + os.path.sep + 'resources' + os.path.sep + 'scrubbed_file.txt'
    for _ in range(10):
        print(generate_sentence(file_name=file_name))
