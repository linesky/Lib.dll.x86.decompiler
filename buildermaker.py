import tkinter as tk
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
import subprocess
import shutil
import os


files="makefile"
objss="CC=gcc\nobjects : "
programss=""
pp="prog : $(objects)\n    $(cc) $(objects) -o prog"
clearss="clear : rm "
class BareboneBuilder:
    def __init__(self, root):
        self.root = root
        self.root.title("Barebone Builder")

        # Janela amarela
        self.root.configure(bg='blue')

        # Área de texto
        self.text_area = tk.Text(self.root, height=10, width=50)
        self.text_area.pack(pady=10)

        # Botões
        self.build_button = tk.Button(self.root, text="add file", command=self.build_kernel)
        self.build_button.pack(pady=5)

        self.run_button = tk.Button(self.root, text="close", command=self.run_kernel)
        self.run_button.pack(pady=5)

        self.copy_button = tk.Button(self.root, text="new file", command=self.copy_file)
        self.copy_button.pack(pady=5)
    def pbacks(self,filename):
        fff=filename.find(".")
        if fff>-1:
            #fff-=1
            filename=filename[0:fff]
        return filename
    def backs(self,filename):
        if 0==0:
            loops=True
            while loops:
                init=filename.find("/")
                if init>-1:
                    init+=1
                    filename=filename[init:]
                else:
                    loops=False
        return filename
    def execute_command(self, command,show:bool):
        try:
            
            result = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True, text=True)
            self.text_area.insert(tk.END, result)
        except subprocess.CalledProcessError as e:
            if show:
                self.text_area.insert(tk.END,f"Error executing command:\n{e.output}")

    def build_kernel(self):
        global objss
        global programss
        global clearss
        global files
        global pp
        filename = tk.filedialog.askopenfilename(title="Select file")
        self.text_area.insert(tk.END,filename+ "\n")
        objss=objss + " " +self.pbacks(self.backs(filename))+".o"
        programss=programss+self.pbacks(self.backs(filename))+ ".o : " + self.pbacks(self.backs(filename))+".o\n"+ "    $(CC) -c -o "+self.pbacks(self.backs(filename))+".o" +" " +self.backs(filename)+"\n\n"
        clearss=clearss + " " +self.pbacks(self.backs(filename))+".o"

 
                
            
    def run_kernel(self):
        global objss
        global programss
        global clearss
        global files
        global pp
        self.text_area.delete(1.0, tk.END)
        f1=open(files,"w")
        f1.write(objss+"\n\n")
        f1.write(pp+"\n\n")
        f1.write(programss+"\n\n")
        f1.write(clearss+"\n\n")
        f1.close()
        self.text_area.insert(tk.END,objss+"\n\n"+pp+"\n\n"+programss+"\n\n"+clearss+"\n\n")

    def copy_file(self):
        global objss
        global programss
        global clearss
        global files
        global pp
        self.text_area.delete(1.0, tk.END)
        self.text_area.insert(tk.END, "new file makefile\n")
        objss="CC=gcc\nobjects : "
        programss=""
        clearss="clear : rm "
        pp="prog : $(objects)\n    $(cc) $(objects) -o prog"


if __name__ == "__main__":
    root = tk.Tk()
    builder = BareboneBuilder(root)
    root.mainloop()
