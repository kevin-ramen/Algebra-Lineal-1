# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 23:47:12 2020

@author: kevin
"""
import tkinter as tkr
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def xdots(xi):#x de -10 a 10
    x=[]
    for i in range((xi-10),(xi+11)):
        x.append(i)
    print(x)
    return x

def ydots(l,xi):#Obtenemos puntos para y 
    y=[]
    for i in range((xi-10),(xi+11)):
        y.append(((l[2])-(l[0]*i))/(l[1]))
    print(y)
    return y

def graph(l1,l2,lf,sol):#Grafica del resultado
    #Hallamos la interseccion
    yi=lf[2]//lf[1]
    xi=((l1[2]-(l1[1]*yi))//(l1[0]))
    print(xi)
    x=xdots(int(xi))#Mismo rango
    if sol==2:#Infinidad de Soluciones (Caso particular)
        #Obtenemos los puntos de l1
        y1=ydots(l1,int(xi))
        #Grafica
        fig = plt.Figure(figsize=(10,10),dpi=50)
        fig.add_subplot(111).plot(x, y1, label = "L1=L2", linewidth = 3, color = "purple")
    else:
        #No hay solucion
        #Obtenemos los puntos de l1
        y1=ydots(l1,int(xi))
        #Obtenemos los puntos de l2
        y2=ydots(l2,int(xi))
        #Grafica
        fig = plt.Figure(figsize=(10,10),dpi=50)
        fig.add_subplot(111).plot(x, y1, label = "L1", linewidth = 3, color = "blue")
        fig.add_subplot(111).plot(x, y2, label = "L2", linewidth = 3, color = "red")
        #Estetica
        
    #Ventana
    window = tkr.Tk()
    label1 = tkr.Label(window,text="No hay Solucion")
    label2 = tkr.Label(window,text="Infinidad de Soluciones")
    label3 = tkr.Label(window,text="Solucion Unica")
    label4 = tkr.Label(window,text="Matriz Diagonalizada")
    labela11 = tkr.Label(window,text=str(l1[0]))
    labela12 = tkr.Label(window,text=str(l1[1]))
    labelb1 = tkr.Label(window,text=str(l1[2]))
    labela21 = tkr.Label(window,text=str(lf[0]))
    labela22 = tkr.Label(window,text=str(lf[1]))
    labelb2 = tkr.Label(window,text=str(lf[2]))
    window.title("Grafica")
    window.geometry("1000x600")
    #Canvas
    chart = FigureCanvasTkAgg(fig,window)
    chart.get_tk_widget().pack(side = tkr.LEFT)#Cargar grafica a ventana
    #Matriz
    label4.pack()
    label4.config(fg="purple",font=("Verdana",12))
    label4.place(x=650,y=150)
    labela11.pack()
    labela11.config(fg="purple",font=("Verdana",12))
    labela11.place(x=670,y=250)
    labela12.pack()
    labela12.config(fg="purple",font=("Verdana",12))
    labela12.place(x=720,y=250)
    labelb1.pack()
    labelb1.config(fg="purple",font=("Verdana",12))
    labelb1.place(x=770,y=250)
    labela21.pack()
    labela21.config(fg="purple",font=("Verdana",12))
    labela21.place(x=670,y=300)
    labela22.pack()
    labela22.config(fg="purple",font=("Verdana",12))
    labela22.place(x=720,y=300)
    labelb2.pack()
    labelb2.config(fg="purple",font=("Verdana",12))
    labelb2.place(x=770,y=300)
    if sol==1:
        label1.pack()
        label1.config(fg="purple",font=("Verdana",12))
        label1.place(x=650,y=400)
    if sol==2:
        label2.pack()
        label2.config(fg="purple",font=("Verdana",12))
        label2.place(x=650,y=400)
    if sol==3:
        label3.pack()
        label3.config(fg="purple",font=("Verdana",12))
        label3.place(x=650,y=400)
        
    tkr.mainloop()
  
    
    
    
def math(a11,a12,b1,a21,a22,b2):#Algoritmo para resolver sistemas de ecuaciones lineales 2x2
    l1=[a11,a12,b1]#Ecuacion lineal 1
    l2=[a21,a22,b2]#Ecuacion lineal 2
    lt=[]#L temporal para Operaciones
    lf=[]#L Final
    sol=0
    #Diagonalización
    print("Matriz Inicial")
    print("l1:",l1,)
    print("l2:",l2)
    for i in range(0,3):
        lt.append(l1[i]*(-(a21)/(a11)))#Creamos una lista temporal F1(-a21/a11) para tener el mismo valor que a21 pero negativo
        lf.append(lt[i]+l2[i])#F1+F2 = F2
    print("Lista Auxiliar")
    print("lt:",lt)
    print("--------------------------")
    print("Matriz Diagonalizada")
    print("l1:",l1)
    print("l2:",lf)
    if (lf[1] == 0) and (lf[2] != 0):#No hay Solucion
        sol=1
        print("No hay Solucion")
    else:
        if lf[1] == 0 and lf[2] == 0:#Infinidad de Soluciones
            sol=2
            print("Infinidad de Soluciones")
        else:
            if lf[1] != 0:#Solucion Unica
                sol=3
                print("Solucion Unica")       
    graph(l1,l2,lf,sol)
    
    