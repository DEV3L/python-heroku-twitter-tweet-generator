from unittest.mock import patch

from app.twitter_sentence_generator.extractors.file_words_extractor import FileWordsExtractor


def test_file_words_extractor():
    file_words_extractor = FileWordsExtractor('file_name')

    assert 'file_name' == file_words_extractor.file_name
    assert None is file_words_extractor._file_contents


@patch('app.twitter_sentence_generator.extractors.file_words_extractor.open')
def test_read_file(mock_open):
    mock_open.return_value.__enter__.return_value.read.return_value = 'test'
    file_words_extractor = FileWordsExtractor('file_name')

    file_words_extractor._read_file()

    assert 'test' == file_words_extractor._file_contents
    assert 'test' == file_words_extractor.file_contents


@patch('app.twitter_sentence_generator.extractors.file_words_extractor.FileWordsExtractor._read_file')
def test_words_calls_read_file(mock_read_file):
    mock_read_file.return_value = 'test'
    file_words_extractor = FileWordsExtractor('file_name')

    words = file_words_extractor.words

    assert ['test'] == words
    assert mock_read_file.called


def test_words():
    # [\w']+|[.,!?;]
    file_words_extractor = FileWordsExtractor('file_name')
    file_words_extractor._file_contents = ''

    assert [] == file_words_extractor.words

    file_words_extractor._file_contents = 'test 1   "test".,!?;' + u'\u0660'

    assert ['test', '1', 'test', '.', ',', '!', '?', ';', '٠'] == file_words_extractor.words
