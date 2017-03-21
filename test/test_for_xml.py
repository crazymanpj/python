#coding=utf-8
import xml.dom.minidom

file = "AndroidManifest.xml"
testfile = "test.xml"
testfile2 = "test2.xml"
dom = xml.dom.minidom.parse(testfile)
root = dom.documentElement
print root.nodeName
print root.nodeValue
print root.nodeType
print root.ELEMENT_NODE

# temp = root.getElementsByTagName('maxid')
# maxidvalue = temp[0]
# print maxidvalue.nodeName

# temp = root.getElementsByTagName('caption')
# for i in temp:
# 	print i.nodeName

employees = root.getElementsByTagName("employee")

for employee in employees:
	#print (employee.nodeName)
	#print (employee.toxml())

	nameNode = employee.getElementsByTagName("name")[0]
	print (nameNode.childNodes)

	print (nameNode.nodeName + ":" + nameNode.childNodes[0].nodeValue)

	ageNode = employee.getElementsByTagName("age")[0]
	print (ageNode.childNodes)
	print (ageNode.nodeName + ":" + ageNode.childNodes[0].nodeValue)

	for n in employee.childNodes:
		print (n)