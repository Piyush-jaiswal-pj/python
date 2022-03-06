# using a for loop.
#Print all key names in the dictionary, one by one:

for x in thisdict:
print(x)
Print all values in the dictionary, one by one:#Print all values in the dictionary, one by one:
      
#values() method to return values of a dictionary
for x in thisdict.values():
print(x)
  
#keys() method to return the keys of a dictionary
for x in thisdict.keys():
print(x)
  
  #Loop through both keys and values, by using the items() method
for x, y in thisdict.items():
print(x, y)

#Copy a Dictionary
# using copy()
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)

#Make a copy of a dictionary with the dict() function
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)


# Nested Dictionaries
# A dictionary can contain dictionaries, this is called nested dictionaries.
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

#or

child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}