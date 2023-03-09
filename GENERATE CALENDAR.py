#Generating a calender

import calendar
y=int(input("enter the year="))
n=1
cal=calendar.TextCalendar(calendar.SUNDAY)
i=1
while i<=12:
    cal.prmonth(y,i)
    i+=1
