try:
	open("ddd.txt", "r")
except Exception as e:
	print "fe"
	print "et" + str(e)

try:
	open("ddd.txt", "r")
except Exception, e:
	print "fe"
	print "et" + str(e)