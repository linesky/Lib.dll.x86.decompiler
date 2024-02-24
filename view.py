import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename



bottomframe=None
class BareboneBuilder:
    def __init__(self, root):
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
        
        self.run_button = tk.Button(self.topframe, text="load file", command=self.run_kernel,bg='red')
        self.run_button.pack(pady=5)

        
        
        
       
    def run_kernel(self):
        filename = tk.filedialog.askopenfilename(title="load file")
        f1=open(filename,"r")
        heads=f1.read()
        f1.close()
        
        fff=heads.split("\x01|")
        fr=len(fff)
        for n in range(fr):
            
            ff1=fff[n].split("\x02=")
            
            frr=len(ff1)
            for m in range(frr):
                tk.Label(self.bottomframe, text=str(ff1[m]),borderwidth=1,bg='red').grid(row=n, column=m)
                



    

if __name__ == "__main__":
    root = tk.Tk()
    builder = BareboneBuilder(root)
    root.mainloop()
