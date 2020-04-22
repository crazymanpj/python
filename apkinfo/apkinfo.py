import sys,os,shutil
import subprocess
from hashlib import md5

def md5_file(filepath):
    m = md5()
    a_file = open(filepath, 'rb')
    m.update(a_file.read())
    a_file.close()
    return m.hexdigest()

def getApkVersionCode(apkFilePath):
    if os.path.exists("aapt.exe")== 0:
        return
    versioncode = ""
    cmd = "aapt.exe d badging" +" " + apkFilePath
    ret = subprocess.Popen(cmd, stdin = subprocess.PIPE, stdout = subprocess.PIPE, stderr = subprocess.PIPE, shell = False)
    cmdret = ret.stdout.read()
    print('cmdret: ')
    print(cmdret)
    cmdret = str(cmdret)
    packageInfo = cmdret.splitlines()[0]
    print('packageInfo:')
    print(packageInfo)
    arraytemp = packageInfo.split(" ")
    for subitem in arraytemp:
        if subitem.find("versionCode") >= 0:
            versioncodeinfo = subitem
            versioncode = versioncodeinfo.split("=")[1].strip("'")
        elif subitem.find("name") >= 0:
            info = subitem
            packagename = info.split("=")[1].strip("'")
            print("packagename is: " + packagename)
    return versioncode

path = sys.argv[1]
print(path)

apkver = getApkVersionCode(path)
print("versionCode is: " + apkver)
str_md5 = md5_file(path)
print("md5 is: " + str_md5)
os.system("pause")
