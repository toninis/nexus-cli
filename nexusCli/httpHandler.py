import requests
from parser import argParser


class nexusHandler(argParser):
    """docstring for nexusHandler."""

    def __init__(self):
        super(nexusHandler, self).__init__()
        self.api_version = 'v1'
        self.component_url = '{}/service/rest/{}/components'.format(self.base_url,self.api_version)
        self.assets_url = '{}/service/rest/{}/assets'.format(self.base_url,self.api_version)
        self.__params = {
        "repository": self.repository
        }

    def listComponents(self):
        try:
            res = requests.get(self.component_url,params=self.__params,verify=self.verify)
            return res.text
        except Exception as e:
            raise
