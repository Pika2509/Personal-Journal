from time import sleep, strftime
import tkinter 
from tkinter import *

root =Tk()

USER_FIRST_NAME = input("Enter your name")

calendar = {}

def welcome():
    print ("Welcome, " + USER_FIRST_NAME + "!!!!")
    print ("Calendar starting...")
    sleep(1)
    print ("Today is: " + strftime("%A %B %d, %Y"))
    print ("Current Time: " + strftime("%H: %M : %S"))
    print ("What would you like to do?")                                      
def start_calendar():
    welcome()
    start = True
    while start:
        user_choice = input("A to Add, U to Update, V to View, D to Delete, X to Exit: ")
        user_choice = user_choice.upper()
        if user_choice == 'V':
            if len(calendar.keys()) < 1:
                print ("Calendar empty.")
            else:
                print (calendar)
        elif user_choice == 'U':
            date = input("What date? ")
            update = input("Enter the update: ")
            calendar[date] = update
            print ("Success")
        elif user_choice == 'A':
            event = input("Enter event: ")
            date = input("Enter date (MM/DD/YYYY): ")
            if(len(date) > 10 or int(date[6:]) < int(strftime("%Y"))):
                print("Invalid")
                try_again = input("Try Again? Y for Yes, N for No: ")
                try_again = try_again.upper()
                if try_again == 'Y':
                    continue
                else:
                    start = False   
            else:
                calendar[date] = event
        if user_choice == 'D':
            if len(calendar.keys()) < 1:
                print ("Calendar is empty.")
            else: 
                event = input("What event? ")
                for date in calendar.keys():
                    if event == calendar[date]:
                        del calendar[date]
                        print ("The event has been deleted")
                    else:
                        print ("Incorrect name")
        if user_choice == 'X':
            start = False
        else:
            print ("Invalid command")
start_calendar()