__version__ = '1.0.0'

def get_version():
    """
    Get engine version in split list object
    :rtype: list[str]
    """
    if '-' in __version__:
        version = __version__.split('.')
        return version[0:-1] + version[-1].split('-')
    return __version__.split('.')


def get_version_string():
    """
    Get engine version in string format
    """
    return __version__
