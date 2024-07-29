import cv2

imagen = cv2.imread('./Imagenes/8.jpg',1)

# Convertimos a escala de grises
gray = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

# Umbral Binario
#retVal, dst = cv2.threshold(gray,0, 255, cv2.THRESH_BINARY |cv2.THRESH_OTSU)
retVal, dst = cv2.threshold(gray,0, 255, cv2.THRESH_BINARY_INV |cv2.THRESH_OTSU)
print(retVal)

cv2.imshow('umbral', imagen)
cv2.imshow('grises', gray)
cv2.imshow('resultado', dst)

cv2.waitKey(0)
cv2.destroyAllWindows()
