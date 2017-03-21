import os
path = r""
repeatnames = set()
jarfilelist = []

for root, path, files in os.walk(path):
	#print root
	#print path
	for file in files:
		#print os.path.splitext(file)
		if os.path.splitext(file)[1] == ".jar":
			#print file
			#print os.path.join(root, file)
			if file in jarfilelist and file.find("classes.jar") == -1:	
				#print file
				repeatnames.add(file)
				print os.path.join(root, file)
				continue
			else:
				jarfilelist.append(file)

for i in repeatnames:
	print i
