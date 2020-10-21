from tkinter import *

root = Tk()
root.title = ("Complaint Form")
root.iconbitmap('download.ico')

label1 = Label(root, text = "Enter Name:")
name = Entry(root, width = 50)
label2 = Label(root, text = "Enter Address:")
address = Entry(root, width = 50)
label3 = Label(root, text = "Enter Complaint:")
comm = Entry(root, width = 50)
Quit = Button(root, text = "Submit", command = lambda: file_apend() )

label1.grid(row = 0, column = 0)
name.grid(row = 1, column = 0, padx = 70, pady = 70)
label2.grid(row = 2, column = 0)
address.grid(row = 3, column = 0, padx = 70, pady = 70)
label3.grid(row = 4, column = 0)
comm.grid(row = 5, column = 0, padx = 70, pady = 70)
Quit.grid(row = 6, column = 0)

def file_apend():
    name1 = name.get()
    address1 = address.get()
    comm1 = comm.get()
    person = "Name: " + name1 + " " + "Address: " + address1 + " " + "Complaint: " + comm1

    Dem = open("PROJECT Demo.txt", 'a+')
    Dem.write(person)
    Dem.write("\n")
    Dem.close()
    label = Label(root, text = "Information Saved!")
    label.grid(row = 7, column = 0)


root.mainloop()
