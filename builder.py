import tkinter as tk
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
import subprocess
import shutil
import os


files="new.sh"
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

        self.run_button = tk.Button(self.root, text="run", command=self.run_kernel)
        self.run_button.pack(pady=5)

        self.copy_button = tk.Button(self.root, text="new file", command=self.copy_file)
        self.copy_button.pack(pady=5)

    def execute_command(self, command,show:bool):
        try:
            
            result = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True, text=True)
            self.text_area.insert(tk.END, result)
        except subprocess.CalledProcessError as e:
            if show:
                self.text_area.insert(tk.END,f"Error executing command:\n{e.output}")

    def build_kernel(self):
        filename = tk.filedialog.askopenfilename(title="Select file")
        self.text_area.delete(1.0, tk.END)
        if filename:
            loops=True
            while loops:
                init=filename.find("/")
                if init>-1:
                    init+=1
                    filename=filename[init:]
                else:
                    loops=False
            f1=open(files,"a")
            f2=filename.find(".asm")
            if f2<0:
                f2=filename.find(".ASM")
            if f2<0:
                f2=filename.find(".s")
            if f2<0:
                f2=filename.find(".S")
            if f2<0:
                f2=filename.find(".ASM")
            if f2>-1:
                f1.write(('as -f elf32 "$1" -o "/tmp/$1.o"\n').replace("$1",filename))
            f2=filename.find(".c")
            if f2<0:
                f2=filename.find(".C")
            if f2<0:
                f2=filename.find(".CC")
            if f2<0:
                f2=filename.find(".cc")
            if f2>-1:
                f1.write(('gcc -c "$1" -o "/tmp/$1.o"\n').replace("$1",filename))           

            f2=filename.find(".cpp")
            if f2<0:
                f2=filename.find(".CPP")
            if f2>-1:
                f1.write(('g++ -c "$1" -o "/tmp/$1.o"\n').replace("$1",filename))
            f2=filename.find(".bas")
            if f2<0:
                f2=filename.find(".BAS")
            if f2>-1:
                f1.write(('fbc -c "$1" -o "/tmp/$1.o"\n').replace("$1",filename))
            f2=filename.find(".pas")
            if f2<0:
                f2=filename.find(".PAS")
            if f2>-1:
                f1.write(('fpc -c "$1" -o "/tmp/$1.o"\n').replace("$1",filename))
            f1.close()
    def run_kernel(self):
        self.text_area.delete(1.0, tk.END)
        filename = tk.filedialog.askopenfilename(title="Select file")
        self.execute_command('bash "$1"'.replace("$1",filename),True)


    def copy_file(self):
        self.text_area.delete(1.0, tk.END)
        filename = tk.filedialog.asksaveasfilename(title="Select file")
        files=filename
        if filename:
            f1=open(filename,"w")
            f1.write('printf "\x1bc\x1b[44;37m"\n')
            f1.close()


if __name__ == "__main__":
    root = tk.Tk()
    builder = BareboneBuilder(root)
    root.mainloop()
