import argparse
import logging
from . import get_version_string
from .config import BaseConfig
from .logger import loggerInit

DISPLAY_VERSION_MESSAGE = '''
nexusCli 
Version: {}'''.strip("\n").format(
    get_version_string()
)

class argParser(BaseConfig):
    """docstring for argParser."""

    def __init__(self):
        super().__init__()
        self.__logger = logging.getLogger('{}.{}'.format(__name__,self.__class__.__name__))
        self.__run()
        self.__logger.info(self.debug)
        loggerInit(self.debug)

    def __run(self):
        """Argument Parser"""

        global_parser = argparse.ArgumentParser(
            formatter_class=argparse.RawTextHelpFormatter,
            description='Python application to manipulate nexus artifacts.'
        )

        subparsers = global_parser.add_subparsers(
            title='Available sub-commands',
            dest='subcommand'
        )

        global_parser.add_argument('--debug', help='Enable Debug Logging...' , action='store_true')
        global_parser.add_argument('-V','--version',action='version',version=DISPLAY_VERSION_MESSAGE,help='Show the version of the engine and exit.')
        global_parser.add_argument('--host', help='Nexus Host')
        global_parser.add_argument('--port', help='Nexus Port')
        global_parser.add_argument('--repository', help='Nexus repository')
        global_parser.add_argument('--insecure','-k', help='Do not verify TLS cert', action='store_true')

        help_parser = subparsers.add_parser('help')

        config_parser = subparsers.add_parser('config',help='Configuration file parser')
        config_parser.add_argument('--update',help='Update existing config', action='store_true')

        listRepos_parser = subparsers.add_parser('list-repos',help='List repos')

        tags_parser = subparsers.add_parser('list-tags',help='List tags')
        tags_parser.add_argument('--repo',help='Specific repo',required=True)

        get_parser = subparsers.add_parser('get-component',help='Get manifest')
        get_parser.add_argument('--repo',help='Specific repo',required=True)
        get_parser.add_argument('--tag',help='Specific tag',required=True)

        search_parser = subparsers.add_parser('search',help='Search Image')
        search_parser.add_argument('--repo',help='Specific repo',required=True)
        search_parser.add_argument('--tag',help='Specific tag',required=True)

        delete_parser = subparsers.add_parser('delete',help='Delete Image')
        delete_parser.add_argument('--repo',help='Specific repo',required=True)
        group_delete_parser = delete_parser.add_mutually_exclusive_group(required=True)
        group_delete_parser.add_argument('--tag',help='Specific tag')
        group_delete_parser.add_argument('--all',help='All tags',action='store_true')
        group_delete_parser.add_argument('--regex',help='Remove by regex')

        if not vars(global_parser.parse_args())['subcommand'] or vars(global_parser.parse_args())['subcommand'] == 'help':
            global_parser.parse_args(['--help'])

        if vars(global_parser.parse_args())['subcommand'] == 'config':
            self.generateConfig(update=vars(global_parser.parse_args())['update'])

        for key,value in vars(global_parser.parse_args()).items():
            if value is not None:
                setattr(self, key, value)

        if self.insecure:
            setattr(self, 'secure', False)
