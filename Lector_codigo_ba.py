
import cv2
from pyzbar import pyzbar
import numpy as np
import os
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from playsound import *

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
    global cap, root, panel, Detecciones
    
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
                    if Detecciones[codigo] >=  0:
                        print("Deteccion exitosa", codigo)
                        #if os.path.exists("Beep.mp3"):
                            #playsound("Beep.mp3")
                        #else:
                        #    print("El archivo beep.mp3 no se encontró.")
                        cv2.waitKey(250)
                        Detecciones.clear()
                else:
                    Detecciones[codigo] = 1

                x, y, w, h = barcode.rect
                frame = cv2.putText(frame, "Codigo leido", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 128, 0), 4)
                frame = cv2.putText(frame, codigo, (x, y + h + 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 128, 0), 4)
        else:
            h, w, _ = frame.shape
            cv2.rectangle(frame, (w // 4, h // 4), (3 * w // 4, 3 * h // 4), (0, 0, 255), 3)
            frame = cv2.putText(frame, "Escaneando...", (w // 2 - 50, h // 2 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

        # Convertir frame a imagen para tkinter
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(frame)
        imgtk = ImageTk.PhotoImage(image=img)
        panel.imgtk = imgtk
        panel.config(image=imgtk)
    
    root.after(10, detect_and_display)

# Configurar ventana de Tkinter
root = Tk()
root.title("Escaner de Codigos de Barras")

# Configurar la cámara
cap = cv2.VideoCapture(0)
Detecciones = {}

panel = Label(root)
panel.pack(padx=10, pady=10)

# Iniciar la detección y visualización
root.after(0, detect_and_display)
root.mainloop()

cap.release()
cv2.destroyAllWindows()
