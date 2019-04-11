import argparse
import logging
from config import BaseConfig

class argParser(BaseConfig):
    """docstring for argParser."""

    def __init__(self):
        super().__init__()
        self.logger = logging.getLogger('{}.{}'.format(__name__,self.__class__.__name__))
        self.__run()
        self.base_url = '{}://{}:{}'.format(self.proto,self.host,self.port) if self.port \
            else '{}://{}'.format(self.proto,self.host)

    def __run(self):
        """Argument Parser"""

        argparser = argparse.ArgumentParser(
            formatter_class=argparse.RawTextHelpFormatter,
            description='Python application to manipulate nexus artifacts.'
        )

        subparsers = argparser.add_subparsers(
            title='Available sub-commands',
            dest='subcommand'
        )

        config_parser = subparsers.add_parser('config',help='Generate Configuration file',formatter_class=argparse.ArgumentDefaultsHelpFormatter)
        config_parser.add_argument('--update',help='Update existing config', action='store_true')
        argparser.add_argument('--debug', help='Enable Debug Logging...' , action='store_true')
        argparser.add_argument('--host', help='Nexus Host')
        argparser.add_argument('--port', help='Nexus Port')
        argparser.add_argument('--repository', help='Nexus repository')
        argparser.add_argument('--insecure','-k', help='Do not verify TLS cert', action='store_true')

        if vars(argparser.parse_args())['subcommand']:
            self.generateConfig(update=vars(argparser.parse_args())['update'])

        for key,value in vars(argparser.parse_args()).items():
            if value is not None:
                setattr(self, key, value)

        if self.insecure:
            setattr(self, 'secure', False)
