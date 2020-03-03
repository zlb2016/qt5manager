import matplotlib.pyplot as plt
import numpy as np
import cv2
from PIL import Image,ImageGrab
 
class imageedit_self:
    def imagemagnification(path):#放大
        img = Image.open(path) # 读取的图像显示的<matplotlib.image.AxesImage object at 0x7f9f0c60f7f0>
        region = img.transpose(Image.ROTATE_180) #翻转
        (x, y) = img.size
        out = img.resize((x+300, y+300)) # 改变大小
    
        plt.subplot(121),plt.imshow(img,'gray'),plt.title('origin_img')
        plt.subplot(122),plt.imshow(out,'gray'),plt.title('magnification_img')
        plt.show()

    def imagereduction(path):#缩小
        img = Image.open(path) # 读取的图像显示的<matplotlib.image.AxesImage object at 0x7f9f0c60f7f0>
        
        (x, y) = img.size
        out = img.resize((x-200, y-200)) # 改变大小
    
        plt.subplot(121),plt.imshow(img,'gray'),plt.title('origin_img')
        plt.subplot(122),plt.imshow(out,'gray'),plt.title('reduction_img')
        plt.show()
    def imagegray(path):#灰度化图像
        image = cv2.imread(path)
        b,g,r=cv2.split(image)#先将bgr格式拆分
        img=cv2.merge([r,g,b])
        gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        plt.subplot(121),plt.imshow(img),plt.title('origin_img')
        plt.subplot(122),plt.imshow(gray),plt.title('gray_img')
        plt.show()
    
    def imagebrightness(path, c, b):  # 图像亮度就是每个像素所有通道都加上b
        img1 = cv2.imread(path, cv2.IMREAD_COLOR)
        rows, cols, chunnel = img1.shape
        blank = np.zeros([rows, cols, chunnel], img1.dtype)  # np.zeros(img1.shape, dtype=uint8)
        dst = cv2.addWeighted(img1, c, blank, 1-c, b)
        plt.subplot(121),plt.imshow(img1),plt.title('origin_img')
        plt.subplot(122),plt.imshow(dst),plt.title('gray_img')
        plt.show()

    def imagerotate(path):#旋转
        img = Image.open(path) # 读取的图像显示的<matplotlib.image.AxesImage object at 0x7f9f0c60f7f0>
        region = img.transpose(Image.ROTATE_180) #翻转
        out1 = img.rotate(30) #旋转30度
        out2 = img.rotate(60) #旋转60度
        out3 = img.rotate(90) #旋转90度
    
        plt.subplot(221),plt.imshow(img),plt.title('origin_img')
        plt.subplot(222),plt.imshow(out1),plt.title('rotate30_img')
        plt.subplot(223),plt.imshow(out2),plt.title('rotate60_img')
        plt.subplot(224),plt.imshow(out3),plt.title('rotate90_img')
        plt.show()

    def imagegrab(path):#截图
        img = Image.open(path)
        bbox = (760, 0, 1160, 1080)
        im = ImageGrab.grab()
        plt.subplot(121),plt.imshow(img),plt.title('origin_img')
        #im.save('a.jpeg')
        plt.subplot(122),plt.imshow(im),plt.title('grab_img')
        plt.show()

    


