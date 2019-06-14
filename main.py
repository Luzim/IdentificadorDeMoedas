import cv2
import numpy as np
import matplotlib.pyplot as plt
from copy import copy, deepcopy
from manipulate_images import Manipulate_images as mi
def main():
    image = mi()
    h,s,v = image.open_and_convert('./images/','treino.jpg')
    h_first_pixel = image.identify_fist_pixel(h,s,v)
    
    h = image.remove_allDiferent_from_firstPixel(h_first_pixel[0],h,'h')
    s = image.remove_allDiferent_from_firstPixel(h_first_pixel[0],s,'s')
    v = image.remove_allDiferent_from_firstPixel(h_first_pixel[0],v,'v')
    h = cv2.medianBlur(h,3)
    s = cv2.medianBlur(s,3)
    v = cv2.medianBlur(v,3)
    
    #plt.imshow(img,cmap = plt.get_cmap('gray'))
    img = cv2.merge((h,s,v))
    img = cv2.cvtColor(img,cv2.COLOR_HSV2RGB)
    plt.imshow(img)
    plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
    plt.show()

if __name__ == '__main__':
    main()
    
