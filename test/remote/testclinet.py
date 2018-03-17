from xmlrpclib import ServerProxy
if __name__ == '__main__':
	s = ServerProxy("http://10.20.216.222:8080")
	# s = ServerProxy("http://127.0.0.1:8080")
	print s.callwebperftest("http://www.duba.com/yx.html")