# !/usr/bin/env python
# encoding=utf-8

# from libtiff import TIFF
from scipy import misc
from PIL import Image
import os

##tiff文件解析成图像序列
##tiff_image_name: tiff文件名；
##out_folder：保存图像序列的文件夹
##out_type：保存图像的类型，如.jpg、.png、.bmp等
def tiff_to_image_array(tiff_image_name, out_folder, out_type):

    tif = TIFF.open(tiff_image_name, mode = "r")
    idx = 0
    for im in list(tif.iter_images()):
        #
        im_name = out_folder + str(idx) + out_type
        misc.imsave(im_name, im)
        print(im_name, 'successfully saved!!!')
        idx = idx + 1
    return

##图像序列保存成tiff文件
##image_dir：图像序列所在文件夹
##file_name：要保存的tiff文件名
##image_type:图像序列的类型
##image_num:要保存的图像数目
def image_array_to_tiff(image_dir, file_name, image_type, image_num):

    out_tiff = TIFF.open(file_name, mode = 'w')

    #这里假定图像名按序号排列
    for i in range(1, image_num):
        image_name = image_dir + str(i) + '.' + image_type
        image_array = Image.open(image_name)
        #缩放成统一尺寸
        img = image_array.resize((480, 480), Image.ANTIALIAS)
        out_tiff.write_image(img, compression = None, write_rgb = True)

    out_tiff.close()
    return

def image_array_to_tiff2(image_dir, image_type, image_num):
    SAVEPATH = r'd:\kuaipan\python\autopublishpackage\script\tiff'
    for i in range(0, image_num):
        image_name = os.path.join(image_dir, str(i)+ '.' + image_type)
        image = Image.open(image_name)
        image.save(os.path.join(SAVEPATH, str(i)+ '.tiff'))

if __name__=='__main__':
    # image_array_to_tiff('/home/pangjian/imgtiff/', 'test.tiff', 'png', 9)
    # print 'test'
    # im = Image.open(r'd:\kuaipan\python\test\captcha2.png')
    # im.save('captcha2.tiff') # or 'test.tif'
    image_array_to_tiff2(r'd:\kuaipan\python\autopublishpackage\script\img', 'png', 500)
