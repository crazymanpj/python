from ftplib import FTP
filename = "kswebshield.dll"
ftp = FTP(host, user, password)   # connect to host, default port
#ftp.login()               # user anonymous, passwd anonymous@
ftp.cwd(dir)
ftp.retrlines('LIST')     # list directory contents

h_downloadfile = open(filename, "wb")
ftp.retrbinary(r"RETR %s"%(filename), h_downloadfile.write)
print "Download...%s"%(filename)
h_downloadfile.close()