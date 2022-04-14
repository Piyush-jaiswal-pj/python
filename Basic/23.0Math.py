# math is built in function that allows to do mathematical operation

#The min() and max() functions can be used to find the lowest or highest value in an iterable:

x=min(5,6,10);
y= max(0,10,2);
print(y);
print(x)

#abs() function returns the absolute (positive) value of the specified number:

x = abs(-7.25)

print(x)

#The pow(x, y) function returns the value of x to the power of y (xy).

x=pow(4,2);
print(x);

#MAth module 
import math
x= math.sqrt(65);
print(x);

#The math.ceil() method rounds a number upwards to its nearest integer, 
# and the math.floor() method rounds a number downwards to its nearest integer, 
# and returns the result:

import math

x = math.ceil(1.4)
y = math.floor(1.4)

print(x) # returns 2
print(y) # returns 1

#The math.pi constant, returns the value of PI (3.14...):

x = math.pi

print(x)