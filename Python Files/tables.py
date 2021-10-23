import calendar
import datetime
import sys
import sqlite3
import time


#imports correct version of tkinter based on python version
from tkinter import *
#w = Tk()

def database():
	global conn, cursor
	conn = sqlite3.connect("diary.db")
	cursor = conn.cursor()
	cursor.execute(
	"CREATE TABLE IF NOT EXISTS 'INVENTORY' (SNO INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,entry TEXT, date TEXT)")
	conn.commit()
	
class Calendar:
	#Instantiation
	def __init__(self, parent, values):
		self.values = values
		self.parent = parent
		self.cal = calendar.TextCalendar(calendar.SUNDAY)
		self.year = datetime.date.today().year
		self.month = datetime.date.today().month
		self.wid = []
		self.day_selected = 1
		self.month_selected = self.month
		self.year_selected = self.year
		self.day_name = ''
		
		self.setup(self.year, self.month)
		
	#Resets the buttons
	def clear(self):
		for w in self.wid[:]:
			w.grid_forget()
			# w.destroy()
			self.wid.remove(w)
			
	#Moves to previous month/year on calendar
	def go_prev(self):
		if self.month > 1:
			self.month -= 1
		else:
			self.month = 12
			self.year -= 1
		# self.selected = (self.month, self.year)
		self.clear()
		self.setup(self.year, self.month)
	
	# Moves to next month/year on calendar
	def go_next(self):
		if self.month < 12:
			self.month += 1
		else:
			self.month = 1
			self.year += 1
		
		# self.selected = (self.month, self.year)
		self.clear()
		self.setup(self.year, self.month)
	
	#Called on date button press
	def selection(self, day, name):
		self.day_selected = day
		self.month_selected = self.month
		self.year_selected = self.year
		self.day_name = name
		
		# Obtaining data
		self.values['day_selected'] = day
		self.values['month_selected'] = self.month
		self.values['year_selected'] = self.year
		self.values['day_name'] = name
		self.values['month_name'] = calendar.month_name[self.month_selected]
		
		self.clear()
		self.setup(self.year, self.month)
	
	def setup(self, y, m):
		#Tkinter creation
		left = Button(self.parent, text='<', fg="white", bg = "black", command=self.go_prev)
		self.wid.append(left)
		left.grid(row=0, column=1,pady =4,ipady = 4,ipadx=4, padx =4)
		
		header = Label(self.parent, height=2, fg="white", bg = "black", text='{}   {}'.format(calendar.month_abbr[m], str(y)))
		self.wid.append(header)
		header.grid(row=0, column=2, columnspan=3,pady =4,ipady = 4,ipadx=4, padx =4)
		
		right = Button(self.parent, text='>', fg="white", bg = "black", command=self.go_next)
		self.wid.append(right)
		right.grid(row=0, column=5,pady =4,ipady = 4,ipadx=4, padx =4)
		
		days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
		for num, name in enumerate(days):
			t = Label(self.parent, fg="white", bg = "black", text=name[:3])
			self.wid.append(t)
			t.grid(row=1, column=num,pady =4,ipady = 4,ipadx=4, padx =4)
		
		for w, week in enumerate(self.cal.monthdayscalendar(y, m), 2):
			for d, day in enumerate(week):
				if day:
					# print(calendar.day_name[day])
					b = Button(self.parent, width=1, text=day, fg = "white", bg= "black",
								  command=lambda day=day: self.selection(day, calendar.day_name[(day) % 7]))
					self.wid.append(b)
					b.grid(row=w, column=d,pady =4,ipady = 4,ipadx=4, padx =4)
		
		sel = Label(self.parent, fg="white", bg = "black", height=2, text='{} {} {} {}'.format(
			self.day_name, calendar.month_name[self.month_selected], self.day_selected, self.year_selected))
		self.wid.append(sel)
		sel.grid(row=8, column=0, columnspan=7,pady =4,ipady = 4,ipadx=4, padx =4)
		
		ok = Button(self.parent, fg="white", bg = "black", width=5, text='OK', command=self.save)
		self.wid.append(ok)
		ok.grid(row=9, column=2, columnspan=3, pady=10,ipadx = 4,ipady=4, padx =4)
	#Quit out of the calendar and terminate tkinter instance.
	def save(self):
		database()
		new = Toplevel()
		image1 = PhotoImage(file="pink.gif")
		panel1 = Label(new, image=image1)
		panel1.grid(row=0, column = 0)
		panel1.image = image1
		cursor.execute("SELECT * FROM 'INVENTORY'")
		conn.commit()
		y,m,d = self.month_selected, self.day_selected, self.year_selected
		d = [y,m,d,8,15,27,243860]
		date_str = ' '.join([str(elem) for elem in d])  
		date_time_obj = datetime.datetime.strptime(date_str, '%m %d %Y %H %M %S %f')
		date = date_time_obj.date()
		cursor.execute("SELECT entry FROM `INVENTORY` WHERE `date` LIKE ?", (date,))
		conn.commit()
		fetch = cursor.fetchall()
		for data in fetch:
				l1 = Label(panel1, text = data[0], font = ("Ink Free", 24))
				l1.grid(row=0, column=2, columnspan=3, pady=10,ipadx = 4,ipady=4, padx =4)
		cursor.close()
		conn.close()
		
		 
  

class Control:
	def __init__(self, parent):
		self.parent = parent
		self.choose_btn = Button(self.parent, text='Choose', command=self.popup)
		self.choose_btn.grid(row=0, column = 0)
		self.data = {}
	
	def popup(self):
		new = Toplevel()
		image1 = PhotoImage(file="pink.gif")
		panel1 = Label(new, image=image1)
		panel1.grid(row=0, column = 0)
		panel1.image = image1
		cal = Calendar(panel1, self.data)
	
		
            
