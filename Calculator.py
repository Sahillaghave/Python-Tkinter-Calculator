from tkinter import *
from tkinter import messagebox as m

w=Tk()
w.title("Calculator")
w.geometry("390x500")
w.maxsize(390,500)
w.minsize(360,400)
def click(event):
    global scvalue
    global text
    text=event.widget.cget("text")
   
    if text=="=":
        if scvalue.get().isdigit():
            value=int(scvalue.get())
        else:
            value=eval(scvalue.get())
        scvalue.set(value)
    elif text=="C":
        scvalue.set("")
        scvalue.update()
    elif text=="A":
        scvalue.set("0")
        scvalue.update()

    else:
        scvalue.set(scvalue.get()+text)
scvalue=StringVar()
scvalue.set("")
screenval=Entry(w,textvariable=scvalue,font="Arial 40 bold")
screenval.pack(fill=X)


f=Frame(w,width=30,height=50,bg="violet")
f.pack(side=BOTTOM,fill="x",pady=5)      
b=Button(f,text=f"0",font="lucid 30",bg="gray",fg="white")
b.pack(side=LEFT,padx=5)
b.bind("<Button-1>",click)
b=Button(f,text=f"1",font="lucid 30",bg="gray",fg="white")
b.pack(side=LEFT,padx=5)
b.bind("<Button-1>",click)
b=Button(f,text=f"2",font="lucid 30",bg="gray",fg="white")
b.pack(side=LEFT,padx=5)
b.bind("<Button-1>",click)
b=Button(f,text=f"+",font="lucid 30",bg="gray",fg="white")
b.pack(side=LEFT,padx=5)
b.bind("<Button-1>",click)
b=Button(f,text=f"=",font="lucid 30",bg="gray",fg="white")
b.pack(side=LEFT,padx=5)
b.bind("<Button-1>",click)

f2=Frame(w,width=30,height=50,bg="violet")
f2.pack(side=BOTTOM,fill="x",pady=5)
b=Button(f2,text=f"3",font="lucid 30",bg="gray",fg="white")
b.pack(side=LEFT,padx=5)
b.bind("<Button-1>",click)
b=Button(f2,text=f"4",font="lucid 30",bg="gray",fg="white")
b.pack(side=LEFT,padx=5)
b.bind("<Button-1>",click)
b=Button(f2,text=f"5",font="lucid 30",bg="gray",fg="white")
b.pack(side=LEFT,padx=5)
b.bind("<Button-1>",click)
b=Button(f2,text=f"-",font="lucid 30",bg="gray",fg="white")
b.pack(side=LEFT,padx=5)
b.bind("<Button-1>",click)
b=Button(f2,text=f"A",font="lucid 30",bg="gray",fg="white")
b.pack(side=LEFT,padx=5)
b.bind("<Button-1>",click)


f3=Frame(w,width=30,height=50,bg="violet")
f3.pack(side=BOTTOM,fill="x",pady=5)
b=Button(f3,text=f"6",font="lucid 30",bg="gray",fg="white")
b.pack(side=LEFT,padx=5)
b.bind("<Button-1>",click)
b=Button(f3,text=f"7",font="lucid 30",bg="gray",fg="white")
b.pack(side=LEFT,padx=5)
b.bind("<Button-1>",click)
b=Button(f3,text=f"8",font="lucid 30",bg="gray",fg="white")
b.pack(side=LEFT,padx=5)
b.bind("<Button-1>",click)
b=Button(f3,text=f"9",font="lucid 30",bg="gray",fg="white")
b.pack(side=LEFT,padx=5)
b.bind("<Button-1>",click)
b=Button(f3,text=f"C",font="lucid 30",bg="gray",fg="white")
b.pack(side=LEFT,padx=5)
b.bind("<Button-1>",click)


w.mainloop()