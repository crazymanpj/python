import qrcode
img = qrcode.make("www.baidu.com")
img.save("./test.png")