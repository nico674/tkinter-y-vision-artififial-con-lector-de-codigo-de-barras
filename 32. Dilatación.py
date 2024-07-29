import cv2
import numpy as np

img = cv2.imread('./Imagenes/11.png',0)
kernel = np.ones((5,5),np.uint8)

# DILATACION
dilatacion1 = cv2.dilate(img,kernel,iterations = 1)
dilatacion2 = cv2.dilate(img,kernel,iterations = 3)

cv2.imshow('Imagen Original',img)
cv2.imshow('Imagen Dilatada Iteracion 1',dilatacion1)
cv2.imshow('Imagen Dilatada Iteracion 3',dilatacion2)

cv2.waitKey(0)
cv2.destroyAllWindows()
