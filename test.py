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
        keyss[0]=tk.Button(self.bottomframe, text='a',command=lambda:self.ckeyss('a') ,borderwidth=1,bg='red').grid(row=0, column=0)

        keyss[1]=tk.Button(self.bottomframe, text='s',command=lambda:self.ckeyss('s') ,borderwidth=1,bg='red').grid(row=0, column=1)

        keyss[2]=tk.Button(self.bottomframe, text='d',command=lambda:self.ckeyss('d') ,borderwidth=1,bg='red').grid(row=0, column=2)

        keyss[3]=tk.Button(self.bottomframe, text='f',command=lambda:self.ckeyss('f') ,borderwidth=1,bg='red').grid(row=1, column=0)

        keyss[4]=tk.Button(self.bottomframe, text='g',command=lambda:self.ckeyss('g') ,borderwidth=1,bg='red').grid(row=1, column=1)

        keyss[5]=tk.Button(self.bottomframe, text='h',command=lambda:self.ckeyss('h') ,borderwidth=1,bg='red').grid(row=1, column=2)

        keyss[6]=tk.Button(self.bottomframe, text='j',command=lambda:self.ckeyss('j') ,borderwidth=1,bg='red').grid(row=2, column=0)

        keyss[7]=tk.Button(self.bottomframe, text='k',command=lambda:self.ckeyss('k') ,borderwidth=1,bg='red').grid(row=2, column=1)

        keyss[8]=tk.Button(self.bottomframe, text='l',command=lambda:self.ckeyss('l') ,borderwidth=1,bg='red').grid(row=2, column=2)       
    def ckeyss(self,s:str):
        print(s)


    

if __name__ == "__main__":
    root = tk.Tk()
    builder = BareboneBuilder(root)
    root.mainloop()
