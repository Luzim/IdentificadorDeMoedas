import cv2
import numpy as np
import matplotlib.pyplot as plt
from copy import copy, deepcopy
from manipulate_images import Manipulate_images as mi
def main():
    image = mi()
    h,s,v = image.open_and_convert('./images/','treino.jpg') # Convertendo imagem original para HSV
    h_first_pixel = image.identify_fist_pixel(h,s,v) # Fundo
    h = image.remove_allDiferent_from_firstPixel(h_first_pixel[0],h,'h')
    s = image.remove_allDiferent_from_firstPixel(h_first_pixel[0],s,'s')
    v = image.remove_allDiferent_from_firstPixel(h_first_pixel[0],v,'v')
    # Mediana para retirar ruídos
    h = cv2.medianBlur(h,3) 
    s = cv2.medianBlur(s,3)
    v = cv2.medianBlur(v,3)
    # Mediana para retirar ruídos
    # Merge HSV resultante    
    img = cv2.merge((h,s,v))
    img_aux = img.copy()
    #Transformando as moedas em branco
    img_aux = image.transform_black_white(img_aux)
    #Transformando as moedas em branco
    #Identificando Quantidade de Moedas - IMPLEMENTANDO
    image.identify_coins(img_aux)
    #Identificando Quantidade de Moedas - IMPLEMENTANDO
    #Contando diâmetro de cada moeda:
    img2 = cv2.cvtColor(img_aux,cv2.COLOR_HSV2RGB)
    plt.imshow(img2)
    plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
    plt.show()

if __name__ == '__main__':
    main()
    
