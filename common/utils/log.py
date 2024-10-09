"""Defines common config for logging.

Typical usage:

    logger = get_logger(__name__)
    logger.info('Log info')
"""

import logging

handler = logging.StreamHandler(stream=None)
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(" "message)s")
handler.setFormatter(formatter)


def get_logger(name: str) -> logging.Logger:
    """Get logger for a module.

    Args:
        name: Name of a module

    Returns: logging.Logger object for the module
    """

    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)
    return logger
