import logging
import sys

_logger = None
_level = logging.DEBUG

logging_format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'


def get_logger(*, level=None):
    global _logger

    if _logger:
        return _logger

    level = level or _level
    formatter = logging.Formatter(logging_format)

    logger = logging.getLogger()
    logger.setLevel(level)

    logger.addHandler(create_stream_handler(sys.stdout, formatter))

    _logger = logger
    return _logger


def create_stream_handler(stream, formatter):
    stream_handler = logging.StreamHandler(stream)
    stream_handler.setLevel(_level)
    stream_handler.setFormatter(formatter)
    return stream_handler


def log_message(message):
    get_logger().info(message)


def log_exception(message):
    get_logger().exception(message)
