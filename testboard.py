import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename


keyss=[]
bottomframe=None
class BareboneBuilder:
    def __init__(self, root):
        global keyss
        i:int=0
        self.root = root
        self.root.title("view")
        frame = Frame(self.root)
        frame.pack()
        # Janela amarela
        self.root.configure(bg='red')
        self.topframe = Frame(frame,bg='red')
        self.topframe.pack( side = TOP )

        self.bottomframe = Frame(frame,bg='red')
        self.bottomframe.pack( side = BOTTOM )
        # Botões
        for n in range(10):
            keyss=keyss+[""]

        keyss[0]=tk.Button(self.bottomframe, text='x1',command=lambda:self.ckeyss('x1') ,borderwidth=1,bg='red').grid(row=0, column=0)

        keyss[1]=tk.Button(self.bottomframe, text='x2',command=lambda:self.ckeyss('x2') ,borderwidth=1,bg='red').grid(row=0, column=1)

        keyss[2]=tk.Button(self.bottomframe, text='x3',command=lambda:self.ckeyss('x3') ,borderwidth=1,bg='red').grid(row=1, column=0)

        keyss[3]=tk.Button(self.bottomframe, text='x4',command=lambda:self.ckeyss('x4') ,borderwidth=1,bg='red').grid(row=1, column=1)

        keyss[4]=tk.Button(self.bottomframe, text='x5',command=lambda:self.ckeyss('x5') ,borderwidth=1,bg='red').grid(row=2, column=0)

        keyss[5]=tk.Button(self.bottomframe, text='x6',command=lambda:self.ckeyss('x6') ,borderwidth=1,bg='red').grid(row=2, column=1)





    def ckeyss(self,s:str):
        print(s)


    

if __name__ == "__main__":
    root = tk.Tk()
    builder = BareboneBuilder(root)
    root.mainloop()
