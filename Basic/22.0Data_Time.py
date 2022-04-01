#it is a built in module named as a datetime to work as object...
#ex:
import datetime

x= datetime.datetime.now();
print(x)

#object of date time
import datetime

x= datetime.datetime.now();

print(x.year)#year
print(x.strftime("%A"))#day

#The datetime() class requires three parameters to create a date: year, month, day.

import datetime

x = datetime.datetime(2020, 5, 17)
print(x)

#The strftime() Method
#he method is called strftime(), and takes one parameter, format, to specify the format of the returned string:
import datetime

x = datetime.datetime(2018, 6, 1)

print(x.strftime("%B"))