import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

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

#########################################################################
#Buttons
#########################################################################
# Crear un botón para abrir el explorador de archivos
open_button = tk.Button(window, text="Abrir Imagen", command=open_file)
open_button.pack()

##########################################################################
#Label
#########################################################################
# Crear un widget Label para mostrar la imagen
image_label = tk.Label(window)
image_label.pack()

# Iniciar la ventana
window.mainloop()
