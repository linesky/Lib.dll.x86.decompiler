
import tkinter as tk
#Window=None
returnvalue:str=""
def inputbox(msgs:str,yes,no,color:str):
    global returnvalue
    Window = tk.Toplevel(bg=color)
    text_ = tk.Label(Window,text=msgs,bg='red')
    text_.pack(pady=5)   
    bo=tk.Button(Window,text="yes",bg=color,command=lambda:yes(Window))
    bo.pack()
    bo2=tk.Button(Window,text="no",bg=color,command=lambda:no(Window))
    bo2.pack()
    

def setvarssyes(W):
    returnvalue="yes"
    W.title(str(returnvalue))
def setvarssno(W):
    returnvalue="no"
    W.title(str(returnvalue))

root = tk.Tk()
root.title("msgbox")
button = tk.Button(root, text="msgbox", bg='red', fg='Black',
                              command=lambda:inputbox("hello world....hello world....hello world....",setvarssyes,setvarssno,'red'))
button
button.pack()
root.mainloop()