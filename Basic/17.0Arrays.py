# Array is a special variable which hold more than one value at a time.
cars = ["TATA","BMW","JAGWAR"]
 #accessing the elements 
X = cars[0];
print(X);
#length
x=len(cars);
print(x)

# for loop
for i in cars :
    print(i);

#append 
cars.append("HONDA");
for i in cars :
    print(i);

#remove elements 
cars.pop(1);
cars.remove("TATA")# delete element by their name
for i in cars :
    print(i);

