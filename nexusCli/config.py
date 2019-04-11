import logging
import os
import sys
from configparser import ConfigParser
from pathlib import Path
from logger import loggerInit
from distutils.util import strtobool

logger = logging.getLogger(__name__)
DEFAULT_CONFIG_FILE = '~/.nexus/config'

class FileConfig(ConfigParser):
    """docstring for FileConfig."""

    base_config_file_path = Path(DEFAULT_CONFIG_FILE).expanduser()

    def __init__(self):
        super().__init__()
        loggerInit()
        self.logger = logging.getLogger('{}.{}'.format(__name__,self.__class__.__name__))
        self.__readConfigFromFile()

    def __generateDefaultConfig(self):
        self['config'] = {}
        self['config']['host'] = 'localhost'
        self['config']['port'] = ''
        self['config']['proto'] = 'http'
        self['config']['repository'] = 'repository'
        self['config']['secure'] = 'True'

    def __readConfigFromFile(self):
        if self.base_config_file_path.is_file():
            self.read(self.base_config_file_path)
        else:
            self.logger.warn('Configuration file {} does not exist. Use subcommand config to create the config file.'.format(self.base_config_file_path))
            self.__generateDefaultConfig()

    def generateConfig(self,update=False,write_to_file=True):
        try:
            if self.base_config_file_path.is_file():
                if update:
                    self.__getInputs()
                    self.__writeConfig()
                    self.logger.info('Configuration file created under {}'.format(self.base_config_file_path))
                    sys.exit(0)
                else:
                    self.logger.info('Configuration file exists. Use --update flag to override.')
                    print(self.base_config_file_path.read_text())
                    sys.exit(0)
            else:
                self.logger.info('Configuration file does not exist. Creating...')
                self.__getInputs()
                self.__writeConfig()
                self.logger.info('Configuration file created under {}'.format(self.base_config_file_path))
                sys.exit(0)
        except Exception as e:
            raise Exception('Something went wrong creating the configuration file. Error: {}'.format(str(e)))

    def __writeConfig(self):
        with open(self.base_config_file_path,'w') as cfg_file:
            self.write(cfg_file)

    def __getInputs(self):
        print('Configuration for nexus-cli tool.')
        self.__host = input('Enter nexus hostname or IP ({}): '.format(self['config']['host']))
        self.__port = input('Enter nexus port if exists ({}): '.format(self['config']['port']))
        self.__proto = input('Enter nexus protocol ({}): '.format(self['config']['proto']))
        self.__repository = input('Enter nexus repository to interact ({}): '.format(self['config']['repository']))
        self.__secure = input('TLS verification ({}): '.format(self['config']['secure']))
        self['config']['host'] = self.__host if self.__host else self['config']['host']
        self['config']['port'] = self.__port if self.__port else self['config']['port']
        self['config']['proto'] = self.__proto if self.__proto else self['config']['proto']
        self['config']['repository'] = self.__repository if self.__repository else self['config']['repository']
        self['config']['secure'] = self.__secure if self.__secure else self['config']['secure']


class BaseConfig(FileConfig):
    """docstring for BaseConfig."""

    def __init__(self):
        super().__init__()
        self.logger = logging.getLogger('{}.{}'.format(__name__,self.__class__.__name__))
        self.host = os.getenv('NEXUS_HOST', self['config']['host'])
        self.port = int(os.getenv('NEXUS_PORT', self['config']['port'])) if os.getenv('NEXUS_PORT', self['config']['port']) else None
        self.proto = os.getenv('NEXUS_PROTO', self['config']['proto'])
        self.repository = os.getenv('NEXUS_REPO', self['config']['repository'])
        self.secure = strtobool(os.getenv('NEXUS_TLS')) if os.getenv('NEXUS_TLS') else self['config'].getboolean('secure')
