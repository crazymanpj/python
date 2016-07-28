import sys
reload(sys)
import markdown
sys.setdefaultencoding('utf-8')
f = open('2.txt')
input = f.read()
#html = markdown.markdown(input)
#html = markdown.markdownFromFile(input)
md = markdown.Markdown()
html = md.convert(input)
print html