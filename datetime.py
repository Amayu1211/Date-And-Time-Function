#Current date in different formats

from datetime import date

today = date.today()

# dd/mm/YY
d1 = today.strftime("%d/%m/%Y")
print("d1 =", d1)

# Textual month, day and year	
d2 = today.strftime("%B %d, %Y")
print("d2 =", d2)

# mm/dd/y
d3 = today.strftime("%m/%d/%y")
print("d3 =", d3)

# Month abbreviation, day and year	
d4 = today.strftime("%b-%d-%Y")
print("d4 =", d4)


# Get the current date and time
from datetime import datetime

now = datetime.now()
 
print("now =", now)

# dd/mm/YY H:M:S
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("date and time =", dt_string)	



#Current time using datetime object
from datetime import datetime

now = datetime.now()

current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)


#Current time using time module

import time

t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)
print(current_time)

#Time .ctime() Function
import time

# seconds passed since epoch
seconds = 1545925769.9618232
local_time = time.ctime(seconds)
print("Local time:", local_time)	

#Time .sleep() Function
import time

print("This is printed immediately.")
time.sleep(2.4)
print("This is printed after 2.4 seconds.")

#Display The Calender
import calendar  
# Enter the month and year  
yy = int(input("Enter year: "))  
mm = int(input("Enter month: "))  
  
# display the calendar  
print(calendar.month(yy,mm))  



