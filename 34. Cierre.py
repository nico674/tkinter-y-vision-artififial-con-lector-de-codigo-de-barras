import cv2
import numpy as np

img = cv2.imread('./Imagenes/13.png',0)
kernel = np.ones((5,5),np.uint8)

# CIERRE
cierre = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

cv2.imshow('Imagen Original',img)
cv2.imshow('Imagen - CIERRE',cierre)

cv2.waitKey(0)
cv2.destroyAllWindows()
