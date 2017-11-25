#!/usr/bin/env python3
import os
import glob
from urllib.parse import urlparse
from extension import Extension

def findLinks(filename):
    with open(filename,"r",encoding='utf8') as file:
        output=file.read()
        urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', output)
        return(urls)

def findDomains(filename):
    urls = findLinks(filename)
    domains = [urlparse(url)[1].split('/') for url in urls]
    return(domains)

if __name__ == '__main__':
    if os.name=="posix":
        path=os.path.expanduser("~/.config/google-chrome/Default/Extensions/*")
    elif os.name=="nt":
        path=os.path.expanduser(r"~/AppData/Local/Google/Chrome/User Data/Default/Extensions/*")
    # result=os.listdir(path)
    extensions=[]

    extensionPaths=glob.glob(path)

    for extensionPath in extensionPaths:
        extensions.append( Extension(extensionPath) )

    for extension in extensions:
        print(extension.manifest["name"])
 