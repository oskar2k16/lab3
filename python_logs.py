import logging

def get_logs(level, format_string):
    logging.basicConfig(level=level, format=format_string)
    return logging

logger = get_logs(logging.DEBUG, '%(asctime)s - %(levelname)s - %(message)s')
logger.debug("Debugging log")
logger.info("Information log")
logger.warning("Warning log")
logger.error("Error log")



