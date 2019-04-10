import argparse
import logging
from config import BaseConfig

class argParser(BaseConfig):
    """docstring for argParser."""

    def __init__(self):
        super(argParser, self).__init__()
        self.logger = logging.getLogger('{}.{}'.format(__name__,self.__class__.__name__))
        self.__run()
        self.base_url = '{}://{}:{}'.format(self.proto,self.host,self.port) if self.port \
            else '{}://{}'.format(self.proto,self.host)

    def __run(self):
        """Argument Parser"""
        argparser = argparse.ArgumentParser(
            description='Python application to manipulate nexus artifacts.'
        )
        argparser.add_argument('--debug', help='Enable Debug Logging...' , action='store_true')
        argparser.add_argument('--host', help='Nexus Host')
        argparser.add_argument('--port', help='Nexus Port')
        argparser.add_argument('--repository', help='Nexus repository')
        argparser.add_argument('--verify','-k', help='Do not verify TLS cert', action='store_false')
        for key,value in vars(argparser.parse_args()).items():
            if value is not None:
                setattr(self, key, value)
