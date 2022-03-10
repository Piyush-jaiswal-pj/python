#for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string)
x=["a","b","c"]
for i in x: # here i is getting the  values from the x 
    print(i);
    # we can pass string also 
    # we can use break and continue also:
    # ex :
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break # it breaks from the whole loop
  print(x)
  
  # range function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number
  for x in range(6): #range(2, 6):
    print(x)
    
#Nested Loops
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)
    # we can pass also;
    
  