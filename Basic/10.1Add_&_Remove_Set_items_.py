#ADD SET

#To add one item to a set use the add() method.

thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

#To add items from another set into the current set, use the update() method.
# ex : thisset.update(tropical) //tropical is another set name
#The object in the update() method does not have to be a set, i
# t can be any iterable object (tuples, lists, dictionaries etc.)

thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)

#Remove Item
#o remove an item in a set, use the remove(), or the discard() method.

thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)

# discard mehod

thisset.discard("banana")
print(thisset)

#You can also use the pop() method to remove an item, but this method will remove the last item
#Ex:
x = thisset.pop()
print(x)
print(thisset)

#The clear() method empties the set:

thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)


#The del keyword will delete the set completely:

thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset)