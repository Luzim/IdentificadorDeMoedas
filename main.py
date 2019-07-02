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
    h,s,v = image.open_and_convert_rgb('./images/',sys.argv[1]) # Convertendo imagem original para HSV
    h_first_pixel = image.identify_fist_pixel(h,s,v) # Fundo
    img = cv2.merge((h,s,v))
    img = image.remove_allDiferent_from_firstPixel_rgb(h_first_pixel,img)
    # Mediana para retirar ruídos
    h,s,v = cv2.split(img)
    h = cv2.medianBlur(h,7) 
    s = cv2.medianBlur(s,7)
    v = cv2.medianBlur(v,7)
    # Merge HSV resultante    
    img = cv2.merge((h,s,v))
    img_aux = img.copy()
    opening = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
    #opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel,iterations=5)
    #
    #opening = cv2.erode(img,kernel,iterations = )
    #Transformando as moedas em branco
    #img_aux = image.transform_black_white(img_aux)
    #Transformando as moedas em branco
    #Identificando Quantidade de Moedas - IMPLEMENTANDO
    moedas_identifyed = image.identify_coins(opening)
    #VERIFICANDO CORES
    #print('Componentes',len(moedas_identifyed))
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
        print(str(aux[12]) + " - "+str(aux2[12])+" - "+str(aux3[12])) 
    print("-----------------------------")
    for key in moedas_identifyed:
        i = int(moedas_identifyed[key][0]['centroid'][1])
        left = int(moedas_identifyed[key][0]['left_pixel']+moedas_identifyed[key][0]['diameter_x']/9)
        #right = int(moedas_identifyed[key][0]['right_pixel']-moedas_identifyed[key][0]['diameter_x']/9)
        aux = []
        #aux2 = []
        aux3 = []
        #aux4 = []
        aux5 = []
        #aux6 = []
        for x in range(5):
            for y in range(5):
                aux.append(opening[i+x-2][left+y-2][0])
                #aux2.append(opening[i+x-2][right+y-2][0])
                aux3.append(opening[i+x-2][left+y-2][1])
                #aux4.append(opening[i+x-2][right+y-2][1])
                aux5.append(opening[i+x-2][left+y-2][2])
                #aux6.append(opening[i+x-2][right+y-2][2])
        aux.sort()
        #aux2.sort()
        aux3.sort()
        #aux4.sort()
        aux5.sort()
        #aux6.sort()
        moedas_identifyed[key][0]['borderL_r'] = aux[12]
        moedas_identifyed[key][0]['borderL_g'] = aux3[12]
        moedas_identifyed[key][0]['borderL_b'] = aux5[12]
        print(str(aux[12]) + " - "+str(aux3[12])+" - "+str(aux5[12])) 
        #moedas_identifyed[key][0]['borderR_r'] = aux2[12]
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
            if ((moedas_identifyed[key][0]['centroid_color_g'] >= 210) and (moedas_identifyed[key][0]['centroid_color_g'] <= 230)):
                result_gold.append(moedas_identifyed[key][0]['diameter_x'])
        elif ((moedas_identifyed[key][0]['centroid_color_r'] >= 230) and (moedas_identifyed[key][0]['centroid_color_r'] <= 255)):
            if ((moedas_identifyed[key][0]['centroid_color_g'] >= 180) and (moedas_identifyed[key][0]['centroid_color_g'] <= 210)):
                result_gold.append(moedas_identifyed[key][0]['diameter_x'])
    
    result = 0
    if len(result_gold) >=2:
        valor_25,valor_10 = image.compare_general(result_gold)
        result = result + valor_10*0.1 + valor_25*0.25
#        print(valor_25,valor_10)
    if len(result_copper)>=2:
        valor_5,valor_01 = image.compare_general(result_copper)
        result = result + valor_5*0.05 + valor_01*0.01
 #       print(valor_5,valor_01)
    if len(result_silver)>=2:
        valor_1,valor_50 = image.compare_general(result_silver)
        result = result + valor_1*1.0 + valor_50*0.5
  #      print(valor_1,valor_50)
    print(result)
        

    h,s,v = cv2.split(opening)
    #Identificando Quantidade de Moedas - IMPLEMENTANDO
    #Contando diâmetro de cada moeda:
    img2 = cv2.cvtColor(opening,cv2.COLOR_HSV2RGB)
    r,g,b = cv2.split(opening)
    plt.imshow(img)
    plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
    plt.show()

if __name__ == '__main__':
    main()
    
