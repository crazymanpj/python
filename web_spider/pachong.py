import urllib2,re

url = ""

h_file = open("url.txt", "wb")

text = urllib2.urlopen(url).read()

pattern1 = re.compile('<a rd="1" href="http://\S+"')

group1 =  pattern1.findall(text)

for element in group1:
   # element = element.lstrip('<a rd="1" href=')
   # element = element.strip('"')
   print element + "\n"
   url_match = (element[16 : len(element) - 1]) + "\n"
   h_file.write(url_match)

print len(group1)



pattern2 = re.compile('<a href="http://\S+"')

group2 = pattern2.findall(text)

for element in group2:
   print element + "\n"
   url_match = (element[9 : len(element) - 1]) + "\n"
   h_file.write(url_match)
print len(group2)



h_file.close()