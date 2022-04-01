#scope

# variable is only availalble from inside the region it is created. this is called scope.

#Local scope created inside a function range is inside the function only
def fun():
    x=20; #llocal scope
    print(x);
    
fun();

#Global Scope
#which declare outside the func class etc :
#it is accessiable for all having high priority
#The global keyword makes the variable global.
def myfunc():
  global x
  x = 300

myfunc()

print(x)