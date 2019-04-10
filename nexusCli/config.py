import logging
from os import getenv

logger = logging.getLogger(__name__)

class BaseConfig:
    """docstring for BaseConfig."""

    def __init__(self):
        self.logger = logging.getLogger('{}.{}'.format(__name__,self.__class__.__name__))
        self.host = getenv('NEXUS_HOST','nexus.dev.encode.local')
        self.port = getenv('NEXUS_PORT', None)
        self.proto = getenv('NEXUS_PROTO','https')
        self.repository = getenv('NEXUS_REPO','encode-registry')
        self.logger.info('Config Initialized')
