from tkinter import *
from PIL import ImageTk,Image


root = Tk()
root.title("Sliders")
root.iconbitmap('Other Files/download.ico')


vertical = Scale(root, from_=0, to=2000)
vertical.pack()

horizontal = Scale(root, from_=0, to=2000, orient=HORIZONTAL)
horizontal.pack()

def click():
	root.geometry(str(horizontal.get()) + "x" + str(vertical.get()))
	lbl = Label(root, text=horizontal.get())
	lbl.pack()
	lbl1 = Label(root, text=vertical.get())
	lbl1.pack()

btn = Button(root, text="Resize!!", command=click).pack()



root.mainloop()

