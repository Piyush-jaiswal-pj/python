#Loop Through a Tuple
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)
  
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1
  
for i in range(len(thistuple)):
 print(thistuple[i])
 
 
 # Join Two Tuples
 # you can use the + operator
 tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

#Multiply Tuples
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)

#Methods
#count()	Returns the number of times a specified value occurs in a tuple
#index()	Searches the tuple for a specified value and returns the position of where it was found