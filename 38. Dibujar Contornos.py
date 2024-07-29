import cv2

# Cargamos imagen original
img = cv2.imread('./Imagenes/15.jpg',1)

# Convertimos la a escala de grises
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Usamos la umbralización binaria manual con un umbral de 120.  Usar histograma para ver el umbral.
# Umbral seleccionado: 120
# También puede utilizar el umbral óptimo OTSU
retVal,binary = cv2.threshold(gray, 120, 255, cv2.THRESH_BINARY)

# Buscamos contorno en la imagen
# Usamos una copia de la imagen binaria umbralizada para no dañar la original
# Modo de contorno: cv2.RETR_EXTERNAL, Método de Aproximación: cv2.CHAIN_APPROX_SIMPLEZ
contornos, hierarchy = cv2.findContours(binary.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

print("Cantidad de contornos: ", len(contornos))

cv2.imshow('Imagen Original',img)
cv2.imshow('Imagen Binaria',binary)

# Dibujar Contornos
cv2.drawContours(img, contornos, -1, (0, 0, 255), 3, cv2.LINE_AA)
cv2.imshow('Imagen Original con Contornos',img)

cv2.waitKey(0)
cv2.destroyAllWindows()
