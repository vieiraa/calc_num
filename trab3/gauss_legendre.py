import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate
from math import *
from tkinter import *

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

        self.label1 = Label(self.container1, text="Funcao: ")
        self.label1.pack(side="left")

        self.func = Entry(self.container1, width=20)
        self.func.pack()

        self.label2 = Label(self.container2, text="N de pontos: ")
        self.label2.pack(side="left")

        self.grau = Entry(self.container2, width=5)
        self.grau.pack()

        self.button = Button(self.container3)
        self.button["text"] = "Ok"
        self.button["command"] = self.gauss
        self.button.pack()

        self.res = Label(self.container4, text="Resultado: ")
        self.res.pack()

        self.pol = Label(self.container5, text="")
        self.pol.pack()

    def gauss(self):
        grau = int(self.grau.get())
        f = eval("lambda x: " + self.func.get())

        a = -1.0
        b = 1.0

        quad, quad_err = integrate.quad(f, a, b)
        x, w = np.polynomial.legendre.leggauss(grau + 1)
        g = sum(w * f(x))
        print(quad, g)
        self.res["text"] = ""

        self.res["text"] += ("\n\n------------tabela de pesos e nós----------------")
        self.res["text"] += ("\n\n------nós------    -----pesos-----\n")
        for i in range(grau+1):
            new_open_string = "x({0:d}) ={1:.6f}   A({2:d}) = {3:.6f}\n"
            self.res["text"] += (new_open_string.format(i,x[i], i, w[i]))

        
        self.pol["text"] = ""
        self.pol["text"] += ("\n-----------formula polinomial---------------\n")
        aux = ""
        for i in range(grau+1):
            aux += str(round(w[i], 4)) + " * f(" + str(round(x[i], 4)) + ") * \n"
        self.pol["text"] = "P(X) =" + aux + "\n"
            
        self.pol["text"] += "\n\nsolução da integral 'exata': " + str(quad) + "\n"
        self.pol["text"] += "solução gaus-legendre: " + str(g) + "\n"
        self.pol["text"] += "diferença entre gaus-legendre e o valor 'exato' \
        da integral: " + str(abs(g - quad)) + "\n"
        
        plt.plot(x,w)
        plt.title("Pesos X Nós")
        plt.show()



def main():
    GUI = Tk()
    GUI.title("Gauss-Legendre")
    App(GUI)
    GUI.mainloop()

if __name__ == "__main__":
    main()
    
"""    
print ("\n\nsolução da integral 'exata': ", quad)
##print (" erro absoluto do cálculo da integral: ", quad_err)
print("solução gaus-legendre: ", gauss)
print ("diferença entre gaus-legendre e o valor 'exato' da integral: ", abs(gauss - quad))
        
        

a = -1.
b =  1.

f = lambda x: x**3 + x**2 + x + 1

# pra comparar
quad, quad_err = integrate.quad(f, a, b)


# Gauss-Legendre (intervalo default é [-1,1])
grau = 5
x, w = np.polynomial.legendre.leggauss(grau+1)
gauss = sum(w * f(x))

#cria tabela de Nós e pesos
print("\n\n------------tabela de pesos e nós----------------")
print("\n\n------nós------    -----pesos-----")
for i in range(grau+1):
    new_open_string = "x({0:d}) ={1:.6f}   A({2:d}) = {3:.6f}"                      
    print(new_open_string.format(i,x[i], i, w[i]))
    
#plota o gráfico entre os pesos e os Nós
print("\n\n-------------gráfico relacionando peso e nó--------------")
plt.plot(x,w)
plt.title("Pesos X Nós")
plt.show()

#formula do polinomio
print("\n\n-------------formula polinomial-----------------")
string= ""
for i in range(grau+1):
    string = string + str(round(w[i], 4)) +" * f(" + str(round(x[i], 4)) + ") * "
print("P(X) =", string)
    
    
    
print ("\n\nsolução da integral 'exata': ", quad)
##print (" erro absoluto do cálculo da integral: ", quad_err)
print("solução gaus-legendre: ", gauss)
print ("diferença entre gaus-legendre e o valor 'exato' da integral: ", abs(gauss - quad))
"""
