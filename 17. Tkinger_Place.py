from tkinter import *

#########################################################################
#Configuración del GUI
#########################################################################
window = Tk()
window.title("Ejemplo: Place Manager")
window.geometry("800x600")
window.resizable(0,0)

#########################################################################
#Buttons
#########################################################################
boton1=Button(text="Confirmar")
boton1.place(x=680, y=550, width=90, height=30)
boton2=Button(text="Cancelar")
boton2.place(x=580, y=550, width=90, height=30)

window.mainloop()