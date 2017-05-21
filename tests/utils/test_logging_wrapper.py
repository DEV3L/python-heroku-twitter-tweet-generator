import sys
from unittest.mock import patch

from twitter_sentence_generator.utils.logging_wrapper import logging_format, get_logger, create_stream_handler, \
    _level, log_message


@patch('twitter_sentence_generator.utils.logging_wrapper.create_stream_handler')
@patch('twitter_sentence_generator.utils.logging_wrapper.logging')
def test_get_logger(mock_logging, mock_create_stream_handler):
    logger = get_logger()

    mock_logging.Formatter.assert_called_with(logging_format)
    assert 1 == mock_logging.getLogger.call_count
    mock_logging.getLogger.return_value.setLevel.assert_called_with(_level)
    mock_logging.getLogger.return_value.addHandler.assert_called_with(mock_create_stream_handler.return_value)

    assert mock_logging.getLogger.return_value == logger

    get_logger()
    assert 1 == mock_logging.getLogger.call_count


@patch('twitter_sentence_generator.utils.logging_wrapper.logging')
def test_create_stream_handler(mock_logger):
    stream_handler = create_stream_handler(sys.stdout, 'formatter')

    mock_logger.StreamHandler.assert_called_with(sys.stdout)
    mock_logger.StreamHandler.return_value.setLevel.assert_called_with(_level)
    mock_logger.StreamHandler.return_value.setFormatter.assert_called_with('formatter')

    assert mock_logger.StreamHandler.return_value == stream_handler


@patch('twitter_sentence_generator.utils.logging_wrapper.get_logger')
def test_log_message(mock_get_logger):
    log_message('message')
    mock_get_logger.return_value.info.assert_called_with('message')


@patch('twitter_sentence_generator.utils.logging_wrapper.get_logger')
def test_log_message(mock_get_logger):
    log_message('message')
    mock_get_logger.return_value.info.assert_called_with('message')
