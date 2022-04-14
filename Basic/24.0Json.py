# JSON is sytanx for storing and exchanging the data
#it is a text written with js object notation

# in python  json is a built in function  which can be used to work with JSOn Data.


#Parse JSON - Convert from JSON to Python
#If you have a JSON string, you can parse it by using the json.loads() method.

#The result will be a Python dictionary

import json

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])

#Convert from Python to JSON
#If you have a Python object, you can convert it into a JSON string by using the json.dumps() method.


# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)



#You can convert Python objects of the following types, into JSON strings:

#dict	Object
#list	Array
#tuple	Array
#str	String
#int	Number
#float	Number
#True	true
#False	false
#None	null

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x))
#Use the indent parameter to define the numbers of indents:

#formatting the result
json.dumps(x, indent=4)

json.dumps(x, indent=4, separators=(". ", " = "))

#Use the sort_keys parameter to specify if the result should be sorted or not:

json.dumps(x, indent=4, sort_keys=True)

