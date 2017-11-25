#!/usr/bin/env python3
import os
import glob
import re

from extension import Extension

def findLinks(filename):
    with open(filename,"r",encoding='utf8') as file:
        output=file.read()
        urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', output)
        return(urls)

if __name__ == '__main__':
    if os.name=="posix":
        path=os.path.expanduser("~/.config/google-chrome/Default/Extensions/*")
    elif os.name=="nt":
        path=os.path.expanduser(r"~/AppData/Local/Google/Chrome/User Data/Default/Extensions/*")
    # result=os.listdir(path)
    extensions=[]

    extensionPaths=glob.glob(path)

    for extensionPath in extensionPaths:
        try:
            extensions.append( Extension(extensionPath) )
        except ValueError:
            pass

    for extension in extensions:
        print(extension.manifest["name"])
        for path in filter(lambda x: x.endswith('.js'), extension.filelist):
            # print(path)
            print(findLinks(path))
