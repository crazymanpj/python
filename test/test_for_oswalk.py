import os
import os.path
rootdir = r"d:\kuaipan\python\mobiledata\common\testforother"

for parent, dirnames, filenames in os.walk(rootdir):
	for file in filenames:
		fullfilepath = os.path.join(parent, file)
		ext = os.path.splitext(fullfilepath)
		if ext[1] == ".so" and os.path.basename(fullfilepath).find("plugin") == 0:
			print fullfilepath