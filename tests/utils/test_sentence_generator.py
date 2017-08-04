import os
from unittest.mock import patch

import pytest

from twitter_sentence_generator.utils.sentence_generator import generate_sentence


@patch('twitter_sentence_generator.utils.sentence_generator.genSentence')
def test__generate_sentence_default(mock_gen_sentence):
    from twitter_sentence_generator.utils.sentence_generator import _generate_sentence, CHAIN_LENGTH

    _generate_sentence()

    mock_gen_sentence.assert_called_with(int(CHAIN_LENGTH))


@patch('twitter_sentence_generator.utils.sentence_generator.genSentence')
def test__generate_sentence_chain_str_int(mock_gen_sentence):
    from twitter_sentence_generator.utils.sentence_generator import _generate_sentence
    chain_length = '2'

    _generate_sentence(chain_length=chain_length)

    mock_gen_sentence.assert_called_with(2)


def test__generate_sentence_chain_str_not_int():
    from twitter_sentence_generator.utils.sentence_generator import _generate_sentence
    chain_length = 'x'

    with(pytest.raises(ValueError)):
        _generate_sentence(chain_length=chain_length)


@patch('twitter_sentence_generator.utils.sentence_generator.genSentence')
def test__generate_sentence_int(mock_gen_sentence):
    from twitter_sentence_generator.utils.sentence_generator import _generate_sentence
    chain_length = 2

    _generate_sentence(chain_length=chain_length)

    mock_gen_sentence.assert_called_with(2)


@patch('twitter_sentence_generator.utils.sentence_generator.genSentence')
def test__generate_sentence_chain_does_not_use_file_name(mock_gen_sentence):
    from twitter_sentence_generator.utils.sentence_generator import _generate_sentence, CHAIN_LENGTH

    _generate_sentence(file_name='file_name')
    mock_gen_sentence.assert_called_with(int(CHAIN_LENGTH))

    _generate_sentence()
    mock_gen_sentence.assert_called_with(int(CHAIN_LENGTH))


def test_main():
    file_name = '..' + os.path.sep + '..' + os.path.sep + 'resources' + os.path.sep + 'scrubbed_file.txt'
    print('\n10 random sentences from the file: {file_name}'.format(file_name=file_name))
    for _ in range(10):
        sentence = generate_sentence(file_name=file_name)
        print(sentence)
        assert sentence
