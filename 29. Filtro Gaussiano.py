import cv2

img = cv2.imread('./Imagenes/10.jpg',1)

# 3. FILTRO GAUSSIANO
gausiano = cv2.GaussianBlur(img,(3,3),50)
gausiano1 = cv2.GaussianBlur(img,(5,5),50)
gausiano2 = cv2.GaussianBlur(img,(7,7),50)
gausiano3 = cv2.GaussianBlur(img,(11,11),50)

cv2.imshow('Imagen Original',img)
cv2.imshow('Suavizado - Gaussiano',gausiano)
cv2.imshow('Suavizado - Gaussiano 1',gausiano1)
cv2.imshow('Suavizado - Gaussiano 2',gausiano2)
cv2.imshow('Suavizado - Gaussiano 3',gausiano3)

cv2.waitKey(0)
cv2.destroyAllWindows()
