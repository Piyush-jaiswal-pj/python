#inheritance
#acquire the properties of another class 

#Parent class is the class being inherited from, also called base class.

#Child class is the class that inherits from another class, also called derived class.

#CREATING PARENTS CLASS

class infoBirds:
    def __init__(self, name):
     self.name=name;
    
    def printInfo(self):
      print(self.name);
        
x= infoBirds("Sparrow");
x.printInfo()

#Create a Child Class
class species(infoBirds):
  pass

x= species("Sparrow");
x.printInfo()

# adding init function 
#the child's __init__() function overrides the inheritance of the parent's __init__() function.

class species(infoBirds):
  def __init__(self, name):
     infoBirds.name=name;
     
x= infoBirds("Sparrow");
x.printInfo()

#Use the super() Function
#Python also has a super() function that will make the child class inherit all the methods and properties from its parent:
class species(infoBirds):
  def __init__(self, specie):
    super().__init__(specie);
    self.birdSpecies="BIRD"
     
  def fullName(self):
        print("BIRD NAME is",self.name,self.birdSpecies)

x= species("Sparrow");
x.fullName()
