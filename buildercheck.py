xx="""    lista=lista+[lists[$1]]
    listsb[$1]=False
    checkss=checkss+[tk.Checkbutton(frametop,text="$0",bg=color,variable=lambda:listsb[$1],onvalue=True,offvalue=False).grid(row=$2, column=$3)]"""
print("\x1bc\x1b[41;37m")
s=input("past key strings separete by ; order? ")
s=s.split(";")
i=1
n:int=0
m:int=0
for nn in range(len(s)//i):
    for mm in range(i):
        xxx=xx.replace("$0",s[nn*i+mm])
        xxx=xxx.replace("$1",str(nn*i+mm))
        xxx=xxx.replace("$2",str(nn))
        xxx=xxx.replace("$3",str(mm))
        print(xxx)
