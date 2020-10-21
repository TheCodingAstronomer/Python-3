from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("Status")
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

total_img = str(len(imglist))

status = Label(root,text="Image 1 of " + total_img,bd=1,relief=SUNKEN,anchor=E)


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
	buttonFron.grid(row=1,column=2,pady=10)

	#Update Status Num
	strimgnum = str(imgnum)
	status = Label(root,text="Image " + strimgnum +" of " + total_img,bd=1,relief=SUNKEN,anchor=E)
	status.grid(row=2,column=0,columnspan=3,sticky=W+E)
	

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

	#Update Status Num
	strimgnum1 = str(imgnum1)
	status = Label(root,text="Image " + strimgnum1 +" of " + total_img,bd=1,relief=SUNKEN,anchor=E)
	status.grid(row=2,column=0,columnspan=3,sticky=W+E)


buttonBack = Button(root, text="<<", command=lambda: back(0))
quit = Button(root, text="Exit Program", command=root.quit)
buttonFron = Button(root, text=">>", command=lambda: forward(0))


quit.grid(row=1,column=1)
buttonBack.grid(row=1,column=0)
buttonFron.grid(row=1,column=2)
status.grid(row=2,column=0,columnspan=3,sticky=W+E)


root.mainloop()