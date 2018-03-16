from tkinter import *
import re
import inspect
import sympy as sp
import numpy as np

class App:
    def __init__(self, master=None):
        self.container1 = Frame(master)
        self.container1["pady"] = 10
        self.container1.pack()
        self.container2 = Frame(master)
        self.container2["padx"] = 20
        self.container2.pack()
        self.container3 = Frame(master)
        self.container3.pack()
        self.container4 = Frame(master)
        self.container4.pack()
        self.container5 = Frame(master)
        self.container5.pack()
        self.container6 = Frame(master)
        self.container6.pack()
        self.container7 = Frame(master)
        self.container7.pack()

        self.text1 = Label(self.container1, text="Função: ")
        self.text1.pack()
        self.text2 = Label(self.container2, text="Limite inferior: ")
        self.text2.pack()
        self.text3 = Label(self.container3, text="Limite superior:")
        self.text3.pack()
        self.text4 = Label(self.container4, text="Tolerancia:")
        self.text4.pack()
        self.text5 = Label(self.container5, text="Nº de tentativas:")
        self.text5.pack()

        self.func = Entry(self.container1)
        self.func.pack()
        self.lim_inf = Entry(self.container2)
        self.lim_inf.pack()
        self.lim_sup = Entry(self.container3)
        self.lim_sup.pack()
        self.tol = Entry(self.container4)
        self.tol.pack()
        self.num = Entry(self.container5)
        self.num.pack()
        
        self.calc = Button(self.container6)
        self.calc["text"] = "Calcular"
        self.calc["command"] = self.calcular
        self.calc.pack(side=LEFT)
        self.sair = Button(self.container6)
        self.sair["text"] = "Sair"
        self.sair["command"] = self.container1.quit
        self.sair.pack()

        self.listbox = Listbox(self.container7, width=550)
        self.listbox.pack()

    def calcular(self):
        func = self.func.get()
        lim_inf = int(self.lim_inf.get())
        lim_sup = int(self.lim_sup.get())
        tol = float(self.tol.get())
        num = int(self.num.get())
        text = falsa_posicao(func, lim_inf, lim_sup, tol, num)
        self.listbox.insert(END, text)


def falsa_posicao(f,a,b,tol,N):        
    # TODO identificar a variável usada na função 
    #      Aqui, tentei assumir que apenas uma era usada (e.g. 'x'),
    #      mas foi complicado generalizar quando há objeto numpy
    #var = re.search('[a-zA-Z]+',f)
    #var = var.group()

    var = re.search(r'((\*|-)+[a-zA-Z](\*\*|/)?)', f)
    #var = re.search(r'((\*|-|\()[a-zA-Z])', f)
    var = var.group(0)
    var = re.search(r'[a-zA-Z]', var)
    var = var.group(0)
    print(var)
    string = ""

    # cria função anônima
    f = eval('lambda ' + var + ':' + f)
    
    # Se função não for de uma variável, lança erro.
    # Mais aplicável se o caso geral fosse implementado.
    if len(inspect.getfullargspec(f).args) - 1 > 0:
        raise ValueError('O código é válido apenas para uma variável.')

    # calcula valor da função nos extremos
    fa = f(a)
    fb = f(b)

    # verifica sinal da função para o intervalo passado
    if fa*fb >= 0:
        raise ValueError('A função deve ter sinais opostos em a e b!')
    
    # flag usada para prevenir a obtenção da raiz 
    # antes de o intervalo ter sido 
    # suficientemente reduzido
    done = 0;

    # loop principal

    # bisecta o intervalo
    xm = (b*f(a) - a*f(b))/(f(a) - f(b))

    i = 1 # contador

    while abs(a-b) > tol and ( not done or N != 0 ):
        # avalia a função no ponto médio
        fxm = f(xm)
        #string += ("(i = {0:d}) f(xm)={1:f} | f(a)={2:f} | f(b)={3:f}".format(i,fxm,fa,fb))
        
        if fa*fxm < 0:       # Raiz esta à esquerda de xm
            b = xm
            fb = fxm
            xm = (b*f(a) - a*f(b))/(f(a) - f(b))
        elif fxm*fb < 0:     # Raiz esta à direita de xm
            a = xm
            fa = fxm
            xm = (b*f(a) - a*f(b))/(f(a) - f(b))
        else:               # Achamos a raiz
            break
        
        N -= 1              # Atualiza passo
        i += 1              # Atualiza contador

    string += ("Solução encontrada: {0}".format(xm))

    return string

GUI = Tk()
App(GUI)
GUI.title("Falsa posição")
GUI.geometry("600x600")
GUI.mainloop()
