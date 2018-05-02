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
    top.title("Cholesky")
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
        G, GT = cholesky(A)
        G = str(G)
        GT = str(GT)
        res["text"] = "\nG: " + G[1:len(G)-1]
        res["text"] += "\nGT: " + GT[1:len(GT)-1]
        res["justify"] = "right"
    except alg.LinAlgError:
        messagebox.showerror("Erro", "Matriz não é positiva definida.")
    except ValueError:
        messagebox.showerror("Erro", "Matriz é singular.")
        
def cholesky(A):
    if alg.det(A) == 0:
        raise ValueError
    else:
        G = alg.cholesky(A, lower=True)
        GT = alg.cholesky(A, overwrite_a=True)
        
        return (G, GT)
    
GUI = Tk()
GUI.title("Cholesky")
App(GUI)
GUI.mainloop()
