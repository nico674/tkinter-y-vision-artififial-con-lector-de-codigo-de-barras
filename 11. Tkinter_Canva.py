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
canvas = Canvas(height=500, width=500)
canvas.pack()
canvas.create_line(0,0,400,300, width=5, fill="red")
canvas.create_line(0,300,400,0, width=5, fill="red")
canvas.create_rectangle(100,75,300,225, fill="yellow", outline="blue", width=5)

window.mainloop()