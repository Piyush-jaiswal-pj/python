#Tuples are used to store multiple items in a single variable.
#A tuple is a collection which is ordered and unchangeable & Allow Duplicates
#Tuple items are indexed
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple);
print(thistuple[0]);

#Tuple Length use print(len(name_of_tuple))
#To create a tuple with only one item, 
# you have to add a comma after the item, otherwise Python will not recognize it as a tuple.
#ex: thistuple = ("apple",)
#Tuple items can be of any data type: int strings etc 
# tofind the type of data use type() in print statement


#The tuple() Constructor
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)

# to access tuples item use same syntax that we use in lists
#print(thistuple[1]),print(thistuple[2:5]),print(thistuple[:4]),print(thistuple[2:]),print(thistuple[-4:-1])
#thistuple = ("apple", "banana", "cherry")
#if "apple" in thistuple:
  #print("Yes, 'apple' is in the fruits tuple")
