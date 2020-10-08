# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 23:47:12 2020

@author: kevin
"""
from tkinter import *
import algorithm as gauss
#GUI
root = Tk()
label1 = Label(root,text="Resolucion de Sistemas de Ecuaciones Lineales de 2x2 :)")
label2 = Label(root,text="Inserta los valores en Decimales")
button1 = Button(root,text="Graficarlo",command=lambda:[gauss.math(float(entry1.get()),float(entry2.get()),float(entry3.get()),float(entry4.get()),float(entry5.get()),float(entry6.get()))])
entry1 = Entry(root)
entry2 = Entry(root)
entry3 = Entry(root)
entry4 = Entry(root)
entry5 = Entry(root)
entry6 = Entry(root)
label3 = Label(root,text="x +")
label4 = Label(root,text="y =")
label5 = Label(root,text="x +")
label6 = Label(root,text="y =")
label7 = Label(root,text="L1: ")
label8 = Label(root,text="L2: ")

root.title("Algebra Lineal_Ramirez Mendez Kevin")
root.geometry("600x400")
label1.pack(anchor=NW)
label1.config(fg="purple",font=("Verdana",14))
label2.pack(anchor=NW)
label2.config(font=("Verdana",12))
#Primera Fila
label7.pack()
label7.place(x=100,y=120)
entry1.pack()
entry1.config(width=5)
entry1.place(x=150,y=120)
label3.pack()
label3.place(x=200,y=120)
entry2.pack()
entry2.config(width=5)
entry2.place(x=250,y=120)
label4.pack()
label4.place(x=300,y=120)
entry3.pack()
entry3.config(width=5)
entry3.place(x=350,y=120)
#Segunda Fila
label8.pack()
label8.place(x=100,y=170)
entry4.pack()
entry4.config(width=5)
entry4.place(x=150,y=170)
label5.pack()
label5.place(x=200,y=170)
entry5.pack()
entry5.config(width=5)
entry5.place(x=250,y=170)
label6.pack()
label6.place(x=300,y=170)
entry6.pack()
entry6.config(width=5)
entry6.place(x=350,y=170)

button1.pack()
button1.place(x=225,y=220)
root.mainloop()