from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("Radio")
root.iconbitmap('Other Files/download.ico')

#r = IntVar()
#r.set("2")

TOPPINGS = [
	("Pepporoni", "Pepporoni"),
	("Onion", "Onion"),
	("Cheese", "Cheese"),
	("Mushroom", "Mushroom")
]

pizza = StringVar()
pizza.set("Pepporoni")

for topingname, toppings in TOPPINGS:
	Radiobutton(root, text=topingname, variable=pizza, value=toppings).pack(anchor=W)

def clicker(value):
	label = Label(root, text=value)
	label.pack()

#Radiobutton(root, text="Option 1", variable=r, value=1, command=lambda: clicker(r.get())).pack()
#Radiobutton(root, text="Option 2", variable=r, value=2, command=lambda: clicker(r.get())).pack()


#label = Label(root, text=pizza.get())
#label.pack()

myButton = Button(root, text="Click Me!", command=lambda: clicker(pizza.get())).pack()
button2 = Button(root, text="Exit", command=root.quit).pack()



root.mainloop()