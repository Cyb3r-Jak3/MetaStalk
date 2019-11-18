"""Makes the logger for the program"""
import logging


def make_logger(name, log_level):
    """Creates the logger.
       Might look to make this happen in the main script
    """
    logger = logging.getLogger(name)
    logger.setLevel(log_level)
    formatter = logging.Formatter(
        '%(levelname)s - %(name)s - %(asctime)s - %(message)s',
        '%Y-%m-%d %H:%M:%S')
    fh = logging.FileHandler("{}.log".format(name), mode='w')
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    ch = logging.StreamHandler()
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    return logger
