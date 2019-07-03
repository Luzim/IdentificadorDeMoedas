#coding: utf-8
import sys
import cv2
import numpy as np
import matplotlib.pyplot as plt
from copy import copy, deepcopy
from manipulate_images import Manipulate_images as mi
def main():
    image = mi()
    kernel = np.ones((3,3),np.uint8)
    h,s,v = image.open_and_convert_rgb('./images/',sys.argv[1]) # Convertendo imagem original para HSV
    h_first_pixel = image.identify_fist_pixel(h,s,v) # Fundo
    img = cv2.merge((h,s,v))
    img = image.remove_allDiferent_from_firstPixel_rgb(h_first_pixel,img)
    # Mediana para retirar ruídos
    h,s,v = cv2.split(img)
    h = cv2.medianBlur(h,7) 
    s = cv2.medianBlur(s,7)
    v = cv2.medianBlur(v,7)
    # Merge RGB resultante    
    img = cv2.merge((h,s,v))
    img_aux = img.copy()
    opening = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
    
    #Identificando moedas
    moedas_identifyed = image.identify_coins(opening)
    
    #VERIFICANDO CORES
    
    for key in moedas_identifyed:
        i = int(moedas_identifyed[key][0]['centroid'][1])
        j = int(moedas_identifyed[key][0]['centroid'][0])
        aux = []
        aux2 = []
        aux3 = []
        for x in range(5):
            for y in range(5):
                aux.append(opening[i+x-2][j+y-2][0] )
                aux2.append(opening[i+x-2][j+y-2][1] )
                aux3.append(opening[i+x-2][j+y-2][2] )
        aux.sort()
        aux2.sort()
        aux3.sort()
        moedas_identifyed[key][0]['centroid_color_r'] = aux[12]
        moedas_identifyed[key][0]['centroid_color_g'] = aux2[12]
        moedas_identifyed[key][0]['centroid_color_b'] = aux3[12]
    
    #MONTANDO E COMPARANDO VALORES
    ## Resultado
    result_gold = []
    result_copper = []
    result_silver = []
    for key in moedas_identifyed:
        if ((moedas_identifyed[key][0]['centroid_color_r'] >= 180) and (moedas_identifyed[key][0]['centroid_color_r'] <= 210)):
            if ((moedas_identifyed[key][0]['centroid_color_g'] >= 180) and (moedas_identifyed[key][0]['centroid_color_g'] <= 210)):
                result_silver.append(moedas_identifyed[key][0]['diameter_x'])
        elif ((moedas_identifyed[key][0]['centroid_color_r'] >= 230) and (moedas_identifyed[key][0]['centroid_color_r'] <= 255)):
            if ((moedas_identifyed[key][0]['centroid_color_g'] > 210) and (moedas_identifyed[key][0]['centroid_color_g'] <= 230)):
                result_gold.append(moedas_identifyed[key][0]['diameter_x'])
            elif ((moedas_identifyed[key][0]['centroid_color_g'] >= 180) and (moedas_identifyed[key][0]['centroid_color_g'] <= 210)):
                result_copper.append(moedas_identifyed[key][0]['diameter_x'])
        elif ((moedas_identifyed[key][0]['centroid_color_r'] >= 155) and (moedas_identifyed[key][0]['centroid_color_r'] <= 175)):
            if ((moedas_identifyed[key][0]['centroid_color_g'] >= 110) and (moedas_identifyed[key][0]['centroid_color_g'] <= 130)):
                result_copper.append(moedas_identifyed[key][0]['diameter_x'])
    	
    result = 0
    if len(result_gold) >=2:
        valor_25,valor_10 = image.compare_general(result_gold)
        print('Moedas de 25 centavos: ', valor_25)
        print('Moedas de 10 centavos: ', valor_10)
        result = result + valor_10*0.1 + valor_25*0.25
    if len(result_copper)>=2:
        valor_5,valor_01 = image.compare_general(result_copper)
        print('Moedas de 5 centavos: ', valor_5)
        print('Moedas de 1 centavo: ', valor_01)
        result = result + valor_5*0.05 + valor_01*0.01
    if len(result_silver)>=2:
        valor_1,valor_50 = image.compare_general(result_silver)
        print('Moedas de 1 real: ', valor_1)
        print('Moedas de 50 centavos: ', valor_50)
        result = result + valor_1*1.0 + valor_50*0.5
    print(result)
        

    #Identificando Quantidade de Moedas - IMPLEMENTANDO
    #Contando diâmetro de cada moeda:
    plt.title('R$ '+str(result))
    plt.imshow(img)
    plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
    plt.show()

if __name__ == '__main__':
    main()
    
