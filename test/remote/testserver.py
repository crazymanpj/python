from SimpleXMLRPCServer import SimpleXMLRPCServer
import os

def add(x,y):
	return x + y

def callwebperftest(url):
	print url
	configpath = r"D:\Program\berserkJS\build\release\data\js\init_url.js"
	print configpath
	try:
		f = open(configpath, 'w')
		f.write(r'input_url = "' + url + '";')
	except Exception as e:
		pass
	finally:
		f.close()
	# command = r"D:\Program\berserkJS\daohong.bat"
	# os.system(command)
	os.chdir(r"D:\Program\berserkJS\build\release")
	print os.getcwd()
	print "test begin..."
	command = r"berserkJS.exe --script=D:/Program/berserkJS/demo/pcautoscript.js --command"
	os.system(command)
	print "test end"

	print "insert DB begin..."
	command = r"daohangdatatodb.exe " + url + r" D:\Program\berserkJS\build\release\data\json"
	print command
	os.system(command)
	print "insert DB end"
	print "end"
	return True

if __name__ == '__main__':
	s = SimpleXMLRPCServer(('10.20.216.222', 8080))
	# s = SimpleXMLRPCServer(('127.0.0.1', 8080))
	s.register_function(callwebperftest, "callwebperftest")
	s.serve_forever()
