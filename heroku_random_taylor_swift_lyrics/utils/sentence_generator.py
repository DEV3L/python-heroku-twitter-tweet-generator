import os

from heroku_random_taylor_swift_lyrics.utils.markov_sentence_generator import buildMapping, genSentence, wordlist

CHAIN_LENGTH = os.environ.get('MARKOV_CHAIN_LENGTH', '3')
FILE_NAME = os.environ.get('MARKOV_FILE_NAME',
                           '.' + os.path.sep + 'resources' + os.path.sep + 'scrubbed_file.txt')


def _generate_sentence(*, file_name=FILE_NAME, chain_length=CHAIN_LENGTH):
    buildMapping(wordlist(file_name), int(chain_length))
    return genSentence(int(chain_length))


def generate_sentence(*, file_name=FILE_NAME, chain_length=CHAIN_LENGTH, twitter_hashtag=None):
    lines = []
    sentence = None
    with open(file_name, 'r') as file_handler:
        for line in file_handler:
            lines.append(line)

    is_continue = False
    while True:
        sentence = _generate_sentence(file_name=file_name, chain_length=chain_length)

        for line in lines:
            if sentence in line:
                is_continue = True
                break

        if is_continue:
            is_continue = False
            continue

        if twitter_hashtag:
            sentence += ' ' + twitter_hashtag
            if len(sentence) <= 140:
                break
        else:
            break

    return sentence


if __name__ == "__main__":
    file_name = '..' + os.path.sep + '..' + os.path.sep + 'resources' + os.path.sep + 'scrubbed_file.txt'
    print(generate_sentence(file_name=file_name))
