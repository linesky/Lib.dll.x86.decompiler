
import tkinter as tk
#Window=None
returnvalue:str=""
def inputbox(msgs:str,yes,color:str):
    global returnvalue
    listsb:list=[]
    lists=[]
    lista:list=[]
    checkss=[]
    Window = tk.Toplevel(bg=color)
    frametop = tk.Frame(Window,bg='red')
    frametop.pack( side = "top" )

    text_ = tk.Label(Window,text=msgs,bg='red')
    text_.pack(pady=5)
    for n in range(10):
        lists=lists+[""]
        listsb=listsb+[False]
        checkss=checkss+[None]
    lista=lista+[lists[0]]
    listsb[0]=False


    lista=lista+[lists[0]]
    listsb[0]=False
    checkss=checkss+[tk.Checkbutton(frametop,text="x86",bg=color,variable=lambda:id(listsb[0]),onvalue=True,offvalue=False).grid(row=0, column=0)]
    lista=lista+[lists[1]]
    listsb[1]=False
    checkss=checkss+[tk.Checkbutton(frametop,text="8086",bg=color,variable=lambda:listsb[1],onvalue=True,offvalue=False).grid(row=1, column=0)]
    lista=lista+[lists[2]]
    listsb[2]=False
    checkss=checkss+[tk.Checkbutton(frametop,text="80186",bg=color,variable=lambda:listsb[2],onvalue=True,offvalue=False).grid(row=2, column=0)]
    lista=lista+[lists[3]]
    listsb[3]=False
    checkss=checkss+[tk.Checkbutton(frametop,text="80286",bg=color,variable=lambda:listsb[3],onvalue=True,offvalue=False).grid(row=3, column=0)]
    lista=lista+[lists[4]]
    listsb[4]=False
    checkss=checkss+[tk.Checkbutton(frametop,text="80386",bg=color,variable=lambda:listsb[4],onvalue=True,offvalue=False).grid(row=4, column=0)]
    lista=lista+[lists[5]]
    listsb[5]=False
    checkss=checkss+[tk.Checkbutton(frametop,text="80487",bg=color,variable=lambda:listsb[5],onvalue=True,offvalue=False).grid(row=5, column=0)]
    lista=lista+[lists[6]]
    listsb[6]=False
    checkss=checkss+[tk.Checkbutton(frametop,text="arm",bg=color,variable=lambda:listsb[6],onvalue=True,offvalue=False).grid(row=6, column=0)]
    lista=lista+[lists[7]]
    listsb[7]=False
    checkss=checkss+[tk.Checkbutton(frametop,text="arm7",bg=color,variable=lambda:listsb[7],onvalue=True,offvalue=False).grid(row=7, column=0)]

    bo=tk.Button(Window,text="yes",bg=color,command=lambda:yes(text_,listsb))
    bo.pack()
    

def setvarssyes(W,ll:list):
    
    lll:list=[]
    for n in range(len(ll)):
        if ll[n]:
            lll=lll+[ll[n]]
    W.text=str(lll)

root = tk.Tk()
root.title("msgbox")

button = tk.Button(root, text="msgbox", bg='red', fg='Black',
                              command=lambda:inputbox("hello world....hello world....hello world....",setvarssyes,'red'))

button.pack()
root.mainloop()