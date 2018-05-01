from tkinter import Tk, Frame, Label, Entry, Button, LEFT, RIGHT

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

        self.result = Label(self.container3, text="")
        self.result.pack()
        
        self.txt_box = Entry(self.container1)
        self.txt_box.pack()

        self.convert = Button(self.container2)
        self.convert["text"] = "Converter"
        self.convert["command"] = self.set_text
        #self.convert.bind("<Button-1>", self.set_text())
        self.convert.pack(side=LEFT)
        self.sair = Button(self.container2)
        self.sair["text"] = "Sair"
        self.sair["command"] = self.container1.quit
        self.sair.pack()

    def set_text(self):
        text = str(self.float2bin(str(self.txt_box.get())))
        self.result["text"] = "Resultado = " + text
        print (text)

    def int2bin(self, num):
        binary = ""

        while num >= 1:
            binary += str(num % 2)
            num = int(num / 2)

        binary = binary[::-1]

        return binary

    def frac2bin(self, num):
        binary = ""

        while num % 1 != 0:
            num = num % 1 * 2
            binary += str(int(num // 1))
        
        return binary

    def float2bin(self, num):
        if not num == "":
            
            if num.find(".") != -1:
                num = num.split(".")
                num[1] = "0." + num[1]
                integer = self.int2bin(int(num[0])) if num[0] != "0" else "0"
                if float(num[1]) != 0:
                    frac = self.frac2bin(float(num[1]))
                else:
                    frac = "0"

                return integer + "." + frac

            else:
                integer = self.int2bin(int(num))
                return integer + "." + "0"


GUI = Tk()
App(GUI)
GUI.title("Decimal para binário")
GUI.geometry("300x100")

GUI.mainloop()
