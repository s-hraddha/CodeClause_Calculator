print("hello world! ")
from tkinter import *

def click(event):
    global stvalue
    text = event.widget.cget("text")
    print(text)
    if text == "=":
        if stvalue.get().isdigit():
            value = int(stvalue.get())
        else:
            value=eval(screen.get())

        stvalue.set(value)
        screen.update()
           
    elif text == "C":
        stvalue.set("")
        screen.update()
    else:
        stvalue.set(stvalue.get()+text)
        screen.update()

# create an instance of tkinter frame
root= Tk()

# set the geometry of frame
root.geometry("450x710")

# set the title
root.title("calculator")

stvalue = StringVar()
stvalue.set("")
screen = Entry(root, textvar=stvalue, font="lucida 50 bold",width=70,background="black",foreground="white")
screen.pack(fill =X, padx=19, pady=5)

frame1 = Frame(root, bg="grey") 
button = Button(frame1, text="C",padx=8, pady=8, font="lucida 35 bold",foreground="orange", background="black")
button.pack(side=LEFT, padx=8, pady=8)
button.bind("<Button-1>",click)

button = Button(frame1, text="^",padx=8, pady=8, font="lucida 35 bold",foreground="orange", background="black")
button.pack(side=LEFT, padx=10, pady=8)
button.bind("<Button-1>",click)

button = Button(frame1, text="%",padx=8, pady=8, font="lucida 35 bold",foreground="orange", background="black")
button.pack(side=LEFT, padx=2, pady=2)
button.bind("<Button-1>",click)

button = Button(frame1, text="/",padx=8, pady=8, font="lucida 35 bold",foreground="orange", background="black")
button.pack(side=LEFT, padx=10, pady=8)
button.bind("<Button-1>",click)
frame1.pack()

frame1 = Frame(root, bg="grey") 
button = Button(frame1, text="7",padx=8, pady=8, font="lucida 35 bold",foreground="white", background="black")
button.pack(side=LEFT, padx=10, pady=8)
button.bind("<Button-1>",click)

button = Button(frame1, text="8",padx=8, pady=8, font="lucida 35 bold",foreground="white", background="black")
button.pack(side=LEFT, padx=10, pady=8)
button.bind("<Button-1>",click)

button = Button(frame1, text="9",padx=8, pady=8, font="lucida 35 bold",foreground="white", background="black")
button.pack(side=LEFT, padx=10, pady=8)
button.bind("<Button-1>",click)

button = Button(frame1, text="*",padx=8, pady=8, font="lucida 35 bold",foreground="orange", background="black")
button.pack(side=LEFT, padx=10, pady=8)
button.bind("<Button-1>",click)

frame1.pack()

frame1 = Frame(root, bg="grey") 
button = Button(frame1, text="4",padx=8, pady=8, font="lucida 35 bold",foreground="white", background="black")
button.pack(side=LEFT, padx=10, pady=10)
button.bind("<Button-1>",click)

button = Button(frame1, text="5",padx=8, pady=8, font="lucida 35 bold",foreground="white", background="black")
button.pack(side=LEFT, padx=10, pady=8)
button.bind("<Button-1>",click)

button = Button(frame1, text="6",padx=8, pady=8, font="lucida 35 bold",foreground="white", background="black")
button.pack(side=LEFT, padx=10, pady=8)
button.bind("<Button-1>",click)

button = Button(frame1, text="-",padx=8.5, pady=8.5, font="lucida 35 bold",foreground="orange", background="black")
button.pack(side=LEFT, padx=10, pady=8)
button.bind("<Button-1>",click)
frame1.pack()

frame1 = Frame(root, bg="grey") 
button = Button(frame1, text="1",padx=8, pady=8,font="lucida 35 bold",foreground="white", background="black")
button.pack(side=LEFT, padx=10, pady=8)
button.bind("<Button-1>",click)

button = Button(frame1, text="2",padx=8, pady=8,font="lucida 35 bold",foreground="white", background="black")
button.pack(side=LEFT, padx=10, pady=8)
button.bind("<Button-1>",click)

button = Button(frame1, text="3",padx=8, pady=8, font="lucida 35 bold",foreground="white", background="black")
button.pack(side=LEFT, padx=10, pady=8)
button.bind("<Button-1>",click)

button = Button(frame1, text="+",padx=7, pady=7.5,font="lucida 35 bold",foreground="orange", background="black")
button.pack(side=LEFT, padx=7, pady=7)
button.bind("<Button-1>",click)
frame1.pack()

frame1 = Frame(root, bg="grey") 
button = Button(frame1, text="0",padx=8, pady=8, font="lucida 35 bold",foreground="white", background="black")
button.pack(side=LEFT, padx=10, pady=8)
button.bind("<Button-1>",click)

button = Button(frame1, text=".",padx=8, pady=8, font="lucida 35 bold",foreground="white", background="black")
button.pack(side=LEFT, padx=11, pady=8)
button.bind("<Button-1>",click)

button = Button(frame1, text="=", padx=62, pady=15, font="lucida 35 bold",foreground="orange", background="black")
button.pack(side=LEFT, padx=10, pady=8)
button.bind("<Button-1>",click)
frame1.pack()

root.mainloop()