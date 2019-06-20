import sys
import cv2
import numpy as np
import matplotlib.pyplot as plt
from copy import copy, deepcopy
from manipulate_images import Manipulate_images as mi
def main():
    image = mi()
    kernel = np.ones((3,3),np.uint8)
    #kernel = [[0,1,0],[1,1,1],[0,1,0]]
    #kernel = np.uint8(kernel)
    h,s,v = image.open_and_convert('./images/',sys.argv[1]) # Convertendo imagem original para HSV
    h_first_pixel = image.identify_fist_pixel(h,s,v) # Fundo
    h = image.remove_allDiferent_from_firstPixel(h_first_pixel[0],h,'h')
    s = image.remove_allDiferent_from_firstPixel(h_first_pixel[0],s,'s')
    v = image.remove_allDiferent_from_firstPixel(h_first_pixel[0],v,'v')
    # Mediana para retirar ruídos
    
    h = cv2.medianBlur(h,7) 
    s = cv2.medianBlur(s,7)
    v = cv2.medianBlur(v,7)
    # Merge HSV resultante    
    img = cv2.merge((h,s,v))
    img_aux = img.copy()
    #opening = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)
    opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel,iterations=3)
    #
    #opening = cv2.erode(opening,kernel,iterations = 1)
    #Transformando as moedas em branco
    #img_aux = image.transform_black_white(img_aux)
    #Transformando as moedas em branco
    #Identificando Quantidade de Moedas - IMPLEMENTANDO
    moedas_identifyed = image.identify_coins(opening)
    #VERIFICANDO CpORES
    print('Componentes',len(moedas_identifyed))
    for key in moedas_identifyed:
        i = int(moedas_identifyed[key][0]['centroid'][1])
        j = int(moedas_identifyed[key][0]['centroid'][0])
        aux = []
        for x in range(5):
            for y in range(5):
                aux.append(opening[i+x-2][j+y-2][0] )
        aux.sort()
        moedas_identifyed[key][0]['centroid_color'] = aux[12]
    print("-----------------------------")
    for key in moedas_identifyed:
        i = int(moedas_identifyed[key][0]['centroid'][1])
        left = int(moedas_identifyed[key][0]['left_pixel']+moedas_identifyed[key][0]['diameter_x']/9)
        right = int(moedas_identifyed[key][0]['right_pixel']-moedas_identifyed[key][0]['diameter_x']/9)
        aux = []
        aux2 = []
        for x in range(5):
            for y in range(5):
                aux.append(opening[i+x-2][left+y-2][0])
                aux2.append(opening[i+x-2][right+y-2][0])
        aux.sort()
        aux2.sort()
        moedas_identifyed[key][0]['borderL'] = aux[12]
        moedas_identifyed[key][0]['borderR'] = aux2[12]
    #MONTANDO E COMPARANDO VALORES
    ## Resultado
    result_gold = []
    result_copper = []
    result_silver = []
    for key in moedas_identifyed:
        if ((moedas_identifyed[key][0]['centroid_color'] >= 15) and (moedas_identifyed[key][0]['centroid_color'] <= 23)):
            if ((moedas_identifyed[key][0]['borderL'] >= 15) and (moedas_identifyed[key][0]['borderL'] <= 23)):
                if ((moedas_identifyed[key][0]['borderR'] >= 15) and (moedas_identifyed[key][0]['borderR'] <= 23)):
                    print(moedas_identifyed[key][0]['borderR'])
                    result_gold.append(moedas_identifyed[key][0]['diameter_x'])
                else:
                    result_silver.append(moedas_identifyed[key][0]['diameter_x'])
            else:
                result_silver.append(moedas_identifyed[key][0]['diameter_x'])
                
        elif((moedas_identifyed[key][0]['centroid_color'] >= 8) and (moedas_identifyed[key][0]['centroid_color'] <= 14)):
            if((moedas_identifyed[key][0]['borderL'] >= 8) and (moedas_identifyed[key][0]['borderL'] <= 14)):
                result_copper.append(moedas_identifyed[key][0]['diameter_x'])
            else:
                result_silver.append(moedas_identifyed[key][0]['diameter_x'])
        else:
            result_silver.append(moedas_identifyed[key][0]['diameter_x'])
    
    result = 0
    if len(result_gold) >=2:
        valor_25,valor_10 = image.compare_general(result_gold)
        result = result + valor_10*0.1 + valor_25*0.25
        print(valor_25,valor_10)
    if len(result_copper)>=2:
        valor_5,valor_01 = image.compare_general(result_copper)
        result = result + valor_5*0.05 + valor_01*0.01
        print(valor_5,valor_01)
    if len(result_silver)>=2:
        valor_1,valor_50 = image.compare_general(result_silver)
        result = result + valor_1*1.0 + valor_50*0.5
        print(valor_1,valor_50)
    print(result)
        

    h,s,v = cv2.split(opening)
    #Identificando Quantidade de Moedas - IMPLEMENTANDO
    #Contando diâmetro de cada moeda:
    img2 = cv2.cvtColor(opening,cv2.COLOR_HSV2RGB)
    r,g,b = cv2.split(opening)
    plt.imshow(h)
    plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
    plt.show()

if __name__ == '__main__':
    main()
    
