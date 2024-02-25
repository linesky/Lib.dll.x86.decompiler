
import tkinter as tk
#Window=None
returnvalue:str=""
def inputbox(msgs:str,value:str,color:str):
    global returnvalue
    Window = tk.Toplevel(bg=color)
    text_ = tk.Text(Window, height=1, width=50,bg='red')
    text_.pack(pady=5)   
    bo=tk.Button(Window,text="OK",bg=color,command=lambda:setvarss(str(text_.get("1.0", "end-1c")),Window))
    bo.pack()
    text_.insert(tk.END,returnvalue)

def setvarss(my:str,W):
    returnvalue=my
    W.title(str(returnvalue))

root = tk.Tk()
root.title("msgbox")
button = tk.Button(root, text="msgbox", bg='red', fg='Black',
                              command=lambda:inputbox("hello world....",setvarss,'red'))
button
button.pack()
root.mainloop()