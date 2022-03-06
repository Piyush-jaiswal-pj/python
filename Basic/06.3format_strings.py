# String Format
#we can combine strings and numbers by using the format() method! \\directly we cant format the strings so use this  always
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

 # we also use indexing 
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))