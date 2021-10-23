import sqlite3
from tkinter import *
from tables import Calendar
from datetime import date
from datetime import datetime
Today = date.today()
m=Today.month
d=Today.day
def Quote_of_Day():

	try:
		sqliteConnection = sqlite3.connect('quotes.db')
		cursor = sqliteConnection.cursor()
		print("Connected to SQLite")
		q=Tk()
		if m == 1 and d == 26 :
			cursor.execute('select quote, author from quote_of_day where pins=1')
			records = cursor.fetchall()
			for row in records:
				l1 = Label(q, text = row[0], font = ("Ink Free", 30))
				l1.pack(pady = 20 , padx= 20)
				l2 = Label(q, text = row[1], font = ("Ink Free", 20))
				l2.pack(pady = 10 , padx= 10)
		else:
			cursor.execute('select quote, author from quote_of_day where pins=0 order by random() limit 1')
			records = cursor.fetchall()
			for row in records:
				l1 = Label(q, text = row[0], font = ("Ink Free", 30))
				l1.pack(pady = 20 , padx= 20)
				l2 = Label(q, text = row[1], font = ("Ink Free", 20))
				l2.pack(pady = 10 , padx= 10)
		sqliteConnection.close()

	except sqlite3.Error as error:
		print("Failed to read data from sqlite table", error)
	finally:
		if (sqliteConnection):
			sqliteConnection.close()
			print("The SQLite connection is closed")

