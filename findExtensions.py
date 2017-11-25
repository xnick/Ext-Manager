#!/usr/bin/env python3
import os
import glob
import json

from extension import Extension


if __name__ == '__main__':
    if os.name=="posix":
        path=os.path.expanduser("~/.config/google-chrome/Default/Extensions/**/manifest.json")
    elif os.name=="nt":
        path=os.path.expanduser("~/AppData/Local/Google/Chrome/User\ Data/Default/Extensions")
    # result=os.listdir(path)
    extensions=[]

    manifests=glob.glob(path,recursive=True)

    for man in manifests:
        with open(man) as fman:
            extensions.append( Extension(json.load(fman), os.path.dirname(man), []) )

    for extension in extensions:
        print(extension.path)
