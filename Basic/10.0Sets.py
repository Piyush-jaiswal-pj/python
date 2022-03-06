#Sets are used to store multiple items in a single variable.
#A set is a collection which is unordered, unchangeable*, and unindexed.
#do not allow duplicate values.
#thisset = {"apple", "banana", "cherry", "apple"} //not allowed
#use len() function for its length
#Set items can be of any data type
#type()
#sets are defined as objects with the data type 'set'

thisset = {"apple", "banana", "cherry"}
print(thisset)

#It is also possible to use the set() constructor to make a set.

thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)

#You cannot access items in a set by referring to an index or a key.

#But you can loop through the set items using a for loop, 
# or ask if a specified value is present in a set, by using the in keyword.

thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)
  
  #Change Items
#Once a set is created, you cannot change its items, but you can add new items.