import os
import glob
import json

class Extension(object):
    """docstring for Extension."""
    manifest={}
    path=""
    filelist=[]

    def __init__(self, path):
        self.path = path
        for gpath in glob.glob(os.path.join(path, '*/manifest.json')):
            with open(gpath) as mandir:
                self.manifest=json.load(mandir)
        for root, dirs, files in os.walk(self.path):
            for f in files:
                self.filelist.append(os.path.join(root, f))
