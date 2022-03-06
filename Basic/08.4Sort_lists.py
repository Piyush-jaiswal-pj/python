#Sort List Alphanumerically
#List objects have a sort() method that will sort the list alphanumerically, ascending, by default:
#By default the sort() method is case sensitive,
# resulting in all capital letters being sorted before lower case letters
#if you want a case-insensitive sort function, use str.lower as a key function:
# ex :thislist.sort(key = str.lower)
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

#sort descending, use the keyword argument reverse = True
thislist.sort(reverse = True)
print(thislist)

#Customize Sort Function customize your own function by using the keyword argument key = function.
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

# reverse() method reverses the current sorting order of the elements
thislist.reverse()
print(thislist)