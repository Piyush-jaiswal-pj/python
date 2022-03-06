#Change Values
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018   #thisdict.update({"color": "red"}) //for add items
#update() method will update the dictionary with the items from the given argument.
thisdict.update({"year": 2020})

#Adding Items
thisdict["color"] = "red"
print(thisdict)

#Removing Items
#The pop() method removes the item with the specified key name:
thisdict.pop("model")
print(thisdict)

#popitem() method removes the last inserted item
thisdict.popitem()
print(thisdict)

# del keyword removes the item with the specified key name:
del thisdict["color"]
print(thisdict)


#clear() method empties the dictionary
thisdict.clear()
print(thisdict)