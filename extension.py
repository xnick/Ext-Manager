class Extension(object):
    """docstring for Extension."""
    manifest={}
    path=""
    files={}

    def __init__(self, manifest, path, filelist):
        self.manifest = manifest
        self.path = path
        self.files = filelist
