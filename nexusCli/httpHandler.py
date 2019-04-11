import requests
import logging

class nexusHandler:
    """docstring for nexusHandler."""

    def __init__(self,parsedArgs):
        super().__init__()
        self.logger = logging.getLogger('{}.{}'.format(__name__,self.__class__.__name__))
        self.__dict__.update(parsedArgs.__dict__)
        self.base_url = '{}://{}:{}'.format(self.proto,self.host,self.port) if self.port \
            else '{}://{}'.format(self.proto,self.host)
        self.api_version = 'v1'
        self.status_endpoint = '{}/service/rest/{}/status'.format(self.base_url,self.api_version)
        self.status_check()
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
                return requests.get(__tags_url,verify=self.secure).json()['tags']
            except Exception as e:
                self.logger.error('Could not fetch tags.\nError: {}'.format(str(e)))
        else:
            self.logger.error('Image should be one of {}\n'.format(self.repos))

    def __imageExists(self,image):
        return True if image in self.listRepos() else False

    def __tagExists(self,image,tag):
        if self.__imageExists(image):
            return True if tag in self.listTags(image) else False

    def status_check(self):
        try:
            res = requests.get(self.status_endpoint,verify=self.secure)
            self.logger.info('Configuration is valid!')
            if res.status_code != 200:
                raise Exception('Config is wrong or {} is unreachable.\nError: {}'.format(self.base_url,str(res.reason)))
        except Exception as e:
            raise Exception('Config is wrong or {} is unreachable.\nError: {}'.format(self.base_url,str(e)))

    def getManifest(self,image,tag):
        if self.__tagExists(image, tag):
            __manifest_url = '{}/repository/{}/v2/{}/manifests/{}'.format(self.base_url,self.repository,image,tag)
            try:
                return requests.get(__manifest_url,verify=self.secure).json()
            except Exception as e:
                self.logger.error('Image should be one of {}\n. Error: {}'.format(self.repos,str(e)))
        else:
            self.logger.error('Image should be one of {}'.format(self.repos))


    def listRepos(self):
        try:
            res = requests.get(self.repos_url,verify=self.secure)
            self.repos = res.json()['repositories']
            return self.repos
        except Exception as e:
            self.logger.error('Could not fetch repos.\nError: {}'.format(str(e)))

    def listComponents(self,all=True):
        try:
            res = requests.get(self.component_url,params=self.__params,verify=self.secure).json()
            for item in res['items']:
                self.components.append(item)
            while res['continuationToken']:
                self.__params['continuationToken'] = res['continuationToken']
                res = requests.get(self.component_url,params=self.__params,verify=self.secure).json()
                for item in res['items']:
                    self.components.append(item)
            return self.components
        except Exception as e:
            self.logger.error('Could not handle request.\nError: {}'.format(str(e)))
