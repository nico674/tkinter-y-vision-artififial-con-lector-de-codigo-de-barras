import cv2
import numpy as np
from PIL import Image, ImageTk
from tkinter import *

# Cargar la imágen dos veces
img1 = cv2.imread(r"./Imagenes/hojas.jpg",1) 
img = cv2.imread(r"./Imagenes/hojas.jpg",1) 
# Convertir a escala de grises
gris = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
bilateral = cv2.bilateralFilter(gris,15,100,200)

# Umbralización
umbral=235
retVal, dst = cv2.threshold(gris, umbral, 255, cv2.THRESH_BINARY_INV)

# Rellenar imágen umbralizada
kernel = np.ones((5,5),np.uint8)
cierre = cv2.morphologyEx(dst, cv2.MORPH_CLOSE, kernel)

#gradiente
#kernel = np.ones((5,5),np.uint8)
#gradiente = cv2.morphologyEx(img1, cv2.MORPH_GRADIENT, kernel)

###
kernel = np.ones((3,3),np.uint8)
apertura = cv2.morphologyEx(cierre, cv2.MORPH_OPEN, kernel)

# Encontrar contornos
contornos, hierarchy = cv2.findContours(cierre.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
print("Cantidad de contornos: ", len(contornos))

# Contador de contornos
n = 0
# Cálculo de área y centroide
for i, c in enumerate(contornos):

    n = n + 1

    # Calcular centro del rectángulo delimitador
    x, y, w, h = cv2.boundingRect(c)
    cx = x + w // 2
    cy = y + h // 2

    # Cálculo del Area
    area = cv2.contourArea(c)
    print('Area de Contorno de la hoja: ',area)

    # Dibujar contorno de la hoja
    cv2.drawContours(img1, [c],-1,(255, 100, 100), 2)

    # Dibujar número de la hoja
    sz1 = cv2.getTextSize(str(n),cv2.FONT_HERSHEY_SIMPLEX,1,2)
    cv2.putText(img1,str(n),(cx-sz1[0][0]//2,cy-sz1[0][1]//2),cv2.FONT_HERSHEY_SIMPLEX,1,(0, 0, 0),2)
    
    # Dibujar área de la hoja
    sz2 = cv2.getTextSize(str(area),cv2.FONT_HERSHEY_SIMPLEX,0.7,2)
    cv2.putText(img1,str(area),(cx-sz2[0][0]//2,cy+sz2[0][1]),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0, 0, 0),2)


# Guardar la imagen
cv2.imwrite('./Imagenes/Numero_de_hojas.jpg',img=img1)


cv2.imshow("Imagen Original", img1)
cv2.imshow("Escala de grises", gris)
cv2.imshow("Imagen umbralizada y rellenada", cierre)
cv2.imshow("Imagen con contorno, numero de hoja y area", img)

cv2.waitKey(0)
cv2.destroyAllWindows()


# Crear una ventana de Tkinter
window = tk.Tk()
window.title("Detector de Hojas")

# Crear un panel para mostrar la imagen
panel = tk.Label(root)
panel.pack(padx=10, pady=10)

# Botón para detectar hojas
btn_detect = tk.Button(root, text="Detectar Hojas", command=detect_leaves)
btn_detect.pack(pady=5)

# Botón para salir
btn_exit = tk.Button(root, text="Salir", command=root.destroy)
btn_exit.pack(pady=5)

# Ejecutar la aplicación
root.mainloop()
