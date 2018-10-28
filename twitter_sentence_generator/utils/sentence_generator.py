import os

from twitter_sentence_generator.extractors.file_words_extractor import FileWordsExtractor
from twitter_sentence_generator.transformers.random_hashtag_transformer import RandomHashtagTransformer
from twitter_sentence_generator.utils.markov_sentence_generator import build_mapping, build_sentence

SCRUBBED_FILE = os.environ.get('SCRUBBED_FILE', './resources/twentyonepilots_scrubbed.txt')
CHAIN_LENGTH = os.environ.get('MARKOV_CHAIN_LENGTH', '3')
MAX_HASHTAGS = int(os.environ.get('TWITTER_MAX_HASHTAGS', '5'))


def _generate_sentence(*, chain_length=CHAIN_LENGTH):
    return build_sentence(int(chain_length))


def generate_sentence(*, file_name=SCRUBBED_FILE, chain_length=CHAIN_LENGTH, twitter_hashtags=None):
    with open(file_name, 'r') as file_handler:
        lines = [line.rstrip() for line in file_handler]

    file_words_extractor = FileWordsExtractor(file_name)
    words = file_words_extractor.extract_words()

    build_mapping(words, int(chain_length))

    while True:
        sentence = _generate_sentence(chain_length=chain_length)
        if len(sentence) > RandomHashtagTransformer.MAX_TWEET_LENGTH:
            continue

        is_not_unique = [line for line in lines if sentence == line]
        if is_not_unique:
            continue

        random_hashtag_transformer = RandomHashtagTransformer(sentence, twitter_hashtags)
        random_hashtag_transformer.append_random_hashtag()
        sentence = random_hashtag_transformer.tweet
        break

    return sentence


if __name__ == "__main__":
    file_name = SCRUBBED_FILE.split('/')[-1]
    file_path = f'../../resources/{file_name}'
    for _ in range(10):
        print(generate_sentence(file_name=file_path))
