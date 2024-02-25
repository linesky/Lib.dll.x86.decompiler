
import tkinter as tk
#Window=None
def msgbox(msgs:str,color:str):
    Window = tk.Toplevel(bg=color)
    lll = tk.Label(Window,text=msgs,bg=color)
    lll.pack()
    bo=tk.Button(Window,text="OK",bg=color,command=lambda:Window.quit())
    bo.pack()


root = tk.Tk()
root.title("msgbox")
button = tk.Button(root, text="msgbox", bg='red', fg='Black',
                              command=lambda:msgbox("hello world....",'red'))

button.pack()
root.mainloop()