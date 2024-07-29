"""
import cv2
from pyzbar import pyzbar
from playsound import playsound
import numpy as np
import os

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
    # Convertir a escala de grises
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Aplicar desenfoque gaussiano para reducir el ruido
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    
    # Aplicar umbralización adaptativa para mejorar el contraste
    thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
                                   cv2.THRESH_BINARY, 11, 2)
    
    return thresh

cap = cv2.VideoCapture(0)
Detecciones = {}

while True:
    ret, frame = cap.read()
    if ret:
        # Preprocesar la imagen
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
                    if Detecciones[codigo] >= 30:
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
            # Mostrar un rectángulo rojo en el centro de la pantalla si no se detecta ningún código de barras
            h, w, _ = frame.shape
            cv2.rectangle(frame, (w // 4, h // 4), (3 * w // 4, 3 * h // 4), (0, 0, 255), 3)
            frame = cv2.putText(frame, "Escaneando...", (w // 2 - 50, h // 2 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
        
        cv2.imshow("escaner de barras", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()

"""
import cv2
from pyzbar import pyzbar
from playsound import playsound
import numpy as np
import os

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

cap = cv2.VideoCapture(0)
Detecciones = {}

while True:
    ret, frame = cap.read()
    if ret:
        with SuppressStderr():  # Suprimir advertencias de ZBar
            barcodes = pyzbar.decode(frame)
        
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
                    if Detecciones[codigo] >= 30:
                        print("Deteccion exitosa", codigo)
                        playsound("beep.mp3")
                        cv2.waitKey(250)
                        Detecciones.clear()
                else:
                    Detecciones[codigo] = 1

                x, y, w, h = barcode.rect
                frame = cv2.putText(frame, "Codigo leido", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
                frame = cv2.putText(frame, codigo, (x, y + h + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
        else:
            # Mostrar un rectángulo rojo en el centro de la pantalla si no se detecta ningún código de barras
            h, w, _ = frame.shape
            cv2.rectangle(frame, (w // 4, h // 4), (3 * w // 4, 3 * h // 4), (0, 0, 255), 3)
            frame = cv2.putText(frame, "Escaneando...", (w // 2 - 50, h // 2 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
        
        cv2.imshow("escaner de barras", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
