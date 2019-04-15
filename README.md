#### Nexus CLI Script

> Only works for python 3.

Installation :
```
make install
```

Configuration:
```
nexusCli config
```

Usage :
```
astam ~ ➜ nexusCli --help
usage: nexusCli [-h] [--debug] [--host HOST] [--port PORT]
                [--repository REPOSITORY] [--insecure]
                {help,config,list-repos,list-tags,get-component,search,delete}
                ...

Python application to manipulate nexus artifacts.

optional arguments:
  -h, --help            show this help message and exit
  --debug               Enable Debug Logging...
  --host HOST           Nexus Host
  --port PORT           Nexus Port
  --repository REPOSITORY
                        Nexus repository
  --insecure, -k        Do not verify TLS cert

Available sub-commands:
  {help,config,list-repos,list-tags,get-component,search,delete}
    config              Configuration file parser
    list-repos          List repos
    list-tags           List tags
    get-component       Get manifest
    search              Search Image
    delete              Delete Image
```
