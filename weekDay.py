#Filename:  weekDay.py
#Author:    Mark Parry
#Created:   17/02/2021
#Purpose:   Returns the day of the week from todays date and checks if it a working day or the weekend
#References: https://pythontic.com/datetime/date/weekday        Weekday Function in Python uses datetime module
#            https://pythontic.com/datetime/date/introduction   How to get todays date

#bring in the datetime module
import datetime

#store the days of the week in a tuple(these are not going to change)
weekDays = ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")


#get todays date using the datetime module
todaysDate = datetime.date.today()

#check if it is a working day (Mon to Fri, index less than 5)
if todaysDate.weekday()  < 5:
    workDay = True


#use the result of the .weekday() on todays date  as the index to get the string from the weekdays tuple
todaysDay = weekDays[todaysDate.weekday()]

#output whether it is a working day or the weekend
if workDay: 
    print("Today {} is {} which unfortunately is a working day".format(todaysDate,todaysDay))
else:
    print("Today {} is {} and thankfully it  is the weekend!".format(todaysDate,todaysDay))
