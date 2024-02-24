import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
from tkinter import font as tkFont
import subprocess
import shutil
import os
import re


iindex=0
list1=[]
list2=[]
list3=None
text_areas=None
class BareboneBuilder:
    def __init__(self, root):
        i:int=0
        self.root = root
        self.root.title("function database")

        self.menubar = tk.Menu(self.root,bg='red')
        self.mainmenu = tk.Menu(self.menubar, tearoff=0,bg='red')
        
        self.text_ = tk.Text(self.root, height=1, width=50,bg='red')
        self.text_.pack(pady=5)
        self.ls=Listbox(self.root, height=10, width=50,bg='red')
        self.ls.pack(pady=5)
        list3=self.ls
        # Área de texto
        self.text_area = tk.Text(self.root, height=25, width=80,bg='red')
        self.text_area.pack(pady=5)
        

        

        # Botões
        self.build_button = self.mainmenu.add_command( label="new file", command=self.build_kernel)
        

        self.run_button = self.mainmenu.add_command(label="load file", command=self.run_kernel)
        

        
        

        self.copy_button = self.mainmenu.add_command(label="new card", command=self.news)
        
        self.copy_button = self.mainmenu.add_command(label="select card", command=self.selects)
        self.b5=self.menubar.add_cascade(label="main", menu=self.mainmenu)
        self.b4=self.root.configure(menu=self.menubar,bg='red')
        
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
        heads=heads.replace("\r\n","\n")
        heads=heads.replace("\n\r","\n")
        heads=heads.replace("\r","\n")
        heads=heads.replace("\n\n\n\n\n\n","\n")
        heads=heads.replace("\n\n\n\n\n","\n")
        heads=heads.replace("\n\n\n\n","\n")
        heads=heads.replace("\n\n\n","\n")
        heads=heads.replace("\n\n","\n")
        for n in range(iindex):
            self.ls.delete(0) 
        iindex=0
         

        ff1=heads.split("\n")
        beford:int=0
        sss=""
        s1="defines"
        
        for n in ff1:
            t:bool=False
            ppos1=n.find("(")
            ppos2=n.find(")")
            ppos3=n.find("}")
            ppos4=n.find(";")
            ppos5=n.find("int ")
            ppos6=n.find("void ")
            ppos7=n.find("long ")
            ppos8=n.find("float ")
            ppos9=n.find("double ")
            ppos10=n.find("size_t ")
            ppos11=n.find("char ")
            ppos15=n.find("int*")
            ppos16=n.find("void*")
            ppos17=n.find("long*")
            ppos18=n.find("float*")
            ppos19=n.find("double*")
            ppos20=n.find("size_t*")
            ppos21=n.find("char*")

            ooor:bool=ppos5>-1 or ppos6>-1 or ppos7>-1 or ppos8>-1 or ppos9>-1 or ppos10>-1 or ppos11>-1 or ppos15>-1 or ppos16>-1 or ppos17>-1 or ppos18>-1 or ppos19>-1 or ppos20>-1 or ppos21>-1
            
            if beford>-1 and ppos1>-1 and ppos2>-1 and ppos4<0 and ooor:
                
                try:
                    if 0==0:
                        
                        fff1:str=s1
                
                        fff2:str=sss
                        list1=list1+[fff1]
                        self.ls.insert(iindex,fff1)
                        list2=list2+[fff2]
                        iindex+=1
                        s1=n
                        sss=n+"\n"
                except:
                    print(n)
            else:
                sss=sss+"\n"+n
            beford=ppos3;
        if 0==0:
            try:
                if 0==0:
                    fff1:str=s1
                   
                    fff2:str=sss
                    list1=list1+[fff1]
                    self.ls.insert(iindex,fff1)
                    list2=list2+[fff2]
                    iindex+=1
                    s1=n
                    sss=n+"\n"
            except:
               print(n)




if __name__ == "__main__":
    root = tk.Tk()
    builder = BareboneBuilder(root)
    root.mainloop()
