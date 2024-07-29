#Si lo importo así, no es necesario colocar tkinter.
from tkinter import *
#Si lo pongo así, si es necesario tkinter.
#import tkinter

window = Tk()
window.title("My First GUI Program")
#window.minsize(width=500, height=300)
window.geometry("500x300")
window.resizable(False, False)

window.mainloop()