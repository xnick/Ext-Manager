#!/usr/bin/env python3
import os
import glob
import json

from extension import Extension


if __name__ == '__main__':
    unixPath=os.path.expanduser("~/.config/google-chrome/Default/Extensions/**/manifest.json")

    # result=os.listdir(unixPath)
    extensions=[]

    manifests=glob.glob(unixPath,recursive=True)

    for man in manifests:
        with open(man) as fman:
            extensions.append( Extension(json.load(fman), os.path.dirname(man), []) )

    for extension in extensions:
        print(extension.path)
