#Copy a List
#You cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2.
# There are ways to make a copy, one way is to use the built-in List method copy().\
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

#Another way to make a copy is to use the built-in method list().
#ex : mylist = list(thislist)

#Join  The lists
# Join Two Lists
#One of the easiest ways are by using the + operator.
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

#Another way to join two lists is by appending all the items from list2 into list1, one by one:
for x in list2:
  list1.append(x)

print(list1)

# you can use the extend() method, 


list1.extend(list2)
print(list1)