import logging
from logging.handlers import RotatingFileHandler

def setup_logger(log_file: str = "app.log") -> logging.Logger:
    logger = logging.getLogger("UserManagementApp")
    logger.setLevel(logging.DEBUG)

    handler = RotatingFileHandler(log_file, maxBytes=5000000, backupCount=5)
    handler.setLevel(logging.ERROR)
    
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    
    logger.addHandler(handler)
    return logger
