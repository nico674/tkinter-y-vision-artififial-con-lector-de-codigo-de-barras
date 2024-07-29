import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk



# Cargar la imágen dos veces
img1 = cv2.imread(r"./Imagenes/hojas.jpg",1) 
imgoriginal = cv2.imread(r"./Imagenes/hojas.jpg",1) 
# Convertir a escala de grises
gris = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
#bilat = cv2.bilateralFilter(gris,15,100,200)

# Umbralización
umbral=239
retVal, dst = cv2.threshold(gris, umbral, 255, cv2.THRESH_BINARY_INV)

# Rellenar imágen umbralizada
kernel = np.ones((5,5),np.uint8)
close = cv2.morphologyEx(dst, cv2.MORPH_CLOSE, kernel)

#gradiente
#kernel = np.ones((5,5),np.uint8)
#gradiente = cv2.morphologyEx(img1, cv2.MORPH_GRADIENT, kernel)

###
kernel = np.ones((3,3),np.uint8)
apertura = cv2.morphologyEx(close, cv2.MORPH_OPEN, kernel)

# Encontrar contornos
contornos, hierarchy = cv2.findContours(close.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
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
cv2.imshow("Imagen umbralizada y rellenada", close)
cv2.imshow("Imagen con contorno, numero de hoja y area", imgoriginal)


# Crear una ventana de Tkinter
# Función para abrir el explorador de archivos y seleccionar una imagen
def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png *.gif *.bmp *.ppm")])
    if file_path:
        load_and_display_image(file_path)

# Función para cargar y mostrar la imagen en la GUI
def load_and_display_image(file_path):
    image = Image.open(file_path)
    photo = ImageTk.PhotoImage(image)

    # Mostrar la imagen en un widget Label
    image_label.config(image=photo)
    image_label.image = photo

# Crear una ventana
window = tk.Tk()
window.title("Seleccionar y Mostrar Imagen")
window.minsize(width=500, height=100)
window.config(pady=50)
window.minsize(width=500, height=100)
window.config(pady=50, bg="#E0FFFF")  # Light blue background

#########################################################################
#Buttons
#########################################################################
# Crear un botón para abrir el explorador de archivos
#open_button = tk.Button(window, text="Abrir Imagen", command=open_file)
open_button = tk.Button(window, text="Abrir Imagen", command=open_file, 
                        bg="#2196F3", fg="#FFFFFF",
                        font=("Arial", 12, "bold"),
                        borderwidth=2, relief="groove")
open_button.grid(row=5, column=5, padx=10, pady=10)
open_button.pack()

##########################################################################
#Label
#########################################################################
# Crear un widget Label para mostrar la imagen
image_label = tk.Label(window)
image_label.pack()

# Iniciar la ventana
window.mainloop()


cv2.waitKey(0)
cv2.destroyAllWindows()