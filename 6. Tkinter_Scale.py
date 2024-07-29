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

# Modificar una propiedad por su nombre
#my_label["text"] = "New Text"
#my_label.config(text="My New Text 2")

#########################################################################
#Packer
#########################################################################
#sin el pack no se muestra el componente
my_label.pack()                 #Por defecto es side="top"
my_label.pack(side="top")

#########################################################################
#Entry
#########################################################################
input = Entry(width=50, justify="center")
input.insert(index=END, string="Some text to begin with.")
input.pack()

# Obtiene el texto del Entry
print(input.get())

#########################################################################
#Text Box
#########################################################################
#Multiple lines
text = Text(height=5, width=50)
text.focus()    #Focaliza el cursor en el Text Box
text.insert(END, "Example of multi-line text entry.\nEsta es la segunda linea")

#Obtiene el valor actual del TextBox desde la línea 1 - caracter 0 (1,0) hasta el final (END)
print(text.get("1.0", END))
text.pack()

########################################################################
#Spinbox
#########################################################################
#Obtiene el valor actual del Spinbox cada vez que cambie
def spinbox_used():
    print(spinbox.get())

spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()

########################################################################
#Scale
#########################################################################
#Obtiene el valor actual del Scale cada vez que cambie.
def scale_used(value):
    print(value)

scale = Scale(from_=0, to=100, command=scale_used, orient="horizontal")
scale.pack()

window.mainloop()