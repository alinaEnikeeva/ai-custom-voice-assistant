"""
logger.py: Configures logging for AI Assistant.
"""

import logging
import sys


def setup_logging():
    """
    Sets up root logger to output INFO level logs to console with timestamps.
    """
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # Console handler
    ch = logging.StreamHandler(sys.stdout)
    ch.setLevel(logging.INFO)
    formatter = logging.Formatter("[%(asctime)s] %(levelname)s: %(message)s")
    ch.setFormatter(formatter)

    # Avoid adding multiple handlers if called multiple times
    if not logger.handlers:
        logger.addHandler(ch)
