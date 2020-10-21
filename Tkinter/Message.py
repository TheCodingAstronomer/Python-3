from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox

root = Tk()
root.title("Message")
root.iconbitmap('Other Files/download.ico')

# showinfo showwarning showerror askquestion askyesno askokcancel

def popup():
	response = messagebox.askyesno("This is my Popup!", "Hello World!")
	#if response == 1:
		#Label(root, text="You Clicked Yes!").pack()
	#else:
		#Label(root, text="You Clicked No!").pack()


Button(root, text="Popup", command=popup).pack()


root.mainloop()