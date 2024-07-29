import cv2
from tkinter import *
from PIL import Image, ImageTk
import tkinter.ttk as ttk

# Función para actualizar el cuadro de la cámara
def update_camera():
    ret, frame = cap.read()
    if ret:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(frame)
        img = ImageTk.PhotoImage(image=img)
        label.img = img
        label.config(image=img)
        label.after(10, update_camera)

# Función para tomar la foto
def take_picture():
    ret, frame = cap.read()
    cv2.imwrite('./Capturas/Foto.png', frame)

# Función para iniciar video
def iniciar_video():
    global photo_button
    # Iniciar la actualización de la cámara
    photo_button.configure(state="active")
    video_button.configure(state="disabled")
    update_camera()

# Inicializar la cámara
cap = cv2.VideoCapture(0)

# Crear una ventana de Tkinter
window = Tk()
window.title("Visualización de la cámara")

#########################################################################
#Frame
#########################################################################
Frame1 = Frame(window)
Frame1.pack(side=TOP, padx=10, pady=10)
Frame1.configure(relief='groove')
Frame1.configure(borderwidth="2")
Frame1.configure(relief="groove")
Frame1.configure(background="#d9d9d9")
Frame1.configure(width=660)
Frame1.configure(height=500)

#########################################################################
#Label
#########################################################################
# Crear un label para mostrar la imagen de la cámara
label = Label(Frame1)
#label.pack(padx=10, pady=10)
label.place(x=10, y=10, width=640, height=480)
label.configure(background="#d9d9d9")

#########################################################################
#Buttons
#########################################################################
# Botón para iniciar captura
video_button = Button(window, text="Iniciar Video", command=iniciar_video)
video_button.pack(pady=10, side=LEFT, padx=100)

# Botón para cerrar la ventana
quit_button = Button(window, text="Cerrar", command=window.destroy)
quit_button.pack(pady=10, side=LEFT, padx=100)

# Botón para tomar foto
photo_button = Button(window, text="Capturar Foto", command=take_picture)
photo_button.pack(pady=10, side=RIGHT, padx=100)
photo_button.configure(state="disabled")

window.mainloop()

# Liberar la cámara al cerrar la ventana
cap.release()
