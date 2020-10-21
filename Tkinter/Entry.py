from tkinter import *

root = Tk()
root.title("Entry")

e = Entry(root)
e.pack()

def myClick():
	hello = "Hello " + e.get()
	myLabel = Label(root, text = name)
	myLabel.pack()

myButton = Button(root, text = "Enter your name", command = myClick)
myButton.pack()

root.mainloop()
