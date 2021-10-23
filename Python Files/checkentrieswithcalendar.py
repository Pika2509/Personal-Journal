from tkinter import *

import datetime

import calendar



class CalendarGrid():

    ''' Class dealing with calendar grid GUI '''

    

    def __init__(self, root, originX, originY):

        self.root = root

        self.gridBoxes = [0 for i in range(42)] #Generate refernce to grid blocks

        for i in range(42):

            self.gridBoxes[i] = Label(root, bg = 'white', width = 16, anchor = 'nw', height = 5, justify = 'left')

        

        # Set day titles on grid

        for i in range(7):

            self.gridBoxes[i].config(text = Weekdays[i], fg = 'yellow', bg = 'dodgerblue', font = 'Consolas 37 bold', width = 4, height = 1, pady = 8, padx = 4)

        

        self.render(originX, originY)

        self.putValues(currMonth, currYear)

        

    def render(self, originX, originY):

        for i in range(6):

            for j in range(7):

                self.gridBoxes[7 * i + j].place(x = 118 * j + originX, y = 82 * i + originY) 



    def putValues(self, month, year, direction = 'reverse'):

        #places calendar values for current month,year on calendar

        global weekDayOnFirst

        

        if(currMonth == 2 and currYear % 4 == 0):

            leapYearAdjustment = 1

        else:

            leapYearAdjustment = 0



        if(weekDayOnFirst == -101):

                weekdayShift = currDatetime.day % 7

                weekDayOnFirst = currDatetime.weekday() - weekdayShift

        elif(direction == 'reverse'):

                weekDayOnFirst = weekDayOnFirst - monthlyShift[currMonth - 1] - leapYearAdjustment

        elif(direction == 'forward'):

                weekDayOnFirst = weekDayOnFirst + monthlyShift[currMonth - 2] + leapYearAdjustment



        weekDayOnFirst = (weekDayOnFirst + 7) % 7

        numberOfDays = monthlyShift[currMonth - 1] + 28 + leapYearAdjustment

        eventLoader = EventLoader(currYear, currMonth)



        for day in range(1, numberOfDays + 1):

            #places dates and respective events

                indexOfBox = ((day + weekDayOnFirst) % 35) + 7

                eventString = eventLoader.load(day)

                if eventString != '':

                    self.gridBoxes[indexOfBox].config(fg='green3', text = str(day) + '\n' + eventString)

                elif indexOfBox in [13, 20, 27, 34, 41]: # List of Sunday Boxes

                    self.gridBoxes[indexOfBox].config(text = str(day), fg='red2') # Changes all Sunday dates to red

                else:

                    self.gridBoxes[indexOfBox].config(text = str(day))

                

    def clearValues(self):

        # Clear the grid for new values

        for i in range(7, 42):

                self.gridBoxes[i].config(text = '', fg = 'black')

    

    def forget(self):

	# Forgets all boxes so that they can be re-rendered

        for i in self.gridBoxes:

            i.place_forget()





class EventLoader():

     'Class dealing with loading events from file '

    def __init__(self,year,month):

        self.year = year

        self.month = calendar.month_abbr[month].upper()

        self.monthlyEventStr = ''

        self.eventDateList = dict()

        self.monthLoad()

        

    def monthLoad(self):

        eventFile = open('cal.dat', 'rb')

        line = 'initialized'

        while line != '':

            line = eventFile.readline(4)

            if(line == str(self.year)):

                while line != '':

                    line = eventFile.readline()

                    if(line[:3] == self.month):

                        self.monthlyEventStr = line[4:]

                        self.indexEvents()

                        break

                break

        eventFile.close()

        return None



    def indexEvents(self):

        monthlyEventList = self.monthlyEventStr.split(';')

        for event in monthlyEventList:

            self.eventDateList[int(event[:2])] = event[3:]

        

    def load(self, day):

        if self.eventDateList.has_key(day):

            events = self.eventDateList[day]

            events = events.split(',')

            return '\n'.join(events)

        else:

            return ''



class transparentWidget():

    ' Implementation of Transparent widget '

    def __init__(self, canvas, x, y, text, color1, color2, textcolor, command = None):

        self.canvas = canvas

        self.text = text

        self.color1 = color1

        self.color2 = color2

        self.txtColor = textcolor

        self.command = command

        self.create(x, y)



    def create(self, x, y): 

    # Renders attributes into graphics and bind animations

        self.BgLayer = self.canvas.create_oval(x, y, x+60, y+60, fill = self.color1, width = 0.0, activefill = self.color2)

        self.textLayer = self.canvas.create_text( x+30, y+28, text = self.text, font = 'consolas 30 bold', fill = self.txtColor)

        self.canvas.tag_bind(self.textLayer, '<Enter>', self.hover)

        self.canvas.tag_bind(self.textLayer, '<Leave>', self.unhover)

        self.canvas.tag_bind(self.textLayer, '<Button-1>', self.action)

        self.canvas.tag_bind(self.textLayer, '<ButtonRelease-1>', self.postAction)



    def place(self,x,y):

        self.canvas.coords(self.BgLayer, x, y, x+60, y+60)

        self.canvas.coords(self.textLayer, x+30, y+28)



    #<----Various Animations---->

    def hover(self, event):  

            self.canvas.itemconfig(self.BgLayer, fill = self.color2)



    def unhover(self, event):

            self.canvas.itemconfig(self.BgLayer, fill = self.color1)



    def action(self, event = None):

        self.canvas.itemconfig(self.textLayer, fill = self.txtColor + '4')

        if callable(self.command):

           self.command()



    def postAction(self, event = None):

        self.canvas.itemconfig(self.textLayer, fill = self.txtColor)



    def actionTmp(self, event):

        self.action()

        self.canvas.after(200, self.postAction)



            







class main():

    ' Main controller class for the program '

    def __init__(self):

        self.root=Tk()#main window

        self.root.minsize(width=1200,height=760)#maximises window at start

        self.root.wm_title('Planner')

        self.img1 = PhotoImage(file = 'back.gif')

        self.bgLayer = Canvas(self.root, width = 1200, height = 760)

        self.bgLayer.pack(fill = BOTH, expand = 1)

        self.bgLayer.create_image(0, 0, anchor = 'nw', image = self.img1)

        self.createGraphicObjects(220, 190)

        

    def createGraphicObjects(self,originX,originY):

        #creates a formatted program window

        self.grid = CalendarGrid(self.bgLayer, originX, originY)

        self.yearBox = transparentWidget(self.bgLayer, originX + 367, 20, str(currYear), '', '', 'yellow')

        self.monthBox = transparentWidget(self.bgLayer, originX + 367, 100, calendar.month_name[currMonth], '', '', 'yellow')

        self.nextButton = transparentWidget(self.bgLayer, 935, 100, '>', '', 'dodgerblue2', 'yellow', self.Next)

        self.backButton = transparentWidget(self.bgLayer, 285, 100, '<', '', 'dodgerblue2', 'yellow', self.Back)

        self.root.bind('<Right>', self.nextButton.actionTmp)

        self.root.bind('<Left>', self.backButton.actionTmp)

        self.bgLayer.bind('<Configure>', self.resize)



    def resize(self,event):

        w , h = event.width , event.height

        if(w > 1200):              #condition to filter required event

            x, y = (w-830)/2, (h-490)*3/4

            self.grid.render(x, y)

            self.nextButton.place(x+750, y-80)

            self.backButton.place(x+30, y-80)

            self.yearBox.place(x+380, y-150)

            self.monthBox.place(x+380, y-80)

        

    def Next(self, event=None):

        # Function to load next month

        global currMonth, currYear

        self.grid.clearValues()

        currMonth += 1

        if currMonth > 12:

            currMonth = 1

            currYear += 1

        self.grid.putValues(currMonth, currYear, 'forward')

        self.bgLayer.itemconfig(self.yearBox.textLayer, text = str(currYear))

        self.bgLayer.itemconfig(self.monthBox.textLayer, text = calendar.month_name[currMonth])

        



    def Back(self,event=None):

        # Function to load previous month

        global currMonth, currYear

        self.grid.clearValues()

        currMonth -= 1

        if currMonth < 1:

            currMonth = 12

            currYear -= 1

        self.grid.putValues(currMonth, currYear)

        self.bgLayer.itemconfig(self.yearBox.textLayer, text = str(currYear))

        self.bgLayer.itemconfig(self.monthBox.textLayer, text = calendar.month_name[currMonth])

   

# Globals

Weekdays = ['M', 'T', 'W', 'Th', 'F', 'Sa', 'S']



monthlyShift = [3, 0, 3, 2, 3, 2, 3, 3, 2, 3, 2, 3]

  # Number of days in month[i] = 28 + monthlyShift[i]



weekDayOnFirst = -101   

  # Refers to week day on first of current month



currDatetime = datetime.datetime.now()

currMonth = currDatetime.month

currYear = currDatetime.year



# MAIN SECTION
#program = main()

mainloop()
