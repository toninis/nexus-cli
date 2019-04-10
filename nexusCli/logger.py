import logging

logger = logging.getLogger(__name__)

def loggerInit(debug=False):
    logging_map = {
     "50": "CRITICAL",
     "40": "ERROR",
     "30": "WARNING",
     "20": "INFO",
     "10": "DEBUG"
    }
    __level = logging.DEBUG if debug else logging.INFO
    logging.basicConfig(level=__level,format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    logger.info('Logging Initialized. Level: {}'.format(logging_map[str(__level)]))
