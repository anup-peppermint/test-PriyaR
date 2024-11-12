# utils/logger.py
import logging

def setup_logger():
    logging.basicConfig(filename='pizzeria.log', level=logging.INFO,
                        format='%(asctime)s:%(levelname)s:%(message)s')
    return logging.getLogger()
