from tkinter import *  
from tkinter.messagebox import showinfo
import sqlite3
import time
from datetime import datetime
from calendar import *
from tables import *
from quotes import *

w=Tk()
w.state("zoomed")
def logged():
	s = str(datetime.datetime.now())
	tm.showinfo("Log", "Entry created successfully at "+s)

def database():
	global conn, cursor
	conn = sqlite3.connect("diary.db")
	cursor = conn.cursor()
	cursor.execute(
	"CREATE TABLE IF NOT EXISTS 'INVENTORY' (SNO INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, entry TEXT, date TEXT)")
	conn.commit()
	
	
def database_add(entry) :
	database()
	global conn, cursor	
	unix = int(time.time())
	date = str(datetime.fromtimestamp(unix).strftime('%Y-%m-%d'))
	cursor.execute("INSERT INTO 'INVENTORY'(entry, date) VALUES (?, ?)",(entry, date))
	conn.commit()
	print("Entry Added To Database")
	showinfo( title = "Entry Add", message = "Data inserted To table")
	cursor.close()
	conn.close()
	
def create_widgets(Frame):
	time = datetime.now()
	Y = time.year
	M = time.month
	days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
	#create labels
	for i in range(7):
		label = Label(Frame, text=days[i])
		label.grid(row = 0, column = i,pady =4 , padx =4)

		weekday, numDays = monthrange(Y,M)
		week = 1
		for i in range(1, numDays + 1):
			button = Button(Frame, text = str(i))
			button.grid(row = week, column = weekday,pady = 4,padx = 4)
			weekday += 1
			if weekday > 6:
				week += 1
				weekday = 0	

def addentry():
	
	
	new = Toplevel()
	new.geometry('800x500')
	image1 = PhotoImage(file="cute.gif")
	panel1 = Label(new, image=image1)
	panel1.pack(side='top', fill='both', expand='yes')
	panel1.image = image1
	l1 = Label(panel1,text = "Add to your day ..",fg = "black",justify = LEFT,font = ("Ink Free", 40))
	l1.pack(pady = 20)
	entryvar = StringVar()
	entry = Entry(panel1, textvariable=entryvar, width = 100)
	entry.pack(ipady=120,pady=20)	
	bsave = Button(panel1, text="Add Entry", command=lambda: database_add(entryvar.get()))
	bsave.pack(pady = 10)	
	new.resizable(0, 0)
	new.mainloop()
	
		
	
def viewentry():
	new = Toplevel()
	new.geometry('250x250')
	image1 = PhotoImage(file="pink.gif")
	panel1 = Label(new, image=image1)
	panel1.grid(row=0, column = 0)
	panel1.image = image1
	#create_widgets(panel1)		
	app = Control(panel1)  
	new.mainloop()
		
image1 = PhotoImage(file="clouds.gif")
w.geometry('1300x720')
panel1 = Label(w, image=image1)
panel1.pack(side='top', fill='both', expand='yes')
panel1.image = image1
	
l1 = Label(panel1,text = "WELCOME ",bg = "black",fg = "white",bd = 10, relief = RAISED ,font = ("bebas", 70))
l1.pack(pady = 20)
		
l2 = Label(panel1,text = "What would you like to do ????",bg = "cyan",fg = "black",font = ("Comic Sans MS", 26))
l2.pack(pady = 30)
	
b3 = Button(panel1,text = "Add to your day ..",bg = "#E5A2FB",fg = "black",justify = LEFT,font = ("Ink Free", 20) , command = addentry)
b3.pack(pady = 5)	
		
b4 = Button(panel1,text = "View your logs ..",bg = "#E5A2FB",fg = "black",justify = LEFT,font = ("Ink Free", 20) , command = viewentry)
b4.pack(pady = 5)
		
b5 = Button(panel1,text = "Quote of the day ..",bg = "#E5A2FB",fg = "black",justify = LEFT,font = ("Ink Free", 20) , command = Quote_of_Day)
b5.pack(pady = 5)
		
b6 = Button(panel1,text = "How's the mood ..",bg = "#E5A2FB",fg = "black",justify = LEFT,font = ("Ink Free", 20) , command = addentry)
b6.pack(pady = 5)	
w.wm_title("MY DIARY")
w.mainloop()


 