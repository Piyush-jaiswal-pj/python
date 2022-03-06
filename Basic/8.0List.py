# Lists
# Lists are used to store multiple items in a single variable
thislist = ["apple", "banana", "cherry"]
print(thislist)

#List Items
#List items are ordered, changeable, and allow duplicate values.List items are indexed,
# here from the ordered means that the items have a defined order, and that order will not change.
#Changeable meansThe list is changeable, meaning that we can change, add, and remove items in a list after it has been created.


#List Length
print(len(thislist))

#List Items - Data Types
#list1 = ["abc", 34, True, 40, "male"] //multi datatypes

#type()
print(type(thislist))

#The list() Constructor
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)