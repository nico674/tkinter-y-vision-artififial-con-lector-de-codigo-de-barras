import cv2

img = cv2.imread('./Imagenes/10.jpg',1)

# 1. FILTRO PROMEDIADO
promediado = cv2.blur(img,(3,3))
promediado1 = cv2.blur(img,(5,5))
promediado2 = cv2.blur(img,(10,10))

cv2.imshow('Imagen Original',img)
cv2.imshow('Suavizado - Promedio',promediado)
cv2.imshow('Suavizado - Promedio 1',promediado1)
cv2.imshow('Suavizado - Promedio 2',promediado2)

cv2.waitKey(0)
cv2.destroyAllWindows()
