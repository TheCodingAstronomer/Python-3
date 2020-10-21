from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("Frame")
root.iconbitmap('Other Files/download.ico')

#                                         Changes space inside frame
frame = LabelFrame(root,text="My Frame....",padx=5,pady=5)
#Changes space outside frame
frame.pack(padx=10,pady=10)

b = Button(frame,text="Don't Click Here!")
#Can do grid inside a frame
b.pack( )


root.mainloop()