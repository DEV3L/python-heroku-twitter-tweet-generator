import logging
import sys

_logger = None


def get_logger(*, level=logging.DEBUG):
    global _logger

    if _logger:
        return _logger

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    logger = logging.getLogger()
    logger.setLevel(level)

    stdout_handler = logging.StreamHandler(sys.stdout)
    stdout_handler.setLevel(level)
    stdout_handler.setFormatter(formatter)

    logger.addHandler(stdout_handler)

    _logger = logger
    return _logger


def log_message(message):
    get_logger().info(message)


def log_exception(message):
    get_logger().exception(message)
