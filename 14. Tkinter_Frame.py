#Si lo importo así, no es necesario colocar tkinter.
from tkinter import *
#Si lo pongo así, si es necesario tkinter.
#import tkinter

window = Tk()
window.title("My First GUI Program")
#window.minsize(width=500, height=300)
#window.geometry("500x300")
#window.resizable(False, False)

#########################################################################
#Frame
#########################################################################
Frame1 = Frame(window)
Frame1.configure(relief='groove') #Specifies the 3-D effect desired for the widget. Acceptable values are raised, sunken, flat, ridge, solid, and groove.
Frame1.configure(borderwidth="2")
Frame1.configure(background="#d9d9d9")
Frame1.configure(width=345)
Frame1.configure(height=345)
Frame1.pack(side=LEFT, padx=10, pady=10)

Frame2 = Frame(window)
Frame2.configure(relief='groove') #Specifies the 3-D effect desired for the widget. Acceptable values are raised, sunken, flat, ridge, solid, and groove.
Frame2.configure(borderwidth="2")
Frame2.configure(background="#d9d9d9")
Frame2.configure(width=345)
Frame2.configure(height=345)
Frame2.pack(side=RIGHT, padx=10, pady=10)

#########################################################################
#Buttons
#########################################################################
button1 = Button(window, text="Botón1")
button1.pack(side=BOTTOM, fill=BOTH, padx=10, pady=10)

#En el empaquetador Pack() los widgets hijos modifican el tamaño del padre
button2 = Button(Frame1, text="Botón2")
button2.pack(padx=10, pady=10)

button3 = Button(Frame2, text="Botón3")
button3.pack(padx=10, pady=10)

window.mainloop()