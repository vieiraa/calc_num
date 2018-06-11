import numpy as np
from tkinter import *
from sympy import Symbol

class App:
    def __init__(self, master=None):
        self.container1 = Frame(master)
        self.container1.pack()

        self.container2 = Frame(master)
        self.container2.pack()

        self.label1 = Label(self.container1, text="Grau do polinomio: ")
        self.label1.pack(side="left")

        self.grau = Entry(self.container1, width=5)
        self.grau.pack()

        self.button = Button(self.container2)
        self.button["text"] = "Ok"
        self.button["command"] = self.newton
        self.button.pack()

    def newton(self):
        n = int(self.grau.get()) + 1

        newton_window(n)

def newton_window(n):
    top = Toplevel()
    top.title("Newton")
    x = []
    y = []

    for i in range(n):
        c1 = Frame(top)
        c1.pack()

        c2 = Frame(top)
        c2.pack()

        label_x = Label(c1, text="x%d=" % i)
        label_x.pack(side="left")
        label_y = Label(c2, text="f(x%d)" % i)
        label_y.pack(side="left")
        xx = Entry(c1, width=5)
        xx.pack()
        yy = Entry(c2, width=5)
        yy.pack()

        x.append(xx)
        y.append(yy)

    c1 = Frame(top)
    c1.pack()
    c2 = Frame(top)
    c2.pack()
    c3 = Frame(top)
    c3.pack()

    val = Label(c1)
    val["text"] = "x a ser calculado:"
    val.pack(side="left")

    x_calc = Entry(c1, width=5)
    x_calc.pack()

    calc = Button(c2)
    calc["text"] = "Calcular"
    calc["command"] = lambda: result(x, y, n, x_calc, res)
    calc.pack()

    res = Label(c3)
    res["text"] = "Resultado:"
    res.pack()

def result(x, y, n, x_calc, res):
    matriz = np.zeros((n,n)).astype("float32")
    vetor = np.zeros(n).astype("float32")
    xx = Symbol('x')

    for i in range(n):
        vetor[i] = float(x[i].get())
        matriz[i][0] = float(y[i].get())
        print(matriz)

    for i in range(1, n):
        for j in range(1, n):
            matriz[j][i] = ( (matriz[j][i-1]-matriz[j-1][i-1])
                            / (vetor[j]-vetor[j-i]))

    p = matriz[0][0]

    for i in range(1, n):
        aux = 1
        for j in range(i-1):
            aux *= (xx - vetor[j])
        aux *= matriz[i][0]
        print(aux)
        p += aux

    print(p)

    ponto = float(x_calc.get())
    string = ""
    string += ("------------------------------\n")
    string += ("------------------------------\n")
    string += ("---tabela de diferenças divididas----\n")
    t = n-1
    for k in range(n):
        string += str(matriz[t]) + "\n"
        t = t-1
    
    string += ("------------------------------\n")
    string += ("------------------------------\n")
    
    aprx = 0
    mul = 1.0
    for i in range(n):
        mul = matriz[i][i];
        for j in range(1,i+1):
            mul = mul * (ponto - vetor[j-1])
        aprx = aprx + mul

    string += ("------------------------------\n")
    string += ("\n\n\nOs valores das diferenças divididas são:" +
               str(matriz[n-1]) + "\n")
    string += ("------------------------------\n")
    string += ("o valor aproximado de f(" + str(ponto) + ") é: " +
               str(aprx) + "\n")

    res["text"] = string
    res["justify"] = "right"

def main():
    GUI = Tk()
    GUI.title("Newton")
    App(GUI)
    GUI.mainloop()

if __name__ == "__main__":
    main()
            
"""
print ("------- Interpolação polinomial  de newton -------")
n = int(input("digite o grau do polinomio: "))+1


for i in range(n):
    matriz[i] = [0.0] * n

vector = [0.0] * n

#print (matriz)
#print (vector)
for i in range(n):
    x = input("digite o valor de x: ")
    y = input("digite o valor de f("+x+"): ")
    vector[i]=float(x)
    matriz[i][0]=float(y)

punto_a_evaluar = float(input("digite o valor de x a ser calculado: "))


for i in range(1,n):
    for j in range(i,n):
        #print "i=",i,"    j=",j
        #print "(",matriz[j][i-1],"-",matriz[j-1][i-1],")/(",vector[j],"-",vector[j-i],")"
        matriz[j][i] = ( (matriz[j][i-1]-matriz[j-1][i-1]) / (vector[j]-vector[j-i]))
        #print "matriz[",j,"][",i,"] = ",(matriz[j][i-1]-matriz[j-1][i-1])/(vector[j]-vector[j-i])

print ("------------------------------")
print ("------------------------------")
print ("---tabela de diferenças divididas----")
t = n-1
for k in range(n):
    print (matriz[t]) 
    t = t-1
    
print ("------------------------------")
print ("------------------------------")

aprx = 0
mul = 1.0
for i in range(n):
    #print ("matriz[",i,"][",i,"]","=",matriz[i][i])
    mul = matriz[i][i];
    #print ("mul antes del ciclo j=",mul)
    for j in range(1,i+1):
        mul = mul * (punto_a_evaluar - vector[j-1])
        #print ("mul en el ciclo j=",mul)
    # print aprx
    aprx = aprx + mul

print ("------------------------------")
print("\n\n\nOs valores das diferenças divididas são:", matriz[n-1])
print ("------------------------------")
print ("o valor aproximado de f(",punto_a_evaluar,") é: ", aprx)"""
