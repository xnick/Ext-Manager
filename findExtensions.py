#!/usr/bin/env python3
import os
import glob

from extension import Extension


if __name__ == '__main__':
    if os.name=="posix":
        path=os.path.expanduser("~/.config/google-chrome/Default/Extensions/*")
    elif os.name=="nt":
        path=os.path.expanduser("~/AppData/Local/Google/Chrome/User\ Data/Default/Extensions")
    # result=os.listdir(path)
    extensions=[]

    extensionPaths=glob.glob(path)

    for extensionPath in extensionPaths:
        extensions.append( Extension(extensionPath) )

    for extension in extensions:
        print(extension.manifest["name"])
