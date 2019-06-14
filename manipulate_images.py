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
    
        