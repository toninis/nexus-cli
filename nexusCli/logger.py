import logging

logger = logging.getLogger(__name__)

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
        super(loggerInit, self).__init__()
        self.__level = logging.DEBUG if debug else logging.INFO
        logging.basicConfig(level=self.__level,format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    @property
    def logging_level(self):
        return self.logging_map[str(self.__level)]
