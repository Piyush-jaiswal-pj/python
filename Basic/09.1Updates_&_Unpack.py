#Once a tuple is created, you cannot change its values. Tuples are unchangeable, 
# or immutable as it also is called.
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

#ADD List
#Since tuples are immutable,
# they do not have a build-in append() method, but there are other ways to add items to a tuple. 

# Convert into a list
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
#Add tuple to a tuple
y = ("orange",)
thistuple += y
print(thistuple);


#Remove Items
#You cannot remove items in a tuple.
#Tuples are unchangeable, so you cannot remove items from it, 
#but you can use the same workaround as we used for changing and adding tuple items:

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

#The del keyword can delete the tuple completely:

thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) #this will raise an error because the tuple no longer exists.

#Unpacking a Tuple
#When we create a tuple, we normally assign values to it. This is called "packing" a tuple:

#Packing a tuple:

fruits = ("apple", "banana", "cherry")

#But, in Python, we are also allowed to extract the values back into variables. This is called "unpacking":
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)


#Using Asterisk*
#If the number of variables is less than the number of values,
# you can add an * to the variable name and the values will be assigned to the variable as a list:

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")     
(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

#If the asterisk is added to another variable name than the last, 
# Python will assign values to the variable until the number of values left matches the number of variables left.
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)