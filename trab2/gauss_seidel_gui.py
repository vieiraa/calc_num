import numpy as np
from numpy import array, zeros, diag, diagflat, dot, absolute
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
    top.title("Método de Gauss-Seidel")
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
    
    er = Label(container4)
    er["text"] = "err="
    er.pack(side="left")
    er = Entry(container4, width=5)
    er.pack(side="left")
    
    matriz = Button(container5)
    matriz["text"] = "Calcular"
    matriz["command"] = lambda: result(a, b, er, res, num)
    matriz.pack()
    
    res = Label(container6)
    res["text"] = "Resultado: "
    res.pack()
    
def result(a, b, err, res, num):
    A = ""
    B = ""
    er = 0
    
    for i in range(num):
        v = ""
        B += str(b[i].get()) + ";"
        
        for j in range(num):
            index = (i, j)
            
            v += str(a[index].get()) + ","
        
        A += v[:len(v)-1] + ";"
        
    er = float(err.get())
    A = np.mat(A[:len(A)-1])
    B = np.mat(B[:len(B)-1])

    r = ""
    try:
        r = gauss_seidel(A, B, er, num)
        res["text"] = "Resultado: " + r
    except ValueError:
        messagebox.showerror("Erro", "Critério das linhas não cumprido.")

def gauss_seidel(A, b, error_s, num_eq):
    if not converge_condition(A):
        raise ValueError

    [m, n] = np.shape(A)

    U = np.triu(A, 1)
    L = np.tril(A)

    x = np.ones((m,1))
    
    err = 0
    
    while True:
        xn = np.dot(np.linalg.inv(L), (b - np.dot(U, x)))
        
        x_dif = []
        for i in range(num_eq):
            x_dif.append(abs(xn[i] - x[i]))
            
        err = abs(np.max(x_dif)/np.max(xn))
        x = xn
        
        if err < error_s:
            break
    
    res = ""
    for i in range(m):
        res += ('\nx[%0.0f] = %6.4f' % (i+1, x[i]))
        
    return res + "\nErro = " + str(err)

def converge_condition(A):
    D = diag(A)
    R = A - diagflat(D)

    alpha = zeros(len(A[0]))
    for i in range(len(A)):
        for j in range(len(A[0])):
            alpha[i] += R[i][j]
        alpha[i] = (alpha[i]/A[i][i]) 

    maxAlpha = float(max(alpha))

    if(maxAlpha<1.0):
        return True
    
    return False

GUI = Tk()
GUI.title("Método de Gauss-Seidel")
App(GUI)
GUI.mainloop()
