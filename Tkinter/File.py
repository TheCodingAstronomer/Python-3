from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog

root = Tk()
root.title("File")
root.iconbitmap('Other Files/download.ico')

def click():
	global img1
	root.filename = filedialog.askopenfilename(initialdir="C:/Users/nihal/Desktop/Wallpaper", title="Select A File", filetypes=(("JPG Files", "*.jpg"),))
	lbl = Label(root, text=root.filename).pack()
	img1 = ImageTk.PhotoImage(Image.open(root.filename))
	lbl = Label(root, image=img1).pack()

btn = Button(root, text="Open File", command=click).pack()

root.mainloop()