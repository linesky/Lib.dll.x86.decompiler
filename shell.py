import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
from tkinter import font as tkFont
import subprocess
import shutil
import os


iindex=0
list1=[]
list2=[]
list3=None
text_areas=None
class BareboneBuilder:
    def __init__(self, root):
        i:int=0
        self.root = root
        self.root.title("shell")

        self.menubar = tk.Menu(self.root,bg='red')
        self.mainmenu = tk.Menu(self.menubar, tearoff=0,bg='red')
        
        self.text_ = tk.Text(self.root, height=1, width=80,bg='red')
        self.text_.pack(pady=5)
        self.ls=Listbox(self.root, height=25, width=80,bg='red')
        self.ls.pack(pady=5)
        list3=self.ls
        # Área de texto
        self.text_area = tk.Text(self.root, height=1, width=80,bg='red')
        self.text_area.pack(pady=5)
        

        

        # Botões
        self.build_button = self.mainmenu.add_command( label="new file", command=self.build_kernel)
        

        self.run_button = self.mainmenu.add_command(label="load file", command=self.run_kernel)
        

        self.copy_button = self.mainmenu.add_command(label="save file", command=self.copy_file)
        

        self.copy_button = self.mainmenu.add_command(label="new card", command=self.news)
        
        self.copy_button = self.mainmenu.add_command(label="select card", command=self.selects)
        self.run_button = self.mainmenu.add_command(label="run", command=self.execute_command)
        self.b5=self.menubar.add_cascade(label="main", menu=self.mainmenu)
        self.b4=self.root.configure(menu=self.menubar,bg='red')
    def execute_command(self):
        try:
            commandss=self.text_area.get("1.0", "end-1c")
            filename = tk.filedialog.askopenfilename(title="load file")
            commandss=commandss.replace("$0",filename)
            result = subprocess.check_output(commandss, stderr=subprocess.STDOUT, shell=True, text=True)
            print( result)
        except subprocess.CalledProcessError as e:
            if 0==0:
                print(f"Error executing command:\n{e.output}")        
    
    def news(self):
        global list1
        global list2
        global iindex
        list1=list1+[str(self.text_.get("1.0", "end-1c"))]
        self.ls.insert(iindex,str(self.text_.get("1.0", "end-1c")))
        list2=list2+[str(self.text_area.get("1.0", "end-1c"))]
        iindex+=1

    def selects(self):
        global list1
        global list2
        global iindex
        if self.ls.curselection()[0]<0:
            return 0
        self.text_.delete(1.0, tk.END)

        self.text_area.delete(1.0, tk.END)
    
        self.text_.insert(tk.END,list1[self.ls.curselection()[0]] )
        self.text_area.insert(tk.END,list2[self.ls.curselection()[0]] )



    def build_kernel(self):
        global list1
        global list2
        global iindex
        list1=[]
        list2=[]
        for n in range(iindex):
            self.ls.delete(0) 
        iindex=0
         
        self.text_.delete(1.0, tk.END)

        self.text_area.delete(1.0, tk.END)
        
        
        
       
    def run_kernel(self):
        global list1
        global list2
        global iindex
        list1=[]
        list2=[]

        filename = tk.filedialog.askopenfilename(title="load file")
        f1=open(filename,"r")
        heads=f1.read()
        f1.close()
        self.text_area.insert(tk.END,"" )
        self.text_.insert(tk.END,"" )
        for n in range(iindex):
            self.ls.delete(0) 
        iindex=0


        ff1=heads.split("\x01|")
        for n in ff1:
            ff2=n.split("\x02=")
            try:
                
                fff1:str=ff2[0]
                
                fff2:str=ff2[1]
                list1=list1+[fff1]
                self.ls.insert(iindex,fff1)
                list2=list2+[fff2]
                iindex+=1

            except:
                fff1=""

    def copy_file(self):
        global list1
        global list2
        global iindex
        heads=self.text_area.get("1.0", "end-1c")
        filename = tk.filedialog.asksaveasfilename(title="save file")
        heads=""
        for n in range(len(list1)):
            heads=heads+list1[n]+"\x02="+list2[n]+"\x01|"
        f2=open(filename,"w")
        f2.write(heads)
        f2.close()




if __name__ == "__main__":
    root = tk.Tk()
    builder = BareboneBuilder(root)
    root.mainloop()
