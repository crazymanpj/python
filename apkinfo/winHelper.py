# encoding: UTF-8
import win32api,os,sys,shutil
import getfilesinfo,common
import ctypes,subprocess

def checkIsHasCapitalLetter(filename):
    if filename.islower() == True:
        return  True
    else:
        common.outError(filename + "文件名存在大写.................")
        sys.exit()

def getDatVersionCode(datpath):
    dll = ctypes.windll.LoadLibrary( 'interface.dll' )
    datpath_p = ctypes.c_wchar_p()
    datpath_p.value = datpath
    nRst = dll.Dat_To_Xml(datpath_p)
    
    xmlname = "kandeng.xml"
    xmlpath = os.path.join(os.path.dirname(datpath), xmlname)
    xmlfile = open(xmlpath)
    codeinfo = xmlfile.read()
    code = codeinfo.split("=")[1].strip("'")
    code = code.strip("\n")
    file.close(xmlfile)
    os.remove(xmlpath)
    return code

def getApkVersionCode(apkFilePath):
    if os.path.exists("aapt.exe")== 0 or os.path.exists("interface.dll")== 0 or os.path.exists("zlib1.dll") == 0:
        return    
    versioncode = ""
    cmd = "aapt.exe d badging" +" " + apkFilePath
    ret = subprocess.Popen(cmd, stdin = subprocess.PIPE, stdout = subprocess.PIPE, stderr = subprocess.PIPE, shell = False)
    cmdret = ret.stdout.read()
    packageInfo = cmdret.splitlines()[0]
    arraytemp = packageInfo.split(" ")
    for subitem in arraytemp:
        if subitem.find("versionCode") >= 0:
            versioncodeinfo = subitem
            versioncode = versioncodeinfo.split("=")[1].strip("'")
            break
    return versioncode

def CheckApkCfg(DisPath):
    apklocalpath = r"phone\shoujikongservice.apk"
    datlocalpath = r"data\kandeng.dat"
    apkpath = os.path.join(DisPath, apklocalpath)
    datpath = os.path.join(DisPath, datlocalpath)
    
    if(os.path.exists(apkpath) and os.path.exists(datpath)):
        versioncode = getApkVersionCode(apkpath)
        versioncode_dat = getDatVersionCode(datpath)
        if cmp(versioncode, versioncode_dat) != 0:
            info = r"shoujikongservice.apk: " + versioncode + " kandeng.dat: " + versioncode_dat
            common.outError(info)
            sys.exit()
    return True

def isPE(filename):
    extlist=['.exe','.dll','.sys','.khf']
    if os.path.splitext(filename)[1] not in extlist:
        return False
    else:
        return True

def getFileVersion(file_name):
    info = win32api.GetFileVersionInfo(file_name, os.sep)
    ms = info['FileVersionMS']
    ls = info['FileVersionLS']
    version = '%d.%d.%d.%04d' % (win32api.HIWORD(ms), win32api.LOWORD(ms), win32api.HIWORD(ls), win32api.LOWORD(ls))
    return version  

def getFileVerByArray(file_name):
    verinfo = []
    info = win32api.GetFileVersionInfo(file_name, os.sep)
    ms = info['FileVersionMS']
    ls = info['FileVersionLS']
    verinfo.append(win32api.HIWORD(ms))
    verinfo.append(win32api.LOWORD(ms))
    verinfo.append(win32api.HIWORD(ls))
    verinfo.append(win32api.LOWORD(ls))
    return verinfo      

def isVerHigher(srcfile, disfile):
    array1 = getFileVerByArray(srcfile)
    array2 = getFileVerByArray(disfile)

    for i in range(0, len(array2)):
        if array1[i] > array2[i]:
            return False
        elif array1[i] < array2[i]:
            return True
        elif array1[i] == array2[i]:
            continue
    return False

def signcheck(Dispath):
    nosignfile = []
    noverfile =[]
    
    ret = True
    retvercheck = True
    for root, path, files in os.walk(Dispath):
        for file in files:
            fullfilepath = os.path.join(root, file)
            if getfilesinfo.main(fullfilepath) == False:
                nosignfile.append(file)
                ret = False
                
            if getfilesinfo.getFileVersion(fullfilepath) == None:
                noverfile .append(file)
                retvercheck = False
                
            #检查是否存在大写文件
            checkIsHasCapitalLetter(file)
                
    if ret == True:
        common.outMsg("sign check success")
    elif ret == False:
        common.outError("digital signature verification failed! " + str(nosignfile))
        sys.exit()
        
    if retvercheck == True:
        common.outMsg("ver check success")
    elif retvercheck == False:
        common.outError("file version verification failed! " + str(noverfile))
        sys.exit()
        
def updateindex():
    try:
        sqlindex = r"\\10.20.220.57\index_makedata\index.sqlite"
        inindex = r"\\10.20.220.57\index_makedata\index.ini"
        currentpath = os.getcwd()
        shutil.copyfile(sqlindex, os.path.join(currentpath, r"index.sqlite"))
        shutil.copyfile(inindex, os.path.join(currentpath, r"index.ini"))        
    except:
        return False
    return True

def init():
    path1 = r"\\dubabin\DubaTest\KIS\DailyBuild\kis_2013_released_sp5.0_fb\inc\20131017.127270\diffdata"
    path2 = r"\\10.20.221.86\DubaTest\KIS\DailyBuild\kis_2013_released_sp5.0_fb\inc\20131017.127270\diffdata"
#    path3 = r"\\10.20.223.55\data\update_back_kav2010\201310\11\1403"
    path4 = r"\\10.20.220.57\data_back\update_back_kav2010\201401\12\092743"
    path5 = r"\\10.20.220.176\Testlib\libupdate\hmpgconfig\newDefenseFile"
    path6 = r"\\10.20.220.119\dubarelease\updata\Setup\kmobile\2001"
    
    if os.path.isdir(path1) == False:
        cmd1 = r'net use \\dubabin\ipc$ "duba123" /user:"duba"'
        os.system(cmd1)

    if os.path.isdir(path2) == False:
        cmd2 = r'net use \\10.20.221.86\ipc$ "duba123" /user:"duba"'
        os.system(cmd2)
        
    if os.path.isdir(path4) == False:
        cmd4 = r'net use \\10.20.220.57\ipc$ "duba123" /user:"duba"'
        os.system(cmd4)            
                
    if os.path.isdir(path5) == False:
        cmd5 = r'net use \\10.20.220.176\ipc$ "duba123" /user:"duba"'
        os.system(cmd5)
        
    if os.path.isdir(path6) == False:
        cmd6 = r'net use \\10.20.220.119\ipc$ "duba123" /user:"duba"'
        os.system(cmd6)        
                    
    if(updateindex() == False):
        common.outMsg("update index failed!")
        
def encrypt(key, s):     
    b = bytearray(str(s).encode("gbk"))     
    n = len(b) # 求出 b 的字节数     
    c = bytearray(n*2)     
    j = 0
    for i in range(0, n):     
        b1 = b[i]     
        b2 = b1 ^ key # b1 = b2^ key     
        c1 = b2 % 16
        c2 = b2 // 16 # b2 = c2*16 + c1     
        c1 = c1 + 65
        c2 = c2 + 65 # c1,c2都是0~15之间的数,加上65就变成了A-P 的字符的编码     
        c[j] = c1     
        c[j+1] = c2     
        j = j+2
    return c.decode("gbk")     

def decrypt(key, s):     
    c = bytearray(str(s).encode("gbk"))     
    n = len(c) # 计算 b 的字节数     
    if n % 2 != 0 :     
        return ""     
    n = n // 2
    b = bytearray(n)     
    j = 0
    for i in range(0, n):     
        c1 = c[j]     
        c2 = c[j+1]     
        j = j+2
        c1 = c1 - 65
        c2 = c2 - 65
        b2 = c2*16 + c1     
        b1 = b2^ key     
        b[i]= b1     
    try:     
        return b.decode("gbk")     
    except:     
        return "decrypt failed"