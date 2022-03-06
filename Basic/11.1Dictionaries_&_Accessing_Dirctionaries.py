#Dictionaries 
#Dictionaries are used to store data values in key:value pairs.

#A dictionary is a collection which is ordered*, changeable and do not allow duplicates(two keys with same name is not allowed).

# note :  As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

direc={
    "name" :"Piyush",
    "Age" : 20,
    "From": "indore"
}
print(direc)

#Dictionary items are presented in key:value pairs, and can be referred to by using the key name.
print(direc['name'])

#Dictionary Length by using len()
# ex: 
print(len(direc))

#Dictionary Items - Data Types :any data type we can use ..

# by type() function gives the data type of the item
print(type(direc))

#Accessing Directinories
#You can access the items of a dictionary by referring to its key name, inside square brackets:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]

#get() that will give you the same result
x = thisdict.get("model")

# keys() method will return a list of all the keys in the dictionary.
x = thisdict.keys()

#values() method will return a list of all the values in the dictionary.
x = thisdict.values()

#items() method will return each item in a dictionary, as tuples in a list.
x = thisdict.items()
#To determine if a specified key is present in a dictionary use the in keyword

if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")