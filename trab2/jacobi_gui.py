from numpy import array, zeros, diag, diagflat, dot, absolute
import numpy as np
from tkinter import Tk, Frame, Label, Entry, Button, Toplevel, messagebox

class App:
    def __init__(self, master=None):
        self.container1 = Frame(master)
        self.container1.pack()

        self.container2 = Frame(master)
        self.container2.pack()

        self.label1 = Label(self.container1, text="Número de funções:")
        self.label1.pack(side="left")        

        self.func = Entry(self.container1, width=5)
        self.func.pack()

        self.matriz = Button(self.container2)
        self.matriz["text"] = "Matriz"
        self.matriz["command"] = self.matrix
        self.matriz.pack(side="left")
        self.sair = Button(self.container2)
        self.sair["text"] = "Sair"
        self.sair["command"] = self.container1.quit
        self.sair.pack()
                
    def matrix(self):
        num = int(self.func.get())
        
        if num < 2 or num > 8:
            messagebox.showerror("Erro", "Número de equações deve ser 2 <= n <= 8")
            return
            
        matrix_window(num)

def matrix_window(num):
    top = Toplevel()
    top.title("Método de Jacobi")
    container = []
    
    a = {}
    first = True
    
    for i in range(num):
        c = Frame(top)
        c.pack()
        container.append(c)
        
        for j in range(num):    
            if first:
                A = Label(c)
                A["text"] = "A="
                A.pack(side="left")
                first = False
            index = (i, j)
            e = Entry(c, width=5)
            e.pack(side="left")
            a[index] = e
            
    container2 = Frame(top)
    container2.pack()
    container3 = Frame(top)
    container3.pack()
    container4 = Frame(top)
    container4.pack()
    container5 = Frame(top)
    container5.pack()
    container6 = Frame(top)
    container6.pack()
    
    B = Label(container2)
    B["text"] = "b="
    B.pack(side="left")
    b = []
    
    for i in range(num):
        e = Entry(container2, width=5)
        e.pack(side="left")
        b.append(e)
            
    X = Label(container3)
    X["text"] = "x="
    X.pack(side="left")
    x = []
    
    for i in range(num):
        e = Entry(container3, width=5)
        e.pack(side="left")
        x.append(e)
    
    er = Label(container4)
    er["text"] = "err="
    er.pack(side="left")
    er = Entry(container4, width=5)
    er.pack(side="left")
    
    matriz = Button(container5)
    matriz["text"] = "Calcular"
    matriz["command"] = lambda: result(a, b, x, er, res, num)
    matriz.pack()
    
    res = Label(container6)
    res["text"] = "Resultado: "
    res.pack()
    
def result(a, b, x, err, res, num):
    A = []
    B = []
    X = []
    er = 0
    
    for i in range(num):
        v = []
        B.append(float(b[i].get()))
        X.append(float(x[i].get()))
        
        for j in range(num):
            index = (i, j)
            
            v.append(float(a[index].get()))
            
            er = float(err.get())
        
        A.append(v)
        
    A = array(A)
    B = array(B)
    X = array(X)

    if not converge_condition(A):
        messagebox.showwarning("Aviso", "Critério das linhas não cumprido.")
    
    r = jacobi(A, B, er, X)

    res["text"] = "Resultado: " + r

def jacobi(A,b,err, x=None, N = 25):                                                                                                                           
    if x is None:
        x = zeros(len(A[0]))
    
    xn = x                                                                                                                                                                  
    D = diag(A)
    R = A - diagflat(D)
    
    i = 0
    e = 0
                                                                                                                                                                      
    while True:
        xn = (b - dot(R,x)) / D
        x_diff = []
        for i in range(len(A)):
            x_diff.append(xn[i] - x[i])
        
        x = xn
        e = abs(np.max(absolute(x_diff)) / np.max(absolute(xn)))
        i += 1
        
        if e < err and i < N:
            break
        
    res = ""
    
    for i in range(len(x)):
        res += "\nx[" + str(i) + "] = " + str(x[i])
        
    return res + "\nErro = " + str(e)

def converge_condition(A):
    D = diag(A)
    R = A - diagflat(D)
    alpha = zeros(len(A))
    
    for i in range(len(A)):
        for j in range(len(A)):
            alpha[i] += R[i,j]
        alpha[i] = (alpha[i]/A[i,i]) 

    maxAlpha = float(max(alpha))
    
    if(maxAlpha<1.0):
        return True
    
    return False

GUI = Tk()
GUI.title("Método de Jacobi")
App(GUI)
GUI.mainloop()

