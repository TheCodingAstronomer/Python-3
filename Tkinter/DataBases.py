from tkinter import *
from PIL import ImageTk,Image
import sqlite3

root = Tk()
root.title("DataBases")
root.iconbitmap('download.ico')
root.geometry("400x400")

# DataBases

# Create database or connect to one
conn = sqlite3.connect('TheGreatDataBase.db')

# Create A Cursor
c = conn.cursor()

# Create Table
'''
c.execute("""CREATE TABLE addresses(
	fn text,
	ln text,
	address text,
	city text,
	state text,
	zip_code integer
)


	""")
'''
# Create Functions To Update Record

def update():
	# Create database or connect to one
	conn = sqlite3.connect('TheGreatDataBase.db')

	# Create A Cursor
	c = conn.cursor()

	c.execute("""UPDATE addresses SET
		first_name = :first,
		last_name = :last,
		address = :address,
		city = :city,
		state = :state,
		zipc = :zipc

		WHERE oid = :oid""",
		{
		'first': f_name_hoot.get(),
		'last': l_name_hoot.get(),
		'address': address_hoot.get(),
		'city': city_hoot.get(),
		'state': state_hoot.get(),
		'zipc': zipc_hoot.get(),
		'oid': recordid
		})

	# Commit Changes
	conn.commit()

	# Close Connection
	conn.close()

	# Clear Text Boxes
	f_name_hoot.delete(0, END)
	l_name_hoot.delete(0, END)
	address_hoot.delete(0, END)
	city_hoot.delete(0, END)
	state_hoot.delete(0, END)
	zipc_hoot.delete(0, END)

def edit():
	hoot = Tk()
	hoot.title("Update")
	hoot.iconbitmap('download.ico')
	hoot.geometry("400x400")

	# Create database or connect to one
	conn = sqlite3.connect('TheGreatDataBase.db')

	# Create A Cursor
	c = conn.cursor()

	global recordid
	recordid = delbox.get()

	# Query The Database
	c.execute("SELECT * FROM addresses WHERE oid=" + recordid)
	records = c.fetchall()
	
	# Create Global variables 
	global f_name_hoot
	global l_name_hoot
	global address_hoot
	global city_hoot
	global state_hoot
	global zipc_hoot

	# Create Text Boxes
	f_name_hoot = Entry(hoot, width=50)
	f_name_hoot.grid(row=0, column=1, padx=20, pady=(10,0))
	l_name_hoot = Entry(hoot, width=50)
	l_name_hoot.grid(row=1, column=1)
	address_hoot = Entry(hoot, width=50)
	address_hoot.grid(row=2, column=1)
	city_hoot = Entry(hoot, width=50)
	city_hoot.grid(row=3, column=1)
	state_hoot = Entry(hoot, width=50)
	state_hoot.grid(row=4, column=1)
	zipc_hoot = Entry(hoot, width=50)
	zipc_hoot.grid(row=5, column=1)
	delbox_hoot = Entry(hoot, width=30)
	delbox_hoot.grid(row=6, column=1)

	#Loop Thru Results
	for record in records:
		f_name_hoot.insert(0, record[0])
		l_name_hoot.insert(0, record[1])
		address_hoot.insert(0, record[2])
		city_hoot.insert(0, record[3])
		state_hoot.insert(0, record[4])
		zipc_hoot.insert(0, record[5])

	# Create Text Box Labels
	fi_hoot = Label(hoot, text="Enter First Name:")
	fi_hoot.grid(row=0, column=0)
	ln_hoot = Label(hoot, text="Enter Last Name:")
	ln_hoot.grid(row=1, column=0)
	addres_hoot = Label(hoot, text="Enter Address:")
	addres_hoot.grid(row=2, column=0)
	ci_hoot = Label(hoot, text="Enter City Name:")
	ci_hoot.grid(row=3, column=0)
	st_hoot = Label(hoot, text="Enter State Name:")
	st_hoot.grid(row=4, column=0)
	zpc_hoot = Label(hoot, text="Enter Zip Code:")
	zpc_hoot.grid(row=5, column=0)
	dellabel_hoot = Label(hoot, text="Select Record")
	dellabel_hoot.grid(row=6,column=0)

	# Create An Update Button
	editbtn_hoot = Button(hoot, text="Update Record", command=update)
	editbtn_hoot.grid(row=8, column=0, columnspan=2, ipadx=100)

	# Commit Changes
	conn.commit()

	# Close Connection
	conn.close()


# Create Function To Delete Record
def deleter():
	# Create database or connect to one
	conn = sqlite3.connect('TheGreatDataBase.db')

	# Create A Cursor
	c = conn.cursor()

	c.execute("DELETE from addresses WHERE oid=" + str(delbox.get()))

	# Commit Changes
	conn.commit()

	# Close Connection
	conn.close()

def btn_clicked():
	# Clear Text Boxes
	f_name.delete(0, END)
	l_name.delete(0, END)
	address.delete(0, END)
	city.delete(0, END)
	state.delete(0, END)
	zipc.delete(0, END)

	# Create database or connect to one
	conn = sqlite3.connect('TheGreatDataBase.db')

	# Create A Cursor
	c = conn.cursor()

	# Insert Into Table
	c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zipc)", 
		{
			'f_name':f_name.get(),
			'l_name':l_name.get(),
			'address':address.get(),
			'city':city.get(),
			'state':state.get(),
			'zipc':zipc.get()
		})
	# Commit Changes
	conn.commit()

	# Close Connection
	conn.close()

# Create Query Function
def query():
	# Create database or connect to one
	conn = sqlite3.connect('TheGreatDataBase.db')

	# Create A Cursor
	c = conn.cursor()

	# Query The Database
	c.execute("SELECT *, oid FROM addresses")
	records = c.fetchall()
	print(records)

	#Loop Thru Results
	print_records = ''
	for record in records:
		print_records += str(record) + "\n"

	queryl = Label(root, text=print_records)
	queryl.grid(row=12,column=0, columnspan=2)


	# Commit Changes
	conn.commit()

	# Close Connection
	conn.close()


# Create Text Boxes
f_name = Entry(root, width=50)
f_name.grid(row=0, column=1, padx=20)
l_name = Entry(root, width=50)
l_name.grid(row=1, column=1)
address = Entry(root, width=50)
address.grid(row=2, column=1)
city = Entry(root, width=50)
city.grid(row=3, column=1)
state = Entry(root, width=50)
state.grid(row=4, column=1)
zipc = Entry(root, width=50)
zipc.grid(row=5, column=1)
delbox = Entry(root, width=30)
delbox.grid(row=9, column=0, columnspan=2)

# Create Text Box Labels
fi = Label(root, text="Enter First Name:")
fi.grid(row=0, column=0)
ln = Label(root, text="Enter Last Name:")
ln.grid(row=1, column=0)
addres = Label(root, text="Enter Address:")
addres.grid(row=2, column=0)
ci = Label(root, text="Enter City Name:")
ci.grid(row=3, column=0)
st = Label(root, text="Enter State Name:")
st.grid(row=4, column=0)
zpc = Label(root, text="Enter Zip Code:")
zpc.grid(row=5, column=0)
dellabel = Label(root, text="Select Record")
dellabel.grid(row=9,column=0)

# Create Submit Button
btn = Button(root, text="Submit", command=btn_clicked)
btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# Create A Query Button
query_btn = Button(root, text="See Record", command=query)
query_btn.grid(row=7, column=0, columnspan=2, ipadx=100)

# Create A Delete Button
dbtn = Button(root, text="Delete Record", command=deleter)
dbtn.grid(row=10, column=0, columnspan=2, ipadx=100)

# Create An Update Button
editbtn = Button(root, text="Update Record", command=edit)
editbtn.grid(row=11, column=0, columnspan=2, ipadx=100)

# Commit Changes
conn.commit()

# Close Connection
conn.close()


root.mainloop()