# Lists Acessing 
#you can access them by referring to the index number


thislist = ["apple", "banana", "cherry"]
print(thislist[1])

#Negative indexing means start from the end.
print(thislist[-1])

#You can specify a range of indexes by specifying where to start and where to end the range
#same you can apply on the negative indexing[-1:1]
print(thislist[0:2])#Return the 1 and 2 item:

#Check if Item Exists using "in"
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
  
  # same as above concept u can change the list   items  ....
  #example:
thislists[1] = "blackcurrant"
print(thislists)

#Insert Items using insert()
thislist.insert(2, "watermelon")# 2 is index and watermelon is object that is inserted at 2nd index
print(thislist)