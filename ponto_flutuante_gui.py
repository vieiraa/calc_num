from tkinter import Tk, Frame, Label, Entry, Button, LEFT, RIGHT
import matplotlib.pyplot as plt
import numpy as np

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

        self.label1 = Label(self.container1, text="Precisão:")
        self.label1.pack(side=LEFT)

        self.label2 = Label(self.container2, text="Limite underflow:")
        self.label2.pack(side=LEFT)

        self.label3 = Label(self.container3, text="Limite overflow:")
        self.label3.pack(side=LEFT)

        self.prec = Entry(self.container1)
        self.prec.pack()

        self.lower = Entry(self.container2)
        self.lower.pack()

        self.upper = Entry(self.container3)
        self.upper.pack()

        self.calcular = Button(self.container4)
        self.calcular["text"] = "Plotar"
        self.calcular["command"] = self.plot
        self.calcular.pack(side=LEFT)
        self.sair = Button(self.container4)
        self.sair["text"] = "Sair"
        self.sair["command"] = self.container1.quit
        self.sair.pack()

    def plot(self):
        prec = int(self.prec.get())
        lower = int(self.lower.get())
        upper = int(self.upper.get())
        base = 10
        maior_numero = base**upper*(1-base**(-prec))
        nums = []
        
        for numero in range(0, int(maior_numero), 1):
            print('_________{:.02f}_________%'.format((numero/maior_numero)*100))
            
            for expoente in range(lower, upper+1):
                x = numero * (10**(expoente - len(str(numero))))
                nums.append(x)
                nums.append(-x)
                print('X: {}, Numero: {}, Expoente: {}'.format(x, numero, expoente))
                
        plt.plot(nums, np.zeros_like(nums) + .0, '|')
        plt.show()
        #return nums
        
GUI = Tk()
App(GUI)
GUI.title("Ponto flutuante")
GUI.geometry("300x110")
GUI.mainloop()
