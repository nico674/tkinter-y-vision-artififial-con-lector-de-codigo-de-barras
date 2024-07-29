from tkinter import *

#########################################################################
#Configuración del GUI
#########################################################################
window = Tk()
window.title("My First GUI Program")
window.config(padx=50, pady=50)

#########################################################################
#Canvas
#########################################################################
canvas = Canvas(height=450, width=810)
#canvas.pack()

#########################################################################
#Image
#########################################################################
imagen = PhotoImage(file="./Imagenes/esneda.png")
#create_image(posx, posy, image=)
ancho = imagen.width()
alto = imagen.height()
canvas.create_image(ancho/2, alto/2, image=imagen)
canvas.pack()

window.mainloop()