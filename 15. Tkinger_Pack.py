from tkinter import *

#########################################################################
#Configuración del GUI
#########################################################################
window = Tk()
window.title("Ejemplo: Pack Manager")

#########################################################################
#Buttons
#########################################################################
boton1=Button(text="Boton 1")
boton1.pack(side=TOP, fill=BOTH)
boton2=Button(text="Boton 2")
boton2.pack(side=TOP, fill=BOTH)
boton3=Button(text="Boton 3")
boton3.pack(side=TOP, fill=BOTH)
boton4=Button(text="Boton 4")
boton4.pack(side=LEFT)
boton5=Button(text="Boton 5")
boton5.pack(side=RIGHT)
boton6=Button(text="Boton 6")
boton6.pack(side=RIGHT)
boton7=Button(text="Boton 7")
boton7.pack(side=RIGHT)

window.mainloop()