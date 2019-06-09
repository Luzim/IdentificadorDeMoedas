import cv2
import numpy as np
import matplotlib.pyplot as plt
from copy import copy, deepcopy
from manipulate_images import Manipulate_images as mi
def main():
    image = mi()
    h,s,v = image.open_and_convert('./images/','treino.jpg')
    bgr_img = cv2.imread('./images/treino.jpg')
    img = cv2.cvtColor(bgr_img,cv2.COLOR_BGR2GRAY)
    h_first_pixel = image.identify_fist_pixel(h,s,v)
    print(h_first_pixel)
    #h = image.remove_allDiferent_from_firstPixel(h_first_pixel,h)
    plt.imshow(img,cmap = plt.get_cmap('gray'))
    plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
    plt.show()

if __name__ == '__main__':
    main()
    
