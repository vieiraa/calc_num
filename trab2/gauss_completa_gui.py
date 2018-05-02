import scipy.linalg as alg
import scipy as sp
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
    top.title("Gauss completa")
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
            
    container5 = Frame(top)
    container5.pack()
    container6 = Frame(top)
    container6.pack()
    
    matriz = Button(container5)
    matriz["text"] = "Calcular"
    matriz["command"] = lambda: result(a, res, num)
    matriz.pack()
    
    res = Label(container6)
    res["text"] = "Resultado: "
    res.pack()
    
def result(a, res, num):
    A = []
    
    for i in range(num):
        v = []
        
        for j in range(num):
            index = (i, j)
            
            v.append(float(a[index].get()))
                    
        A.append(v)
        
    A = sp.array(A)

    r = ""
    try:
        P, L, U = gauss_completa(A)
        P = str(P)
        L = str(L)
        U = str(U)
        res["text"] = "\nP: " + P[1:len(P)-1]
        res["text"] += "\nL: " + L[1:len(L)-1]
        res["text"] += "\nU: " + U[1:len(U)-1]
        res["justify"] = "right"
    except alg.LinAlgError:
        messagebox.showerror("Erro", "Matriz é singular.")
        
def gauss_completa(A):
    if alg.det(A) == 0:
        raise alg.LinAlgError
    else:
        P, L, U = alg.lu(A)
        
        return (P, L, U)
    
GUI = Tk()
GUI.title("Gauss completa")
App(GUI)
GUI.mainloop()
