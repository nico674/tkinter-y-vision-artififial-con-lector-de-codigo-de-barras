from tkinter import *
import cv2
import numpy as np
from PIL import Image, ImageTk

def cargar_imagen():
    #Imagen = 512x471
    img = cv2.imread('./Imagenes/R.png')
    b,g,r = cv2.split(img)
    img_1 = cv2.merge((r,g,b))
    im = Image.fromarray(img_1)
    imgtk = ImageTk.PhotoImage(image=im)
    lbl1.imgtk = imgtk
    lbl1.configure(image=imgtk)

def convertir_grises():
    #Imagen = 512x471
    img = cv2.imread('./Imagenes/R.png')
    gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    im1 = Image.fromarray(gris)
    imgtk = ImageTk.PhotoImage(image=im1)
    lbl2.imgtk = imgtk
    lbl2.configure(image=imgtk)

def convertir_hsv():
    #Imagen = 512x471
    img = cv2.imread('./Imagenes/R.png')
    gris = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    im1 = Image.fromarray(gris)
    imgtk = ImageTk.PhotoImage(image=im1)
    lbl3.imgtk = imgtk
    lbl3.configure(image=imgtk)
    
window=Tk()
window.title('MANEJO DE IMÁGENES')
#window.geometry("1094x960")
window.configure(background="#d9d9d9")
window.configure(padx=10, pady=10)
window.resizable(False, False)

#########################################################################
#Frame
#########################################################################
Frame1 = Frame(window)
Frame1.grid(row=0, column=0, padx=10, pady=10, sticky=W+E)
Frame1.configure(relief='groove')
Frame1.configure(borderwidth="2")
Frame1.configure(relief="groove")
Frame1.configure(background="#d9d9d9")
Frame1.configure(width=532)
Frame1.configure(height=491)

Frame2 = Frame(window)
Frame2.grid(row=0, column=1, padx=10, pady=10, sticky=W+E)
Frame2.configure(relief='groove')
Frame2.configure(borderwidth="2")
Frame2.configure(relief="groove")
Frame2.configure(background="#d9d9d9")
Frame2.configure(width=532)
Frame2.configure(height=491)

Frame3 = Frame(window)
Frame3.grid(row=0, column=2, padx=10, pady=10, sticky=W+E)
Frame3.configure(relief='groove')
Frame3.configure(borderwidth="2")
Frame3.configure(relief="groove")
Frame3.configure(background="#d9d9d9")
Frame3.configure(width=532)
Frame3.configure(height=491)

##########################################################################
#Label
#########################################################################
lbl1=Label(Frame1, text="IMAGEN COLOR")
lbl1.place(x=10, y=10, width=512, height=471)
lbl1.configure(background="#d85a34")
lbl1.configure(foreground="#000000")

lbl2=Label(Frame2, text="IMAGEN BLANCO Y NEGRO")
lbl2.place(x=10, y=10, width=512, height=471)
lbl2.configure(background="#d85a34")
lbl2.configure(foreground="#000000")

lbl3=Label(Frame3, text="IMAGEN HSV")
lbl3.place(x=10, y=10, width=512, height=471)
lbl3.configure(background="#d85a34")
lbl3.configure(foreground="#000000")

#########################################################################
#Buttons
#########################################################################
btn1=Button(window, text="Cargar Imágen")
btn1.grid(row=1, column=0)
btn1.configure(activebackground="#ececec")
btn1.configure(activeforeground="#000000")
btn1.configure(background="#d9d9d9")
btn1.configure(disabledforeground="#a3a3a3")
btn1.configure(foreground="#000000")
btn1.configure(highlightbackground="#d9d9d9")
btn1.configure(highlightcolor="black")
btn1.configure(padx=10)
btn1.configure(pady=10)
btn1.configure(text="Cargar Imágen a Color")
btn1.configure(font=("Arial",16, "bold"))
btn1.configure(command=cargar_imagen)

btn2=Button(window, text="Cargar Imágen")
btn2.grid(row=1, column=1)
btn2.configure(activebackground="#ececec")
btn2.configure(activeforeground="#000000")
btn2.configure(background="#d9d9d9")
btn2.configure(disabledforeground="#a3a3a3")
btn2.configure(foreground="#000000")
btn2.configure(highlightbackground="#d9d9d9")
btn2.configure(highlightcolor="black")
btn2.configure(padx=10)
btn2.configure(pady=10)
btn2.configure(text="Cargar Imágen a Escala de Grises")
btn2.configure(font=("Arial",16, "bold"))
btn2.configure(command=convertir_grises)

btn3=Button(window, text="Cargar Imágen")
btn3.grid(row=1, column=2)
btn3.configure(activebackground="#ececec")
btn3.configure(activeforeground="#000000")
btn3.configure(background="#d9d9d9")
btn3.configure(disabledforeground="#a3a3a3")
btn3.configure(foreground="#000000")
btn3.configure(highlightbackground="#d9d9d9")
btn3.configure(highlightcolor="black")
btn3.configure(padx=10)
btn3.configure(pady=10)
btn3.configure(text="Cargar Imágen a HSV")
btn3.configure(font=("Arial",16, "bold"))
btn3.configure(command=convertir_hsv)

window.mainloop()

