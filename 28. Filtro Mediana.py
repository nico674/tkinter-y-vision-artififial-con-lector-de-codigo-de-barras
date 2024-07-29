import cv2

img = cv2.imread('./Imagenes/10.jpg',1)

# 2. FILTRO MEDIANA
mediana = cv2.medianBlur(img,3) # Kernel 3 x 3
mediana1 = cv2.medianBlur(img,5) # Kernel 3 x 3
mediana2 = cv2.medianBlur(img,11) # Kernel 3 x 3

cv2.imshow('Imagen Original',img)
cv2.imshow('Suavizado - Mediana',mediana)
cv2.imshow('Suavizado 1 - Mediana',mediana1)
cv2.imshow('Suavizado 2 - Mediana',mediana2)

cv2.waitKey(0)
cv2.destroyAllWindows()
