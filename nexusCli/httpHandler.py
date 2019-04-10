import requests
import logging
from parser import argParser

class Images(object):
    """docstring for Images."""

    def __init__(self, arg):
        super(Images, self).__init__()
        self.arg = arg


class nexusHandler(argParser):
    """docstring for nexusHandler."""

    def __init__(self):
        super(nexusHandler, self).__init__()
        self.logger = logging.getLogger('{}.{}'.format(__name__,self.__class__.__name__))
        self.api_version = 'v1'
        self.component_url = '{}/service/rest/{}/components'.format(self.base_url,self.api_version)
        self.assets_url = '{}/service/rest/{}/assets'.format(self.base_url,self.api_version)
        self.repos_url = '{}/repository/{}/v2/_catalog'.format(self.base_url,self.repository)
        self.__params = {
        "repository": self.repository
        }
        self.components = []
        self.repos = []

    def listTags(self,image=None):
        if self.__imageExists(image):
            __tags_url = '{}/repository/{}/v2/{}/tags/list'.format(self.base_url,self.repository,image)
            try:
                return requests.get(__tags_url,verify=self.verify).json()['tags']
            except Exception as e:
                self.logger.error('Could not fetch repos.\nError: {}'.format(str(e)))
        else:
            self.logger.error('Image should be one of {}\n'.format(self.repos))

    def __imageExists(self,image):
        return True if image in self.listRepos() else False

    def __tagExists(self,image,tag):
        if self.__imageExists(image):
            return True if tag in self.listTags(image) else False

    def getManifest(self,image,tag):
        if self.__tagExists(image, tag):
            __manifest_url = '{}/repository/{}/v2/{}/manifests/{}'.format(self.base_url,self.repository,image,tag)
            try:
                return requests.get(__manifest_url,verify=self.verify).json()
            except Exception as e:
                self.logger.error('Image should be one of {}\n. Error: {}'.format(self.repos,str(e)))
        else:
            self.logger.error('Image should be one of {}'.format(self.repos))


    def listRepos(self):
        try:
            res = requests.get(self.repos_url,verify=self.verify).json()
            self.repos = res['repositories']
            return self.repos
        except Exception as e:
            self.logger.error('Could not fetch repos.\nError: {}'.format(str(e)))

    def listComponents(self,all=True):
        try:
            res = requests.get(self.component_url,params=self.__params,verify=self.verify).json()
            for item in res['items']:
                self.components.append(item)
            while res['continuationToken']:
                self.__params['continuationToken'] = res['continuationToken']
                res = requests.get(self.component_url,params=self.__params,verify=self.verify).json()
                for item in res['items']:
                    self.components.append(item)
            return self.components
        except Exception as e:
            self.logger.error('Could not handle request.\nError: {}'.format(str(e)))
