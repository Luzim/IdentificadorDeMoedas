import cv2
import numpy as np
import matplotlib.pyplot as plt
from copy import copy, deepcopy

bgr_img = cv2.imread('images/treino.jpg')
img = cv2.cvtColor(bgr_img,cv2.COLOR_BGR2HSV)
h,s,v = cv2.split(img)

plt.imshow(v)
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()