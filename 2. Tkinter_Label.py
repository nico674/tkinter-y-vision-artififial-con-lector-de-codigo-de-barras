#Si lo importo así, no es necesario colocar tkinter.
from tkinter import *
#Si lo pongo así, si es necesario tkinter.
#import tkinter

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

##########################################################################
#Create Components inside the window
##########################################################################
#Label
#########################################################################
my_label = Label(text="I am a Label", font=("Arial",24, "bold"))
#Pasar la referencia del padre
#my_label = Label(window, text="I am a Label", font=("Arial",24, "bold"))

# Modificar una propiedad por su nombre
my_label["text"] = "New Text"
my_label.config(text="My New Text 2")

#########################################################################
#Packer
#########################################################################
#sin el pack no se muestra el componente
my_label.pack()                 #Por defecto es side="top"
my_label.pack(side="left")
#my_label.pack(side=LEFT)
#my_label.pack(side=tk.LEFT) #Si importamos la librería Tkinter as tk

window.mainloop()