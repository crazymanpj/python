#coding=utf-8
text = u"中国"
print text
text = text.encode("gb2312")
print text
text = text.decode("GB2312")
print text