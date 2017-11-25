import os
import glob
import json

class Extension(object):
    """docstring for Extension."""
    manifest={}
    path=""
    files={}

    def __init__(self, path):
        self.path = path
        # path+version
        for gpath in glob.glob(os.path.join(path, '*/manifest.json')):
            with open(gpath) as mandir:
                self.manifest=json.load(mandir)
