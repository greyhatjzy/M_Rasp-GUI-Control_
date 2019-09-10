import cv2
import os
import numpy as np


# TODO:
# 1.增加鲁棒性，对真实场景图像
# 2.判断孔内有无试管

def tubeinside():
    # 判断是否有试管在内部
    pass


if __name__ == '__main__':

    # 分为两步，1.定位出试管盒 2.定位出试管孔，并判断有没有插
    # 膨胀腐蚀等操作得到试管盒，在试管盒内部找圆，根据截取圆心所在适当大小送入分类器判断是否有试管

    os.chdir('/home/jzy/Desktop/M_Rasp-GUI-Control_')
    image_path = './Data/004.jpg'
    img = cv2.imread(image_path)

    greyimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, result_img = cv2.threshold(greyimg, 0, 255, cv2.THRESH_OTSU)
    # im_at_mean = cv2.adaptiveThreshold(greyimg, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,20, 0)

    # 膨胀腐蚀,得到试管盒位置,
    # 超参数可以变成根据边长的变量，更合理
    kernel = np.ones((50, 50), np.uint8)
    opening = cv2.morphologyEx(result_img, cv2.MORPH_OPEN, kernel)
    kernel = np.ones((30, 30), np.uint8)
    closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)

    # 找出轮廓
    contours, hierarchy = cv2.findContours(closing, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    draw_img0 = cv2.drawContours(img.copy(), contours, 0, (0, 255, 255), 3)
    # print('contours',contours)

    # 根据左上角点画出矩形,切割出试管盒
    for i in range(0, len(contours)):
        x, y, w, h = cv2.boundingRect(contours[i])
        cv2.rectangle(img, (x, y), (x + w, y + h), (153, 153, 0), 5)
    box = img[y + 2:y + h - 2, x + 2:x + w - 2]
    box_origin = [y, x]
    print('试管盒坐标偏移：', box_origin)

    # 在切割出的图片中识别圆
    greybox = cv2.cvtColor(box, cv2.COLOR_BGR2GRAY)
    # _, result_box = cv2.threshold(greybox, 0, 255, cv2.THRESH_OTSU)
    circles = cv2.HoughCircles(greybox, cv2.HOUGH_GRADIENT, 1, 20, param1=50, param2=30, minRadius=20, maxRadius=50)
    #
    print(circles)
    circles = np.uint16(np.around(circles))

    for i in circles[0, :]:
        # draw the outer circle
        cv2.circle(img, (i[0], i[1]), i[2], (0, 255, 0), 2)
        # draw the center of the circle
        cv2.circle(img, (i[0], i[1]), 2, (0, 0, 255), 2)

    cv2.imshow('detected circles1', greybox)
    cv2.imshow('detected circles', box)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
