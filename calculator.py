from tkinter import*
root=Tk()
root.geometry("700x600")
root.title("Calculator")
def click(event):
    global val
    text=event.widget.cget("text")
    if text=="=":
        if val.get().isdigit():
            val=int(val.get())
        else:
            value=eval(display.get())
        val.set(value)
        display.update()

    elif text=="C":
        val.set("")
        display.update()

    else:
        val.set(val.get()+text)
        display.update()
val= StringVar()
val.set("")
display=Entry(root,textvariable=val,font=("arial 20"))
display.pack(fill=X,padx=20,pady=5)
frame=Frame(root,bg="blue",borderwidth=6,relief=RIDGE)
b=Button(frame,fg="blue",text="9",font="lucida 18")
b.pack(side=LEFT,padx=10,pady=5)
b.bind("<Button-1>",click)

b=Button(frame,fg="blue",text="8",font="lucida 18")
b.pack(side=LEFT,padx=10,pady=5)
b.bind("<Button-1>",click)

b=Button(frame,fg="blue",text="7",font="lucida 18")
b.pack(side=LEFT,padx=10,pady=5)
b.bind("<Button-1>",click)
frame.pack()

frame=Frame(root,bg="blue",borderwidth=6,relief=RIDGE)
b=Button(frame,fg="blue",text="6",font="lucida 18")
b.pack(side=LEFT,padx=10,pady=5)
b.bind("<Button-1>",click)

b=Button(frame,fg="blue",text="5",font="lucida 18")
b.pack(side=LEFT,padx=10,pady=5)
b.bind("<Button-1>",click)

b=Button(frame,fg="blue",text="4",font="lucida 18")
b.pack(side=LEFT,padx=10,pady=5)
b.bind("<Button-1>",click)
frame.pack()

frame=Frame(root,bg="blue",borderwidth=6,relief=RIDGE)
b=Button(frame,fg="grey",text="3",font="lucida 18")
b.pack(side=LEFT,padx=10,pady=5)
b.bind("<Button-1>",click)

b=Button(frame,fg="blue",text="2",font="lucida 18")
b.pack(side=LEFT,padx=10,pady=5)
b.bind("<Button-1>",click)

b=Button(frame,fg="blue",text="1",font="lucida 18")
b.pack(side=LEFT,padx=10,pady=5)
b.bind("<Button-1>",click)
frame.pack()
frame=Frame(root,bg="blue",borderwidth=6,relief=RIDGE)
b=Button(frame,fg="blue",text="0",font="lucida 18")
b.pack(side=LEFT,padx=10,pady=5)
b.bind("<Button-1>",click)

b=Button(frame,fg="blue",text="+",font="lucida 18")
b.pack(side=LEFT,padx=10,pady=5)
b.bind("<Button-1>",click)

b=Button(frame,fg="blue",text="-",font="lucida 18")
b.pack(side=LEFT,padx=10,pady=5)
b.bind("<Button-1>",click)
frame.pack()

frame=Frame(root,bg="blue",borderwidth=6,relief=RIDGE)
b=Button(frame,fg="blue",text="/",font="lucida 18")
b.pack(side=LEFT,padx=10,pady=5)
b.bind("<Button-1>",click)

b=Button(frame,fg="blue",text="%",font="lucida 18")
b.pack(side=LEFT,padx=10,pady=5)
b.bind("<Button-1>",click)

b=Button(frame,fg="blue",text="C",font="lucida 18")
b.pack(side=LEFT,padx=10,pady=5)
b.bind("<Button-1>",click)
frame.pack()
frame=Frame(root,bg="blue",borderwidth=6,relief=RIDGE)
b=Button(frame,fg="blue",text="=",font="lucida 18")
b.pack(side=LEFT,padx=10,pady=5)
b.bind("<Button-1>",click)

b=Button(frame,fg="blue",text=".",font="lucida 18")
b.pack(side=LEFT,padx=10,pady=5)
b.bind("<Button-1>",click)

b=Button(frame,fg="blue",text="00",font="lucida 18")
b.pack(side=LEFT,padx=10,pady=5)
b.bind("<Button-1>",click)
frame.pack()
root.mainloop()