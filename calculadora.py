"""Calculadora basica con todas las operaciones basicas 
añadiendo la potencia y el porcentaje"""
#@autores
#Lizeth Ginary Bonilla Chinchilla - 20222207521
#MATEO FERNANDO RUIZ LEON - 20222208813
#Nicolas Diaz Vargas - 20212201463
from tkinter import *
from tkinter import font
from tkinter import ttk
from math import sqrt

#root = Tk()
"""esta parte del codigo se usa para saber que tipos de fuente tiene tkinter"""
#for font in font.families():
#    print(font)



window = Tk()
window.resizable(0,0)
window.title("calculadora")
window.config(bg="sky blue")

"""esta es una clase para que el boton cambie de color tan solo con 
que el mause se ponga ensima de él."""

class HoverButton(Button):
	def __init__(self, master, **kw):
		Button.__init__(self,master=master,**kw)
		self.defaultBackground = self["background"]
		self.bind("<Enter>", self.on_enter)
		self.bind("<Leave>", self.on_leave)

	def on_enter(self, e):
		self["background"] = self["activebackground"]

	def on_leave(self, e):
		self["background"] = self.defaultBackground

def operaciones():
	global i

	ecuacion = result.get()

    
	if i !=0:
        		
		try:
			resulta = str(eval(ecuacion))
			result.delete(0,END)
			result.insert(0,resulta)
			longitud = len(resulta)
			i = longitud

		except:
			resulta = 'ERROR'
			result.delete(0,END)
			result.insert(0,resulta)
	else:
		pass

"""
def raizcuadrada():
    ecuacion = result.get()

    raiz = "√"
    indice = ecuacion.index(raiz)



    if indice == 0: 
        ecu = ecuacion[1::]
        ecu = int(ecu)
        sqrt(ecu)
"""
"""
def operaciones():
    global i
    
    ecuacion = result.get()
    if i != 0:
        try:
            # Check if the equation contains the square root symbol
            if "sqrt" in ecuacion:
                # Extract the number within the square root symbol
                number_to_square_root = ecuacion[ecuacion.find("sqrt(") + 5:ecuacion.find(")")]

                # Evaluate the number to be square rooted
                evaluated_number = eval(number_to_square_root)

                # Calculate the square root using math.sqrt()
                square_root_result = math.sqrt(evaluated_number)

                # Convert the square root result to string
                result_str = str(square_root_result)

            else:
                # Evaluate the regular equation
                result_str = str(eval(ecuacion))

            # Clear and update the result entry with the square root or regular result
            result.delete(0, END)
            result.insert(0, result_str)

            # Update the length and index variables
            longitud = len(result_str)
            i = longitud

        except:
            # Handle evaluation errors and display 'ERROR'
            result_str = 'ERROR'
            result.delete(0, END)
            result.insert(0, result_str)
    else:
        pass

"""
i=0

def obterner(dato):
    global i
    i+=1
    result.insert(i,dato)

def borrarOne():
    global i
    if i == -1:
        pass
    else:
        result.delete(i,last=None)
        i -= 1

def alldelete():
    result.delete(0,END)



frame = Frame(window, bg = "azure",relief='groove')
frame.grid(column=0,row=0,padx=3,pady=2,ipadx=2,ipady=1)

result = Entry(frame,bg = "white",width = 30,relief = "groove",font = "ComicSansMS", justify = "right")
result.grid(columnspan=10 , row=0, pady=3,padx=1, ipadx=1, ipady=4)


#todos los botones con su respectivo diseño 

#Botones del 0 al 9
Botton1 = HoverButton(frame,text="1",font=("calibri",15),height=2,width=3,bg="light cyan",activebackground="lightblue1",borderwidth = 3,command=lambda:obterner(1))
Botton1.grid(column=0,rowspan=1,row=1,padx=1,pady=1)

Botton2 = HoverButton(frame,text="2",font=("calibri",15),height=2,width=3,bg="light cyan",activebackground="lightblue1",borderwidth = 3,command=lambda:obterner(2))
Botton2.grid(column=1,rowspan=1,row=1,padx=1,pady=1)

Botton3 = HoverButton(frame,text="3",font=("calibri",15),height=2,width=3,bg="light cyan",activebackground="lightblue1",borderwidth = 3,command=lambda:obterner(3))
Botton3.grid(column=2,rowspan=1,row=1,padx=1,pady=1)

Botton4 = HoverButton(frame,text="4",font=("calibri",15),height=2,width=3,bg="light cyan",activebackground="lightblue1",borderwidth = 3,command=lambda:obterner(4))
Botton4.grid(column=0,rowspan=1,row=2,padx=1,pady=1)

Botton5 = HoverButton(frame,text="5",font=("calibri",15),height=2,width=3,bg="light cyan",activebackground="lightblue1",borderwidth = 3,command=lambda:obterner(5))
Botton5.grid(column=1,rowspan=1,row=2,padx=1,pady=1)

Botton6 = HoverButton(frame,text="6",font=("calibri",15),height=2,width=3,bg="light cyan",activebackground="lightblue1",borderwidth = 3,command=lambda:obterner(6))
Botton6.grid(column=2,rowspan=1,row=2,padx=1,pady=1)

Botton7 = HoverButton(frame,text="7",font=("calibri",15),height=2,width=3,bg="light cyan",activebackground="lightblue1",borderwidth = 3,command=lambda:obterner(7))
Botton7.grid(column=0,rowspan=1,row=3,padx=1,pady=1)

Botton8 = HoverButton(frame,text="8",font=("calibri",15),height=2,width=3,bg="light cyan",activebackground="lightblue1",borderwidth = 3,command=lambda:obterner(8))
Botton8.grid(column=1,rowspan=1,row=3,padx=1,pady=1)

Botton9 = HoverButton(frame,text="9",font=("calibri",15),height=2,width=3,bg="light cyan",activebackground="lightblue1",borderwidth = 3,command=lambda:obterner(9))
Botton9.grid(column=2,rowspan=1,row=3,padx=1,pady=1)

Botton0 = HoverButton(frame,text="0",font=("calibri",15),height=2,width=3,bg="light cyan",activebackground="lightblue1",borderwidth = 3,command=lambda:obterner(0))
Botton0.grid(column=1,rowspan=1,row=4,padx=1,pady=1)

#botones de operación

Bottonplus = HoverButton(frame,text="+",font=("calibri",15),height=2,width=3,bg="light cyan3",activebackground="lightblue4",borderwidth = 3,command=lambda:obterner("+"))
Bottonplus.grid(column=3,rowspan=1,row=1,padx=1,pady=1)

Bottonsubt = HoverButton(frame,text="-",font=("calibri",15),height=2,width=3,bg="light cyan3",activebackground="lightblue4",borderwidth = 3,command=lambda:obterner("-"))
Bottonsubt.grid(column=3,rowspan=1,row=2,padx=1,pady=1)

Bottonmulti = HoverButton(frame,text="X",font=("calibri",15),height=2,width=3,bg="light cyan3",activebackground="lightblue4",borderwidth = 3,command=lambda:obterner("*"))
Bottonmulti.grid(column=3,rowspan=1,row=3,padx=1,pady=1)

Bottondivision = HoverButton(frame,text="÷",font=("calibri",15),height=2,width=3,bg="light cyan3",activebackground="lightblue4",borderwidth = 3,command=lambda:obterner("/"))
Bottondivision.grid(column=3,rowspan=1,row=4,padx=1,pady=1)

Bottonraiz = HoverButton(frame,text="√",font=("calibri",15),height=2,width=3,bg="light cyan3",activebackground="lightblue4",borderwidth = 3,command=lambda:obterner("**1/2"))
Bottonraiz.grid(column=4,rowspan=1,row=4,padx=1,pady=1)

Bottonporcent = HoverButton(frame,text="%",font=("calibri",15),height=2,width=3,bg="light cyan3",activebackground="lightblue4",borderwidth = 3,command=lambda:obterner("/100"))
Bottonporcent.grid(column=2,rowspan=1,row=4,padx=1,pady=1)

Bottonpoint = HoverButton(frame,text=".",font=("calibri",15),height=2,width=3,bg="light cyan",activebackground="lightblue1",borderwidth = 3,command=lambda:obterner("."))
Bottonpoint.grid(column=0,rowspan=1,row=4,padx=1,pady=1)


#funcionalidades clear, delete, igual

Bottonclear = HoverButton(frame,text="C",font=("calibri",15),width=3,height=1,activebackground="lightblue1",borderwidth = 3,command=alldelete)
Bottonclear.grid(column=4,rowspan=2,row=0,padx=1,pady=1)

BottonDel = HoverButton(frame,text="⌫",font=("calibri",15),width=3,height=2,activebackground="orangered2",bg = "tomato1",borderwidth = 3,command=borrarOne)
BottonDel.grid(column=4,rowspan=1,row=2,padx=1,pady=1)


Bottoniqual = HoverButton(frame,text="=",width=3,font=("calibri",12),activebackground="tan1",borderwidth = 3,command=operaciones)
Bottoniqual.grid(column=4,rowspan=1,row=3,padx=1,pady=1,sticky="ns")




window.mainloop()