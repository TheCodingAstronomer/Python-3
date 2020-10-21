from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("CheckBoxes")
root.iconbitmap('Other Files/download.ico')
root.geometry("400x400")



var = StringVar()

c = Checkbutton(root, text="Check this box, I dare you!", variable=var, onvalue="On", offvalue="Off")
c.deselect()
c.pack()

def click():
	lbl = Label(root, text=var.get()).pack()


btn = Button(root, text="Click Me!", command=click).pack()


root.mainloop()

