import logging
import sys

LOGGING_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
logger = logging.getLogger(__name__)

def preInit(__logger):
    __logger.setLevel(logging.INFO)
    __streamHandler = logging.StreamHandler()
    __streamHandler.setLevel(logging.INFO)
    __streamHandler.setFormatter(logging.Formatter(LOGGING_FORMAT))
    __logger.addHandler(__streamHandler)
    return __logger

class loggerInit:
    """docstring for loggerInit."""

    logging_map = {
     "50": "CRITICAL",
     "40": "ERROR",
     "30": "WARNING",
     "20": "INFO",
     "10": "DEBUG"
    }

    def __init__(self, debug=False):
        self.__logger = logging.getLogger('{}.{}'.format(__name__,self.__class__.__name__))
        self.__level = logging.DEBUG if debug else logging.INFO
        logging.basicConfig(level=self.__level,format=LOGGING_FORMAT)
        self.__logger.info('Logging initialized! Level: {}'.format(self.logging_level))

    @property
    def logging_level(self):
        return self.logging_map[str(self.__level)]
