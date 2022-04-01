#Class is object constructor or a blueprint for creating the objects

class myClass:
    x=5
p1 =myClass()
print(p1.x)

#The __init__() Function 
# understand the meaning of classes we have to understand the built-in __init__() function.
# it executed when class is being initiated.
#Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created

class info:
    def __init__(self,name,age):
        self.name=name;
        self.age =age;

p1=info("john",36)
print(p1.age);
print(p1.name);

#object can also contains methods.Methods in objects are function that belong to the object.

class infoCar:
    def __init__(self,name,model):
        self.name = name;
        self.model= model;
        
    def infoProvider (self):
     print("Car name is "+ self.name);
            
            
p2= infoCar("TATA",2020);
p2.infoProvider()

#self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.
# we can use any name in the place of self but it should be the first parameters
 
 #modify obj properties
p2.name="JAGUAR"       
p2.infoProvider()

#delete obj properties
del p2.model:

del p2 #del obj

#Pass statement to avoid any error 
