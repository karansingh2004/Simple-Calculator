from tkinter import *
from PIL import Image, ImageTk

def click(event):
    text= event.widget.cget("text")     #Extract value from text
    global scvalue
    if text == "=":
        if scvalue.get().isdigit():
            value=int(scvalue.get())
        else:
            try:
                value=eval(screen.get())
            except Exception as e:
                print(e)
                scvalue.set("Error")
                screen.update()

        scvalue.set(value)
        screen.update()

    elif text == "AC":
        scvalue.set("")
        screen.update()

    else:
        scvalue.set(scvalue.get()+ text)
        screen.update()


root=Tk()
root.geometry("500x500")
root.minsize(500,500)
root.maxsize(500,500)
root.title("Apna calculator")

icon0=Image.open("calculator_icon.png")
icon=ImageTk.PhotoImage(icon0)
root.iconphoto(False, icon)



scvalue = StringVar()
scvalue.set("")

screen = Entry(root, textvar=scvalue, font="lucida 40 bold")
screen.pack(fill=X,padx=5,pady=5,ipadx=8)

# 1st frame
f = Frame(root,bg="grey",padx=8)

b= Button(f,text="9",font="lucida 17 bold",padx=15,pady=15)
b.pack(side=LEFT, padx=15, pady=12)
b.bind("<Button-1>",click)

b= Button(f,text="8",font="lucida 17 bold",padx=15,pady=15)
b.pack(side=LEFT, padx=15, pady=12)
b.bind("<Button-1>",click)

b= Button(f,text="7",font="lucida 17 bold",padx=15,pady=15)
b.pack(side=LEFT, padx=15, pady=12)
b.bind("<Button-1>",click)

b= Button(f,text="+",font="lucida 17 bold",padx=15,pady=15)
b.pack(side=LEFT, padx=15, pady=12)
b.bind("<Button-1>",click)

b= Button(f,text="/",font="lucida 17 bold",padx=15,pady=15)
b.pack(side=LEFT, padx=15, pady=12)
b.bind("<Button-1>",click)

f.pack()

#2nd Frame
f = Frame(root,bg="grey",padx=5.5)

b= Button(f,text="6",font="lucida 17 bold",padx=15,pady=15)
b.pack(side=LEFT, padx=15, pady=12)
b.bind("<Button-1>",click)

b= Button(f,text="5",font="lucida 17 bold",padx=15,pady=15)
b.pack(side=LEFT, padx=15, pady=12)
b.bind("<Button-1>",click)

b= Button(f,text="4",font="lucida 17 bold",padx=15,pady=15)
b.pack(side=LEFT, padx=15, pady=12)
b.bind("<Button-1>",click)

b= Button(f,text="-",font="lucida 17 bold",padx=15,pady=15)
b.pack(side=LEFT, padx=15, pady=12)
b.bind("<Button-1>",click)

b= Button(f,text="%",font="lucida 17 bold",padx=15,pady=15)
b.pack(side=LEFT, padx=15, pady=12)
b.bind("<Button-1>",click)

f.pack()

# 3rd frame
f = Frame(root,bg="grey")

b= Button(f,text="3",font="lucida 17 bold",padx=15,pady=15)
b.pack(side=LEFT, padx=15, pady=12)
b.bind("<Button-1>",click)

b= Button(f,text="2",font="lucida 17 bold",padx=15,pady=15)
b.pack(side=LEFT, padx=15, pady=12)
b.bind("<Button-1>",click)

b= Button(f,text="1",font="lucida 17 bold",padx=15,pady=15)
b.pack(side=LEFT, padx=15, pady=12)
b.bind("<Button-1>",click)

b= Button(f,text="*",font="lucida 17 bold",padx=15,pady=15)
b.pack(side=LEFT, padx=15, pady=12)
b.bind("<Button-1>",click)

b= Button(f,text="00",font="lucida 17 bold",padx=15,pady=15)
b.pack(side=LEFT, padx=15, pady=12)
b.bind("<Button-1>",click)

f.pack()

# 4th frame
f = Frame(root,bg="grey")

b= Button(f,text="AC",font="lucida 17 bold",padx=17,pady=15)
b.pack(side=LEFT, padx=10, pady=12)
b.bind("<Button-1>",click)

b= Button(f,text="0",font="lucida 17 bold",padx=15,pady=15)
b.pack(side=LEFT, padx=15, pady=12)
b.bind("<Button-1>",click)

b= Button(f,text=".",font="lucida 17 bold",padx=15,pady=15)
b.pack(side=LEFT, padx=15, pady=12)
b.bind("<Button-1>",click)

b= Button(f,text="=",font="lucida 17 bold",padx=15,pady=15)
b.pack(side=LEFT, padx=15, pady=12)
b.bind("<Button-1>",click)


b= Button(f,text="Off",font="lucida 17 bold",padx=10,pady=15,command=exit)
b.pack(side=LEFT, padx=10, pady=12)


f.pack()



root.mainloop()

#Coded By - Karan Singh
