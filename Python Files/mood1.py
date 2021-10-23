import sqlite3
from tkinter import *
import time
from datetime import datetime
from calendar import *
mood = Tk()
mood.geometry("500x400")

def insertMood(pin):
	sqliteConnection = sqlite3.connect('mood.db')
	cursor = sqliteConnection.cursor()
	print("Connected to SQLite")
	unix = int(time.time())
	date = str(datetime.fromtimestamp(unix).strftime('%Y-%m-%d'))
	cursor.execute("INSERT INTO 'mood_of_day'(date, pin) VALUES (?, ?)",(date, pin))
	sqliteConnection.commit()
	print("data inserted successfully as a Mood into a table")
	cursor.close()
	sqliteConnection.close()
	
ask = Label(mood, text = "What is your mood today????", font = ("Ink Free", 30)).place(x=0,y=150)
photo = PhotoImage(file = "happy.png")
photoimage = photo.subsample(1, 1) 
photo1 = PhotoImage(file = "good.gif") 
photoimage1 = photo1.subsample(1, 1)
photo2 = PhotoImage(file = "sad.gif")
photoimage2 = photo2.subsample(1, 1)
photo3 = PhotoImage(file = "angry.gif") 
photoimage3 = photo3.subsample(1, 1)

happy = Button(mood, text = "Happy!", image = photoimage, command = lambda: insertMood(0)).grid(column=1, row=6, ipadx=10, ipady=10, sticky="NSEW")
fine = Button(mood, text = "fine!", image = photoimage1, command = lambda: insertMood(1)).grid(column=2, row=6, ipadx=10, ipady=10, sticky="NSEW")
sad = Button(mood, text = "sad!", image = photoimage2, command = lambda: insertMood(2)).grid(column=3, row=6, ipadx=10, ipady=10, sticky="NSEW")
angry = Button(mood, text = "angry!", image = photoimage3, command =lambda: insertMood(3)).grid(column=4, row=6, ipadx=10, ipady=10, sticky="NSEW")

mood.mainloop()