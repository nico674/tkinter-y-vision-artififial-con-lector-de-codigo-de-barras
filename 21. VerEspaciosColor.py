import cv2

#Metodos de conversión
flags = [i for i in dir(cv2) if i.startswith('COLOR_')]
print(len(flags))
print(flags)
