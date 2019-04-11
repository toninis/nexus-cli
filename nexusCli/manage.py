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
        print('Available Repos:')
        for i in nexusClient.listRepos():
            print('\t'+i)
    elif args.subcommand == 'list-tags':
        print('Available Tags for {}:'.format(args.repo))
        for i in nexusClient.listTags(args.repo):
            print('\t'+i)
    elif args.subcommand == 'get':
        print(nexusClient.deleteImage(args.repo, args.tag))
        print(nexusClient.getImageDigest(args.repo, args.tag))
        print(nexusClient.searchAsset(args.repo, args.tag))
        # print(nexusClient.getManifest(args.repo, args.tag))

if __name__ == '__main__':
    main()
