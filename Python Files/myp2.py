from tkinter import *
import calendar

text = calendar.calendar(2020)

root=Tk()
root.geometry("700x600")
root.title('CALENDAR')
label1=Label(root,text="CALENDAR",bg="dark gray",font=("times",28,'bold'))
label1.grid(row=1,column=1)
root.config(background="white")
label2=Label(root,text=text,font="Consolas 10 bold")
label2.grid(row=2,column=1,padx=70)
root.mainloop()