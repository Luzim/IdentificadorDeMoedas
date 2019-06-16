import cv2
import numpy as np
class Manipulate_images(object):

    def open_and_convert(self, path,file):
        bgr_img = cv2.imread(path+file)
        img = cv2.cvtColor(bgr_img,cv2.COLOR_BGR2HSV)
        h,s,v = cv2.split(img)
        return h,s,v
    def identify_fist_pixel(self,h,s,v):
        HSV_pixel = np.uint8([[[h[0][0],s[0][0],v[0][0] ]]])
        return HSV_pixel
    def remove_allDiferent_from_firstPixel(self,pixel,image,case):
        for x in range(image.shape[0]):
            for y in range(image.shape[1]):
                if case == 'h':
                    if pixel[0][0] == image[x][y] :
                        image[x][y] = 0
                elif case == 's':
                    if pixel[0][1] == image[x][y] :
                        image[x][y] = 0
                elif case == 'v':
                    if pixel[0][2] == image[x][y] :
                        image[x][y] = 0
        return image
    def transform_black_white(self,hsv_image):
        for x in range(hsv_image.shape[0]):
            for y in range(hsv_image.shape[1]):
                if not np.array_equal(hsv_image[x][y],[0,0,0]):
                    hsv_image[x][y] = np.uint8([0,0,255])
        return hsv_image
    def identify_coins(self,image):
        dict_coins = {}
        att = 'Black'
        coin = 0
        for x in range(image.shape[0]):
            coins = []
            for y in range(image.shape[1]):
                if np.array_equal(image[x][y],[0,0,255]) and (att=='Black'):
                    att='White'
                    coins.append([x,y])
                elif np.array_equal(image[x][y],[0,0,255]) and (att=='White'):
                    coins.append([x,y])
                elif np.array_equal(image[x][y],[0,0,0]) and (att=='White'):
                    att='Black'
                    dict_coins[coin] = coins
                    coins = []
            att='Black'

                    
                

    
        