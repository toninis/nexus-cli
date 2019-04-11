import logging
import sys
import os
import json
from parser import argParser

import warnings
warnings.filterwarnings("ignore")

from httpHandler import nexusHandler

logger = logging.getLogger(__name__)

# Allow imports from current working directory
sys.path.append(os.path.abspath(os.path.curdir))

def pretty_print(json_body):
    return json.dumps(json_body, indent=2, separators=(',', ': '))

def main():
    args = argParser()
    nexusClient = nexusHandler(args)

    if args.subcommand == 'list-repos':
        print(nexusClient.listRepos())

if __name__ == '__main__':
    main()
