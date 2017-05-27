#!/usr/bin/env python
#encoding=utf-8
# Date:    2017-05-27
# Author:  pangjian
# version: 1.0

import os
import re
from hashlib import md5
import json

def md5_file(filepath):
    m = md5()
    with open(filepath, 'rb') as f:
        m.update(f.read())
    return m.hexdigest()

#walk by order
def mywalk(toppath):
    try:
        names = os.listdir(toppath)
        # print("ww", names)
    except Exception as e:
        print("error...")
        return

    dirs, nodirs = [], []
    for name in names:
        if os.path.isdir(os.path.join(toppath, name)):
            dirs.append(name)
        else:
            nodirs.append(name)

    yield toppath, dirs, nodirs

    try:
        tempdirs = sorted([int(i) for i in dirs])
        dirs = [str(i) for i in tempdirs]
    except:
        pass
    for name in dirs:
        newpath = os.path.join(toppath, name)
        if not os.path.islink(newpath):
            for x in mywalk(newpath):
                yield x

def getflodernamebypath(path):
    print(path)
    m = re.match('(\S+wallpaper)(\\\\)(\d+)(.+)', path)
    if m != None:
        return m.group(3)
    else:
        return m

def getlabelbyname(name):
    print(name)
    m = re.match('(\d+)(\S+)', name.split('.')[0])
    if m != None:
        print(m.group(2))
        return m.group(2)
    else:
        return m

def writetofile(jsontext):
    with open("wallpaper.json", 'wb') as f:
        f.write(jsontext)


def genaratejson(path):
    imginfo = {}
    retjson = {}
    wallpaper = []
    for i in mywalk(r""):
        for j in i[2]:
            tags = []
            filepath = os.path.join(i[0], j)
            md5 = md5_file(filepath)
            catalog = getflodernamebypath(filepath)
            tags.append(catalog)
            label = getlabelbyname(os.path.basename(filepath))

            isinjson = False
            for m in wallpaper:
                if m['id'] == md5:
                    if not catalog in m['tags']:
                        m['tags'].append(catalog)
                    isinjson = True
                else:
                    continue

            if(not isinjson):
                imginfo = {
                    "id" :md5_file(filepath),
                    "tags" : tags
                }

                if label != None:
                    imginfo['label'] = label

                wallpaper.append(imginfo)

    retjson = {
        "pre_fmt":"",
        "src_fmt":"",
        "wallpaper" : wallpaper
    }
    print(retjson)
    writetofile(json.dumps(retjson))
    return None


if __name__ == '__main__':
    path = r""
    genaratejson(path)