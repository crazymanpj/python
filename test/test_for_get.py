import urllib2,os
opener = urllib2.build_opener()
f = opener.open('http://10.20.212.34/details/newfile.html?filename=kxecom.dll')
print f.read()

t = r""
print os.path.isdir(t)