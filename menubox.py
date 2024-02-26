
import tkinter as tk
#Window=None
returnvalue:str=""
def menubox(msgs:str,value,color:str,llist:list):
    global returnvalue
    Window = tk.Toplevel(bg=color)
    text_ = tk.Label(Window,text=msgs,height=1, width=50,bg='red')
    text_.pack(pady=5)   
    ls=tk.Listbox(Window, height=10, width=50,bg='red')
    ls.pack(pady=5)
    i=0
    for n in llist:
        ls.insert(i,n)
        i+=1
    bo=tk.Button(Window,text="OK",bg=color,command=lambda:value(ls.curselection(),Window))
    bo.pack()
    
    

def setvarssyes(my:int,W):
    returnvalue=my
    W.title(str(returnvalue))
root = tk.Tk()
root.title("msgbox")
menuss=["8086","80186","80286","80386","80486","arm"]
button = tk.Button(root, text="msgbox", bg='red', fg='Black',command=lambda:menubox("hello world....",setvarssyes,'red',menuss))
button
button.pack()
root.mainloop()