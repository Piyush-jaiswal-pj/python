#Add items in lists

# add an item to the end of the list, use the append() method:
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

# insert a list item at a specified index, use the insert() method.
thislist.insert(2,"orange")
print(thislist)

#append elements from another list to the current list, use the extend() method
#Add the elements of tropical to thislist 
# you can add any iterable object (tuples, sets, dictionaries etc.)
#example : thistuple = ("kiwi", "orange")
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)


#Remove Specified Item use remove()
thislist.remove("banana")
print(thislist)

#The pop() method removes the specified index.
# del keyword also removes the specified index and lists 
thislist.pop(1)
print(thislist)

#The clear() method empties the list.
#thislist.clear()