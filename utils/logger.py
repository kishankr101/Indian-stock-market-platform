"""
Logger Module

Configures logging for the application.
"""

import logging
import os
from config import LOGGING_CONFIG


def setup_logger(name, log_file=None):
    """
    Setup and configure a logger.
    
    Args:
        name: Logger name
        log_file: Optional log file path
    
    Returns:
        Configured logger object
    """
    logger = logging.getLogger(name)
    logger.setLevel(getattr(logging, LOGGING_CONFIG['LOG_LEVEL']))
    
    # Create formatters
    formatter = logging.Formatter(LOGGING_CONFIG['LOG_FORMAT'])
    
    # Add console handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    
    # Add file handler if log file is specified
    if log_file or LOGGING_CONFIG['LOG_FILE']:
        file_path = log_file or LOGGING_CONFIG['LOG_FILE']
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        
        file_handler = logging.FileHandler(file_path)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    
    return logger


# Create application logger
app_logger = setup_logger('app')
