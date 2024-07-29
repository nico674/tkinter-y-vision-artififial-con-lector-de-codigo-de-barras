import cv2
import numpy as np

# Cargamos imagen original
img = cv2.imread('./Imagenes/hojas.jpg',1)

# Convertimos la a escala de grises
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#-----------------------------
kernel = np.ones((5,5),np.uint8)

umbral = 235
retVal, dst = cv2.threshold(gray, umbral, 255, cv2.THRESH_BINARY)
#gradiente = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)


#-----------------------------


# Usamos la umbralización binaria manual con un umbral de 120.  Usar histograma para ver el umbral.
# Umbral seleccionado: 120
# También puede utilizar el umbral óptimo OTSU
#retVal,binary = cv2.threshold(gray, 120, 255, cv2.THRESH_BINARY)
retVal,binary = cv2.threshold(gray,0, 255, cv2.THRESH_BINARY_INV |cv2.THRESH_OTSU)
#print(retVal)


# Buscamos contorno en la imagen
# Usamos una copia de la imagen binaria umbralizada para no dañar la original
# Modo de contorno: cv2.RETR_EXTERNAL, Método de Aproximación: cv2.CHAIN_APPROX_SIMPLEZ
contornos, hierarchy = cv2.findContours(binary.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

#print("Cantidad de contornos: ", len(contornos))


# Dibujar Contornos
#cv2.drawContours(img, contornos, -1, (0, 0, 255), 3, cv2.LINE_AA)

# Umbral Binario
retVal, dst = cv2.threshold(gray,0, 255, cv2.THRESH_BINARY |cv2.THRESH_OTSU)
#retVal, dst = cv2.threshold(gray,0, 255, cv2.THRESH_BINARY_INV |cv2.THRESH_OTSU)
print(retVal)


# Operaciones morfologicas
#mask = cv2.erode(binary,  None, iterations=4)
#mask = cv2.dilate(mask, None, iterations=6)

# Buscamos contorno en la imagen
#contornos,_ = cv2.findContours(mask.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
#print("Numero de Contornos: ",len(contornos))

# Contador de contornos
n = 0

# Cálculo de área y centroide
for i, c in enumerate(contornos):

    n = n + 1

    # Calcular centro del rectángulo delimitador
    x, y, w, h = cv2.boundingRect(c)
    cx = x + w // 2
    cy = y + h // 2

    # Cálculo del Area
    area = cv2.contourArea(c)
    print('Area de Contorno: ',area)

    # Dibujar contorno de la hoja
    cv2.drawContours(img, [c],-1,(0, 0, 255), 2)

    # Dibujar número de la hoja
    sz1 = cv2.getTextSize(str(n),cv2.FONT_HERSHEY_SIMPLEX,1,2)
    cv2.putText(img,str(n),(cx-sz1[0][0]//2,cy-sz1[0][1]//2),cv2.FONT_HERSHEY_SIMPLEX,1,(0, 0, 0),2)
    
    # Dibujar área de la hoja
    sz2 = cv2.getTextSize(str(area),cv2.FONT_HERSHEY_SIMPLEX,0.7,2)
    cv2.putText(img,str(area),(cx-sz2[0][0]//2,cy+sz2[0][1]),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0, 0, 0),2)



# CALCULO DE AREA
#for c in contornos:
  #  k = cv2.waitKey(0)
    
    # Momentos
  #  M = cv2.moments(c)

    # Cálculo de centroide
  #  cx = int(M['m10']/M['m00'])
  #  cy = int(M['m01']/M['m00'])
  #  print('Centroide: ',cx,cy)

    # calculo de Area
  #  area = M['m00']
  #  area1 = cv2.contourArea(c)
  #  print('Area de Contorno: ',area)
  #  print('Area de Contorno1: ',area1)
    
    # Dibujar centroide
  #  cv2.circle(img,(cx,cy),4,(0,255,0),-1)
    #cv2.circle(img,(cx,cy),5,(255,0,0),2)
  #  
 #   cv2.drawContours(img, [c],-1,(0, 0, 255), 2)
#    cv2.imshow("Centroide", img)

# Guardar imagen
cv2.imwrite('./Imagenes/Nhojas.jpg',img=img)



#cv2.imshow('umbral', img)
cv2.imshow('grises', gray)
cv2.imshow('resultado', dst)  
cv2.imshow('Imagen Original con Contornos',img)


cv2.waitKey(0)
cv2.destroyAllWindows()
