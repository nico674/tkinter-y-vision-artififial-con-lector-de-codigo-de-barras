import cv2

img = cv2.imread('./Imagenes/10.jpg',1)

# 4. FILTRO BILATERAL
bilateral = cv2.bilateralFilter(img,15,200,200)

cv2.imshow('Imagen Original',img)
cv2.imshow('Suavizado - Bilateral',bilateral)

cv2.waitKey(0)
cv2.destroyAllWindows()
