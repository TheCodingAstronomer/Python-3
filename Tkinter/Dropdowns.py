from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("Drop Downs")
root.iconbitmap('download.ico')
root.geometry("400x400")

# Drop Down Boxes

clicked = StringVar()

options = [
	"Monday", 
	"Tuesday", 
	"Wednesday", 
	"Thursday", 
	"Friday", 
	"Saturday", 
	"Sunday"
]

clicked.set(options[0])

def clickeda():
	lbl = Label(root, text=clicked.get()).pack()


drop = OptionMenu(root, clicked, *options)
drop.pack()


btn = Button(root, text="Show Selection", command=clickeda).pack()


root.mainloop()