import cv2
import numpy as np
import matplotlib.pyplot as plt
from copy import copy, deepcopy
from manipulate_images import Manipulate_images as mi
def main():
    image = mi()
    kernel = np.ones((3,3),np.uint8)
    h,s,v = image.open_and_convert('./images/','treino.jpg') # Convertendo imagem original para HSV
    h_first_pixel = image.identify_fist_pixel(h,s,v) # Fundo
    h = image.remove_allDiferent_from_firstPixel(h_first_pixel[0],h,'h')
    s = image.remove_allDiferent_from_firstPixel(h_first_pixel[0],s,'s')
    v = image.remove_allDiferent_from_firstPixel(h_first_pixel[0],v,'v')
    # Mediana para retirar ruídos

    h = cv2.medianBlur(h,5) 
    s = cv2.medianBlur(s,5)
    v = cv2.medianBlur(v,5)
    # Merge HSV resultante    
    img = cv2.merge((h,s,v))
    img_aux = img.copy()
    opening = cv2.morphologyEx(img_aux, cv2.MORPH_CLOSE, kernel,iterations=5)
    opening = cv2.morphologyEx(opening, cv2.MORPH_OPEN, kernel,iterations=5)
    opening = cv2.erode(opening,kernel,iterations = 3)
    #Transformando as moedas em branco
    #img_aux = image.transform_black_white(img_aux)
    #Transformando as moedas em branco
    #Identificando Quantidade de Moedas - IMPLEMENTANDO
    moedas_identifyed = image.identify_coins(opening)
    #VERIFICANDO CORES
    for key in moedas_identifyed:
        i = int(moedas_identifyed[key][0]['centroid'][1])
        j = int(moedas_identifyed[key][0]['centroid'][0])
        aux = []
        for x in range(5):
            for y in range(5):
                aux.append(v[i+x-2][j+y-2] )
        aux.sort()
        print(aux[12])
    print("-----------------------------")
    for key in moedas_identifyed:
        i = int(moedas_identifyed[key][0]['centroid'][1])
        left = int(moedas_identifyed[key][0]['left_pixel']+moedas_identifyed[key][0]['diameter_x']/9)
        aux = []
        for x in range(5):
            for y in range(5):
                aux.append(opening[i+x-2][left+y-2][0])
        aux.sort()
        print(aux)
    #MONTANDO E COMPARANDO VALORES
    h,s,v = cv2.split(opening)
    #Identificando Quantidade de Moedas - IMPLEMENTANDO
    #Contando diâmetro de cada moeda:
    img2 = cv2.cvtColor(opening,cv2.COLOR_HSV2RGB)
    r,g,b = cv2.split(opening)
    plt.imshow(v)
    plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
    plt.show()

if __name__ == '__main__':
    main()
    
