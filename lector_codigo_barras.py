import cv2
from pyzbar import pyzbar
import numpy as np
import os
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from playsound import playsound

# Redirigir stderr para suprimir las advertencias de ZBar
class SuppressStderr:
    def __init__(self):
        self.null_fds = [os.open(os.devnull, os.O_RDWR)]
        self.saved_fds = [os.dup(2)]

    def __enter__(self):
        os.dup2(self.null_fds[0], 2)

    def __exit__(self, *_):
        os.dup2(self.saved_fds[0], 2)
        for fd in self.null_fds + self.saved_fds:
            os.close(fd)

def preprocess_image(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
                                   cv2.THRESH_BINARY, 11, 2)
    return thresh

def detect_and_display():
    global cap, root, panel_original, panel_filtered, Detecciones
    
    ret, frame = cap.read()
    if ret:
        preprocessed_frame = preprocess_image(frame)
        
        with SuppressStderr():  # Suprimir advertencias de ZBar
            barcodes = pyzbar.decode(preprocessed_frame)
        
        if barcodes:
            for barcode in barcodes:
                puntos = barcode.polygon

                if len(puntos) == 4:
                    puntos = [(p.x, p.y) for p in puntos]
                    puntos = np.array(puntos, dtype=np.int32).reshape((-1, 1, 2))
                    frame = cv2.polylines(frame, [puntos], True, (0, 255, 0), 3)

                codigo = barcode.data.decode('utf-8')
                print(f"Codigo detectado: {codigo}")

                if codigo in Detecciones:
                    Detecciones[codigo] += 1
                    if Detecciones[codigo] >= 0:
                        print("Deteccion exitosa", codigo)
                        if os.path.exists("beep.mp3"):
                            playsound("beep.mp3")
                        else:
                            print("El archivo beep.mp3 no se encontró.")
                        cv2.waitKey(250)
                        Detecciones.clear()
                else:
                    Detecciones[codigo] = 1

                x, y, w, h = barcode.rect
                frame = cv2.putText(frame, "Codigo leido", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
                frame = cv2.putText(frame, codigo, (x, y + h + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
        else:
            h, w, _ = frame.shape
            cv2.rectangle(frame, (w // 4, h // 4), (3 * w // 4, 3 * h // 4), (0, 0, 255), 3)
            frame = cv2.putText(frame, "Escaneando...", (w // 2 - 50, h // 2 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

        # Convertir frame original a imagen para tkinter
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img_original = Image.fromarray(frame_rgb)
        imgtk_original = ImageTk.PhotoImage(image=img_original)
        panel_original.imgtk = imgtk_original
        panel_original.config(image=imgtk_original)

        # Convertir frame preprocesado a imagen para tkinter
        preprocessed_frame_rgb = cv2.cvtColor(preprocessed_frame, cv2.COLOR_GRAY2RGB)
        img_filtered = Image.fromarray(preprocessed_frame_rgb)
        imgtk_filtered = ImageTk.PhotoImage(image=img_filtered)
        panel_filtered.imgtk = imgtk_filtered
        panel_filtered.config(image=imgtk_filtered)
    
    root.after(10, detect_and_display)

# Configurar ventana de Tkinter
root = Tk()
root.title("Escaner de Codigos de Barras")

# Configurar la cámara
cap = cv2.VideoCapture(0)
Detecciones = {}

# Crear paneles para mostrar el video original y el video filtrado
panel_original = Label(root)
panel_original.pack(side="left", padx=10, pady=10)

panel_filtered = Label(root)
panel_filtered.pack(side="right", padx=10, pady=10)

# Iniciar la detección y visualización
root.after(0, detect_and_display)
root.mainloop()

cap.release()
cv2.destroyAllWindows()

"""
import cv2
from playsound import playsound

bd = cv2.barcode.BarcodeDetector()
cap = cv2.VideoCapture(0)

Detecciones = {}

while True:
    ret, frame = cap.read()
    if ret:
        (ret_bc, decode, puntos) = bd.detectAndDecode(frame)
        print("puntos:",puntos)        
        print("retangulo:",ret_bc) 
        print("decode:",decode) 

        if ret_bc:
            if puntos is not None:
                frame = cv2.polylines(frame, [punto.astype(int) for punto in puntos], True, (0,255,0), 3)
                
                # Verifica que cada grupo de puntos tenga la longitud esperada (4 para un cuadrilátero)
                if all(len(punto) == 4 for punto in puntos):
                    #frame = cv2.polylines(frame, [punto.astype(int) for punto in puntos], True, (0,255,0), 3)
                    
                    for codigo, punto in zip(decode, puntos):
                        if codigo in Detecciones:
                            Detecciones[codigo] += 1
                            if Detecciones[codigo] >= -1:
                                print("Deteccion exitosa", codigo)
                                playsound("beep.mp3")
                                cv2.waitKey(250)
                                Detecciones.clear()
                        else:
                            Detecciones[codigo] = 1
                        
                        frame = cv2.putText(frame, codigo, tuple(punto[1].astype(int)), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,0,255), 2, cv2.LINE_AA)
        cv2.imshow("escaner de barras", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
"""

"""
import cv2
#from pyzbar import pyzbar
#import numpy as np
from playsound import playsound

bd = cv2.barcode.BarcodeDetector()
cap = cv2.VideoCapture(0)

Detecciones = {}

while True:
    ret, frame = cap.read()
    if ret:
        (ret_bc,decode,puntos) = bd.detectAndDecode(frame)
        print(puntos)
    if ret_bc:
    
        frame = cv2.polylines(frame, puntos.astype(int),True,(0,255,0),3)
        for codigo, punto in zip(decode, puntos):
            if codigo in Detecciones:
                Detecciones[codigo] +=1
                if Detecciones [codigo] >=1:
                    print("Deteccion exitosa",codigo)
                    playsound("beep.mp3")
                    cv2.waitKey(250)
                    Detecciones.clear()
                else:
                    Detecciones[codigo] = 1
                    
                frame = cv2.putText(frame,codigo,punto[1].astype(int),cv2.FONT_HERSHEY_SIMPLEX,2,(0,0,255),2,cv2.LINE_AA)
    cv2.imshow("escaner de barras", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break    
"""

"""
def read_barcode(image_path):
    image = cv2.imread("Imagenes/barcode_qrcode.jpg")
    barcodes = pyzbar.decode(image)

    for barcode in barcodes:
        barcode_data = barcode.data.decode("utf-8")
        barcode_type = barcode.type

print("Barcode Type:", barcode_type)
print("Barcode Data:", barcode_data)

image_path = "barcode_image.jpg"
read_barcode(image_path)
"""
"""
from PIL import Image, ImageDraw, ImageFont
from pyzbar.pyzbar import decode

img = Image.open('Imagenes/barcode_qrcode.jpg')

draw = ImageDraw.Draw(img)
font = ImageFont.truetype('arial.ttf', size=20)  # Set 'arial.ttf' for Windows

for d in decode(img):
    draw.rectangle(((d.rect.left, d.rect.top), (d.rect.left + d.rect.width, d.rect.top + d.rect.height)),
                   outline=(0, 0, 255), width=3)
    draw.polygon(d.polygon, outline=(0, 255, 0), width=3)
    draw.text((d.rect.left, d.rect.top + d.rect.height), d.data.decode(),
              (255, 0, 0), font=font)

img.save('Imagenes/barcode_qrcode_pillow.jpg')
"""