#Loop Items


#Example
#Loop through the set, and print the values:

thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)
  
  #Join Two Sets
  # use the union() method that returns a new set containing all items from both sets,
  # or the update() method that inserts all the items from one set into another:
  set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2) # set1.update(set2)
print(set3)

#intersection_update() method will keep only the items that are present in both sets
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)
print(x)

#The intersection() method will return a new set, that only contains the items that are present in both sets.
#ex :  = x.intersection(y)

#The symmetric_difference_update() method will keep only the elements that are NOT present in both sets
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)

print(x)

#The symmetric_difference() method will return a new set, that contains only the elements that are NOT present in both sets.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.symmetric_difference(y)

print(z)


#add()	Adds an element to the set
clear()	                    Removes all the elements from the set
copy()	                    Returns a copy of the set
difference()	              Returns a set containing the difference between two or more sets
difference_update()         Removes the items in this set that are also included in another, specified set
discard()	                  Remove the specified item
intersection()	            Returns a set, that is the intersection of two other sets
intersection_update()	      Removes the items in this set that are not present in other, specified set(s)
isdisjoint()	              Returns whether two sets have a intersection or not
issubset()	                 Returns whether another set contains this set or not
issuperset()                 Returns whether this set contains another set or not
pop()	                       Removes an element from the set
remove()	                   Removes the specified element
symmetric_difference()      Returns a set with the symmetric differences of two sets
symmetric_difference_update()	inserts the symmetric differences from this set and another
union()	                   Return a set containing the union of sets
update()	                 Update the set with the union of this set and others