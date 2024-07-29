from tkinter import *
from tkinter import messagebox

#########################################################################
#Configuración del GUI
#########################################################################
window = Tk()
window.title("My First GUI Program")
window.geometry("600x300")

#########################################################################
#Buttons
#########################################################################
def button_clicked():
    print("I got clicked!.")
    #retorno1 = messagebox.showinfo(title="Mensaje", message="Este es un mensaje.")
    #retorno1 = messagebox.showerror(title="Mensaje", message="Este es un mensaje.")
    #retorno1 = messagebox.showwarning(title="Mensaje", message="Este es un mensaje.")

    #retorno1 = messagebox.askyesnocancel(title="Mensaje", message="Este es un mensaje.")
    #retorno1 = messagebox.askretrycancel(title="Mensaje", message="Este es un mensaje.")
    retorno1 = messagebox.askokcancel(title="Mensaje", message="Este es un mensaje.")
    #retorno1 = messagebox.askquestion(title="Mensaje", message="Este es un mensaje.")
    #retorno1 = messagebox.askyesno(title="Mensaje", message="Este es un mensaje.")
    print(retorno1)

button = Button(text="Click Me", command=button_clicked)
button["width"] = 20
button["height"] = 10
button.pack()
#button.pack(side="top", fill="both", pady=50)   #Argumento "fill" rellena dependiendo del argumento "side"
#button.pack(side=TOP, fill=BOTH)

button = Button(text="Click Me", width=10, height=3, command=button_clicked).pack()

window.mainloop()