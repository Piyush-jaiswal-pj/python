#LOOP LIST
#You can loop through the list items by using a for loop
thislist = ["apple", "banana", "cherry"]
for x in thislist:
 print(x)
  
  #Loop Through the Index Numbers
  #Use the range() and len() functions to create a suitable iterable.
for i in range(len(thislist)):
 print(thislist[i])
 
 #Using a While Loop
 i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1
  
  
#Looping Using List Comprehension
#A short hand for loop that will print all items in a list:
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]


#LIST COMPREHENSION
#offers short syntax when  you want to create a new list based on the values of an existing list.

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

#With list comprehension you can do all that with only one line of code:

newlist1 = [x for x in fruits if "a" in x]

print(newlist1)

#SYNTAX : newlist = [expression for item in iterable if condition == True]

#Iterable
# The iterable can be any iterable object, like a list, tuple, set etc.
newlist = [x for x in range(10)]

#Expression
# The expression is the current item in the iteration, but it is also the outcome, 
# which you can manipulate before it ends up like a list item in the new list
newlist2 = [x.upper() for x in fruits]