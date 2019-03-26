from tkinter import *
from tkinter import messagebox


import tkinter.font as tkFont

root = Tk()
tkFont.Font(family="Times", size=10, weight=tkFont.BOLD)
tkFont.Font(family="Helvetica", size=10, weight=tkFont.BOLD,
            slant=tkFont.ITALIC)
tkFont.Font(family="Symbol", size=8)
w = Label(root, text="Hello, world!")
w.pack()

def callback(event):
    print ("clicked at", event.x, event.y)

frame = Frame(root, width=100, height=100)
frame.bind("<Button-1>", callback)
frame.pack()

class App:

    def __init__(self, master):

        frame = Frame(master)
        frame.pack()

        self.button = Button(
            frame, text="QUIT", fg="red", command=frame.quit
            )
        self.button.pack(side=LEFT)

        self.hi_there = Button(frame, text="Hello", command=self.say_hi)
        self.hi_there.pack(side=LEFT)

    def say_hi(self):
        print ("hi there, everyone!")



app = App(root)

def key(event):
    print ("pressed", repr(event.char))

def callback(event):
    frame.focus_set()
    print ("clicked at", event.x, event.y)

frame = Frame(root, width=100, height=100)
frame.bind("<Key>", key)
frame.bind("<Button-1>", callback)
frame.pack()

def callback():
    if messagebox.askokcancel("Quit", "Do you really wish to quit?"):
        root.destroy()


root.protocol("WM_DELETE_WINDOW", callback)

root.mainloop()