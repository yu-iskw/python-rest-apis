import logging
from pythonjsonlogger import jsonlogger


def get_logger():
    # Configure logging.
    log_format = '%(asctime) %(levelname) %(module) %(funcName) %(lineno) %(message)'
    formatter = jsonlogger.JsonFormatter(log_format)
    logger = logging.getLogger()
    logHandler = logging.StreamHandler()
    logHandler.setFormatter(formatter)
    logger.addHandler(logHandler)
    logger.setLevel(logging.DEBUG)
    return logger
