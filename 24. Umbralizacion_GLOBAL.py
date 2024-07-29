import cv2

image = cv2.imread('./Imagenes/7.jpg')

# Convertimos a escala de grises
grises = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Umbral experimental del paso anterior
umbral = 50

# Umbral Binario
retVal, dst = cv2.threshold(grises, umbral, 255, cv2.THRESH_BINARY)

# Umbral Binario Invertido
#retVal, dst = cv2.threshold(grises, umbral, 255, cv2.THRESH_BINARY_INV)

# Umbral Truncar
#retVal, dst = cv2.threshold(grises, umbral, 255, cv2.THRESH_TRUNC)

# Umbral Ajustar a Cero 
#retVal, dst = cv2.threshold(grises, umbral, 255, cv2.THRESH_TOZERO)

# Umbral Ajustar a Cero Invertido
#retVal, dst = cv2.threshold(grises, umbral, 255, cv2.THRESH_TOZERO_INV)

cv2.imshow('umbral', image)
cv2.imshow('grises', grises)
cv2.imshow('resultado', dst)

cv2.waitKey(0)
cv2.destroyAllWindows()
