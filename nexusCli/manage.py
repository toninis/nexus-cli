import logging
import sys
import os
import json
from parser import argParser
from logger import loggerInit
from config import BaseConfig
from httpHandler import nexusHandler

logger = logging.getLogger(__name__)

# Allow imports from current working directory
sys.path.append(os.path.abspath(os.path.curdir))

def pretty_print(json_body):
    return json.dumps(json_body, indent=2, separators=(',', ': '))

def main():
    nexusClient = nexusHandler()
    loggerInit(nexusClient.debug)
    logger.info(nexusClient.listComponents())

if __name__ == '__main__':
    main()
