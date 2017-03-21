import axmlparserpy.axmlprinter as axmlprinter
from xml.dom import minidom
ap = axmlprinter.AXMLPrinter(open(r'd:\kuaipan\python\test\test\AndroidManifest.xml', 'rb').read())
buff = minidom.parseString(ap.getBuff()).toxml()
print(buff)
xmlfile = open('test.xml', "r+")
xmlfile.write(buff)
xmlfile.close()