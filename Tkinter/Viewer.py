from tkinter import *
from PIL import ImageTk,Image
import sqlite3
import pandas as pd

root = Tk()
root.title("DataBases")
root.iconbitmap('download.ico')
root.geometry("400x400")


info = {'': ['Honda Civic','Toyota Corolla','Ford Focus','Audi A4'],
        'Price': [32000,35000,37000,45000]
        }


root.mainloop()