from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("Images")
root.iconbitmap('C:/Users/nihal/OneDrive/Desktop/download.ico')


img1 = ImageTk.PhotoImage(Image.open("Other Files/download.jfif"))
img2 = ImageTk.PhotoImage(Image.open("Other Files/download1.jfif"))
img3 = ImageTk.PhotoImage(Image.open("Other Files/download2.jfif"))
img4 = ImageTk.PhotoImage(Image.open("Other Files/download3.jfif"))
img5 = ImageTk.PhotoImage(Image.open("Other Files/download4.jfif"))
img6 = ImageTk.PhotoImage(Image.open("Other Files/download5.jfif"))
img6 = ImageTk.PhotoImage(Image.open("Other Files/download6.jfif"))
img7 = ImageTk.PhotoImage(Image.open("Other Files/images.jfif"))
img8 = ImageTk.PhotoImage(Image.open("Other Files/images2.jfif"))


imglist = [img1, img2, img3, img4, img5, img6, img7, img8]


myLabel = Label(image=imglist[0])
myLabel.grid(row=0,column=0,columnspan=3)

def forward(imgnum):
	global myLabel
	global buttonBack
	global buttonFron
	myLabel.grid_forget()
	myLabel = Label(image=imglist[imgnum-1])
	buttonFron = Button(root, text=">>", command=lambda: forward(imgnum+1))
	buttonBack = Button(root, text="<<", command=lambda: back(imgnum-1))

	if imgnum == 5:
		buttonFron = Button(root, text=">>", state=DISABLED)	

	myLabel.grid(row=0,column=0,columnspan=3)
	buttonBack.grid(row=1,column=0)
	buttonFron.grid(row=1,column=2)
	

def back(imgnum1):
	global myLabel
	global buttonBack
	global buttonFron
	
	myLabel.grid_forget()

	myLabel = Label(image=imglist[imgnum1-1])
	buttonFron = Button(root, text=">>", command=lambda: forward(imgnum1+1))
	buttonBack = Button(root, text="<<", command=lambda: back(imgnum1-1))

	if imgnum1 == 0:
		buttonBack = Button(root, text="<<", state=DISABLED)

	myLabel.grid(row=0,column=0,columnspan=3)
	buttonBack.grid(row=1,column=0)
	buttonFron.grid(row=1,column=2)


buttonBack = Button(root, text="<<", command=lambda: back(1))
quit = Button(root, text="Exit Program", command=root.quit)
buttonFron = Button(root, text=">>", command=lambda: forward(1))


quit.grid(row=1,column=1)
buttonBack.grid(row=1,column=0)
buttonFron.grid(row=1,column=2)


root.mainloop()