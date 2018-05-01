from tkinter import Tk, Frame, Label, Entry, Button, LEFT, RIGHT
from math import *
import numpy as np
import re, math

class App:
    def __init__(self, master=None):
        self.container1 = Frame(master)
        self.container1.pack()

        self.container2 = Frame(master)
        self.container2.pack()

        self.container3 = Frame(master)
        self.container3.pack()

        self.container4 = Frame(master)
        self.container4.pack()

        self.container5 = Frame(master)
        self.container5.pack()

        self.label1 = Label(self.container1, text="Função:")
        self.label1.pack(side=LEFT)

        self.label2 = Label(self.container2, text="Valor inicial:")
        self.label2.pack(side=LEFT)

        self.label3 = Label(self.container3, text="Precisão:")
        self.label3.pack(side=LEFT)

        self.result = Label(self.container5, text="")
        self.result.pack()

        self.func = Entry(self.container1)
        self.func.pack()

        self.x0 = Entry(self.container2)
        self.x0.pack()

        self.prec = Entry(self.container3)
        self.prec.pack()

        self.calcular = Button(self.container4)
        self.calcular["text"] = "Calcular"
        self.calcular["command"] = self.calculate
        self.calcular.pack(side=LEFT)
        self.sair = Button(self.container4)
        self.sair["text"] = "Sair"
        self.sair["command"] = self.container1.quit
        self.sair.pack()


    def calculate(self):
        f = self.func.get()
        var = list(set(re.findall(r'[a-zA-Z]+', f)) - set(dir(math)))
        var = var[0]
        f = eval("lambda " + var + ":" + f)
        x0 = float(self.x0.get())
        prec = float(self.prec.get())

        self.result["text"] = "Resultado = " + str(newton(f, x0, prec))
        

def derivative(f, x, h=0.00001):
    d = (f(x+h)-f(x))/h
    return d

def newton(f, x0, h):
    i = 0
    last_x = x0
    next_x = x0

    while True:
        last_x = next_x
        next_x = last_x - f(last_x) / derivative(f, last_x, h)
        i += 1
        print("Iteração: ", i)
        print("Valor: ", next_x)
        if abs(last_x - next_x) < h:
            break

    return next_x

GUI = Tk()
App(GUI)
GUI.title("Newton-Raphson")
GUI.geometry("300x110")
GUI.mainloop()
