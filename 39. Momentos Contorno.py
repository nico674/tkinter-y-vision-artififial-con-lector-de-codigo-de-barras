import cv2

# Cargamos imagen original
img = cv2.imread('./Imagenes/16.png',1)

# Convertimos la a escala de grises
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Usamos la umbralización binaria manual con un umbral de 40.  Usar histograma para ver el umbral.
# Umbral seleccionado: 40
# También puede utilizar el umbral óptimo OTSU
_,binary = cv2.threshold(gray, 50, 255, cv2.THRESH_BINARY)

cv2.imshow('Imagen Original',img)
cv2.imshow('Imagen Binaria Original',binary)

# Operaciones morfologicas
mask = cv2.erode(binary,  None, iterations=4)
mask = cv2.dilate(mask, None, iterations=6)
cv2.imshow('Imagen Binaria Filtrada',mask)

# Buscamos contorno en la imagen
contornos,_ = cv2.findContours(mask.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
print("Numero de Contornos: ",len(contornos))

# CALCULO DE AREA
for c in contornos:
    k = cv2.waitKey(0)
    
    # Momentos
    M = cv2.moments(c)

    # Cálculo de centroide
    cx = int(M['m10']/M['m00'])
    cy = int(M['m01']/M['m00'])
    print('Centroide: ',cx,cy)

    # calculo de Area
    area = M['m00']
    area1 = cv2.contourArea(c)
    print('Area de Contorno: ',area)
    print('Area de Contorno1: ',area1)
    
    # Dibujar centroide
    cv2.circle(img,(cx,cy),4,(0,255,0),-1)
    #cv2.circle(img,(cx,cy),5,(255,0,0),2)
    
    cv2.drawContours(img, [c],-1,(0, 0, 255), 2)
    cv2.imshow("Centroide", img)
    
cv2.waitKey(0)
cv2.destroyAllWindows()

