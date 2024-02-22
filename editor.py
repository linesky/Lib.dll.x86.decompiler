import tkinter as tk
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
import subprocess
import shutil
import os



class BareboneBuilder:
    def __init__(self, root):
        i:int=0
        self.root = root
        self.root.title("editor")

        # Janela amarela
        self.root.configure(bg='red')

        # Área de texto
        self.text_area = tk.Text(self.root, height=10, width=50)
        self.text_area.pack(pady=10)

        # Botões
        self.build_button = tk.Button(self.root, text="new file", command=self.build_kernel)
        self.build_button.pack(pady=5)

        self.run_button = tk.Button(self.root, text="load file", command=self.run_kernel)
        self.run_button.pack(pady=5)

        self.copy_button = tk.Button(self.root, text="save file", command=self.copy_file)
        self.copy_button.pack(pady=5)



    def build_kernel(self):
        
        self.text_area.delete(1.0, tk.END)
        
        
        
       
    def run_kernel(self):
        filename = tk.filedialog.askopenfilename(title="load file")
        self.text_area.delete(1.0, tk.END)
        f1=open(filename,"r")
        heads=f1.read()
        f1.close()
        self.text_area.insert(tk.END,heads )



    def copy_file(self):
        
        heads=self.text_area.get("1.0", "end-1c")
        filename = tk.filedialog.asksaveasfilename(title="save file")
        f2=open(filename,"w")
        f2.write(heads)
        f2.close()



if __name__ == "__main__":
    root = tk.Tk()
    builder = BareboneBuilder(root)
    root.mainloop()
