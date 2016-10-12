import os

from heroku_random_taylor_swift_lyrics.utils.markov_sentence_generator import buildMapping, genSentence, wordlist

CHAIN_LENGTH = os.environ.get('MARKOV_CHAIN_LENGTH', '3')
FILE_NAME = os.environ.get('MARKOV_FILE_NAME',
                           '.' + os.path.sep + 'resources' + os.path.sep + 'scrubbed_file.txt')


# /Users/justinbeall/GITHUB/python-heroku-random-taylor-swift-lyrics/resources/scrubbed_file.txt
def generate_sentence():
    buildMapping(wordlist(FILE_NAME), int(CHAIN_LENGTH))
    return genSentence(int(CHAIN_LENGTH))
