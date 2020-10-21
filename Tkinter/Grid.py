from tkinter import *

root = Tk()

#Creating a label widget
myLabel1 = Label(root, text = "Hello World!")
myLabel2 = Label(root, text = "My Name Is G Nihal")
myLabel3 = Label(root, text = "                                                    ")
#Grid system
myLabel1.grid(row = 0, column = 0)
myLabel2.grid(row = 1, column = 5)
myLabel3.grid(row = 1, column = 3)

root.mainloop()
