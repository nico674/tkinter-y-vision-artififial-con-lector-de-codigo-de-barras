from tkinter import *

#########################################################################
#Configuración del GUI
#########################################################################
window = Tk()
window.title("Ejemplo: Grid Manager")

#########################################################################
#Buttons
#########################################################################
boton1=Button(text="Boton 1")
boton1.grid(column=0, row=0)
boton2=Button(text="Boton 2")
boton2.grid(column=1, row=0)

"""En la propiedad sticky (se traduce como 'pegajoso') pedimos que el botón se expanda de north (norte) a south (sur), 
si no disponemos sticky luego el botón ocupa las dos celdas pero aparece centrado."""
boton3=Button(text="Boton 3")
boton3.grid(column=2, row=0, rowspan=2, sticky="ns")
#boton3.grid(column=2, row=0, rowspan=2, sticky=N+S)
#boton3.grid(column=2, row=0, rowspan=2, padx=10, pady=10)

boton4=Button(text="Boton 4")
boton4.grid(column=0, row=1)
boton5=Button(text="Boton 5")
boton5.grid(column=1, row=1)

# En el parámetro sticky indicamos que se estire de west (oeste) a east (este) - izquierda a derecha
boton6=Button(text="Boton 6")
boton6.grid(column=0, row=2, columnspan=3, sticky="we")
#boton6.grid(column=0, row=2, columnspan=3, pady=10)

window.mainloop()