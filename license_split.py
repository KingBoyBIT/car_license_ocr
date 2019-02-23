import cv2
# from numpy import *
import numpy as np
# import cv


if __name__ == '__main__':

    im = cv2.imread('test_image.jpg') # 载入图像
    im_hsv = cv2.cvtColor(im,cv2.COLOR_BGR2HSV) # HSV空间操作
    # im_hsv_s = zeros((274, 432,3))
    h,s,v = cv2.split(im_hsv) #得到单通道图像
    zeros = np.zeros(im.shape[:2],dtype="uint8") # 空矩阵

    h = cv2.merge([h,zeros,zeros]) # 将单通道填充为3通道，为后续阈值判断做准备
    s = cv2.merge([s,zeros,zeros])
    v = cv2.merge([v,zeros,zeros])

    h1=cv2.inRange(h,np.array([90,0,0]),np.array([115,0,0])) # 判断颜色阈值
    s1=cv2.inRange(s,np.array([130,0,0]),np.array([255,0,0]))
    v1=cv2.inRange(v,np.array([80,0,0]),np.array([255,0,0]))

    # cv2.imshow("src",im)

    tmp = cv2.bitwise_and(h1, s1) # H S V三个通道求与运算，得到二值车牌图
    im_bin = cv2.bitwise_and(tmp,v1)

    element = cv2.getStructuringElement(cv2.MORPH_CROSS,(2,2)) # 膨胀和腐蚀滤波的核

    mask = cv2.dilate(im_bin,element)# 腐蚀
    mask = cv2.erode(mask,element,dst=None,anchor=None,iterations=2)# 膨胀
    # im_bin = cv2.bitwise_not(im_bin)
    # cv2.imshow("mask",mask)

    # cv2.imshow("h",h)                            #显示三通道的值都为R值时d图片
    # cv2.imshow("s",s)                          #显示三通道的值都为G值时d图片
    # cv2.imshow("v",v)                           #显示三通道的值都为B值时d图片
    #
    # cv2.imshow("h1",h1)                            #显示三通道的值都为R值时d图片
    # cv2.imshow("s1",s1)                          #显示三通道的值都为G值时d图片
    # cv2.imshow("v1",v1)                           #显示三通道的值都为B值时d图片
    #
    # cv2.imshow("binary image",im_bin)

    im_gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY) # 原图的灰度图
    retval, im_gray_bin = cv2.threshold(im_gray, 0, 255, cv2.THRESH_OTSU) #采用大律法对灰度图二值化

    # cv2.imshow("im_gray_bin",im_gray_bin)

    # 在mask图像中确定车牌的位置
    itr = 20
    tmp = cv2.bitwise_not(mask)
    tmp = cv2.erode(tmp,element,dst=None,anchor=None,iterations=itr)# 膨胀
    tmp = cv2.dilate(tmp,element,dst=None,anchor=None,iterations=itr)# 腐蚀

    # 四角的坐标
    height, width = zeros.shape
    arr = []

    for i in range(height):
        for j in range(width):
            if tmp[i,j] == 0:
                arr.append(np.array([i,j]))
    l = width
    t = height
    r = 0
    b = 0
    for pt in arr:
        if pt[0] <l:
            l = pt[0]
        if pt[0] > r:
            r = pt[0]
        if pt[1] <t:
            t = pt[1]
        if pt[1] > b:
            b = pt[1]
    green = (0, 255, 0)
    im_plt = im
    cv2.rectangle(im_plt, (t-itr, l-itr), (b-itr, r-itr), green,2)# 膨胀和腐蚀造成的坐标偏差

    # cv2.imshow("tmp",tmp)
    cv2.imshow("license position",im_plt)

    license = im_gray_bin[l-itr:r-itr,t-itr:b-itr]
    cv2.imshow("license", license)
    # 获得车牌后按位置拆分每个字符即可

    cv2.waitKey(0)

    print("Finished.")