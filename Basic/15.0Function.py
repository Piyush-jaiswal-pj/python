# FUNctions
#blocks of code that execute when we call it 
# def : key used to define function in python

def add():
    x=5
    y=10
    print(x+y)
    
add()

#Arguments
# that we pass the value at calling time
#Information can be passed into functions as arguments
#A parameter is the variable listed inside the parentheses in the function definition.

#An argument is the value that is sent to the function when it is called.

def sub(x,y): # x,y are parameters

    print(x+y)
    
sub(5,3); #arguments

#call the function with 1 or 3 arguments, you will get an error

#Arbitrary Arguments, *args
# If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition
# this achieve the tuples

def my_function(*kids): # passing unkown args
  print("The youngest child is " + kids[2])

my_function("A", "B", "C")

#Keyword Arguments : send arguments with the key = value

def sub(x,y): # x,y are parameters

    print(x+y)
    
sub(x=5,y=3); #arguments    x and y are keys

#Arbitrary Keyword Arguments, **keywordsargs 
# passes unkowns keys

def sub(**z): # x,y are parameters

    print(z )
    
sub(x=5,y=3); #arguments    x and y are keys


#Default Parameter Value
def add():
    x=5
    y=10
    print(x+y)
    
add()#default ags

#end any data types of argument to a function (string, number, list, dictionary etc.), and it will be treated as the same data type inside the function
def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)

#Return Values
def my_function(x):
  return 5 * x


print(my_function(3))
print(my_function(5))
print(my_function(9))


#function definitions cannot be empty, but if you for some reason have a function definition with no content, put in the pass

def myfunction():
  pass

#Recursion
# means a defined function can call itself.
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)