#Si lo importo así, no es necesario colocar tkinter.
from tkinter import *
#Si lo pongo así, si es necesario tkinter.
#import tkinter

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=50, pady=10) #Padding "x" y "y"

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
def spinbox_used():
    #Obtiene el valor actual del Spinbox cada vez que cambie
    print(spinbox.get())

spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()

########################################################################
#Scale
#########################################################################
#Called with current scale value.
def scale_used(value):
    print(value)

scale = Scale(from_=0, to=100, command=scale_used, orient="horizontal")
scale.pack()

#########################################################################
#Checkbutton
#########################################################################
def checkbutton_used():
    #Prints 1 if On button checked, otherwise 0.
    print(checked_state.get())

checked_state = IntVar() #Variable Int de Tkinter
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
#checked_state.get()
checkbutton.pack()

#########################################################################
#Radiobutton
#########################################################################
def radio_used():
    print(radio_state.get())

#Variable para que guarde el valor de la opción de radio button seleccionada,
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()

#########################################################################
#Listbox
#########################################################################
def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))

listbox = Listbox(height=7)
fruits = ["Apple", "Pear", "Orange", "Banana", "Strawberry"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used) #Ejecuta la función "listbox_used" cada vez que se seleccione un valor
listbox.pack()

window.mainloop()