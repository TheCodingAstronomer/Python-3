from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("New Window")
root.iconbitmap('Other Files/download.ico')

def clicked():
	#Now, I can put anything in this new window just the root window
	top = Toplevel()
	top.title("Second Window")
	top.iconbitmap('Other Files/download.ico')
	global img
	img = ImageTk.PhotoImage(Image.open("Other Files/download.jfif"))
	lbl = Label(top, image=img).pack()
	bt2 = Button(top, text="Close Window", command=top.destroy).pack()



btn = Button(root, text="Click Me!", command=clicked).pack()



root.mainloop()