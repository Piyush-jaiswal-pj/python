#Module :
#Consider a module to be the same as a code library.
#A file containing a set of functions you want to include in your application

#creating the module by using the file 21.1Module_EX_File.py as module file..

#using module
# import 21.1Module_EX_File #dont save the file like this
# 21.1Module_EX_File.greeting("jhon") #Module_EX_File like this u need to call

# rename 
# import 21.1Module_EX_File as mx

# a = mx.person1["age"]
# print(a)

#built in modules

import platform
x=platform.system()
print(x)

import platform
x=dir(platform) #The dir() function can be used on all modules, also the ones you create yourself.

print(x)

#choosing specific module element
#ex
from mymodule import person1

print (person1["age"])