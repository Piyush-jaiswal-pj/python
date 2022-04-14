#file handling

# py has function like creating delering updating and reading.

#the key function for working with files in Python is the open() function
#The open() function takes two parameters; filename, and mode.

#There are four different methods (modes) for opening a file:

#"r" - Read - Default value. Opens a file for reading, error if the file does not exist

#"a" - Append - Opens a file for appending, creates the file if it does not exist

#"w" - Write - Opens a file for writing, creates the file if it does not exist

#"x" - Create - Creates the specified file, returns an error if the file exists

# addition you can specify if the file should be handled as binary or text mode

#"t" - Text - Default value. Text mode

#"b" - Binary - Binary mode (e.g. images)

#syntax
f = open("E:\\python\Basic\30.1Demo.txt", "r")
print(f.read())
f = open("30.1Demo.txt", "r")
print(f.read())


#Read Only Parts of the File
f = open("30.1Demo.txt", "r")
print(f.read(5))

#Read Lines
f = open("30.1Demo.txt", "r")
print(f.readline())#read single line only 

#close files 
f = open("30.1Demo.txt", "r")
print(f.readline())
f.close()

# writing existing file
f = open("demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()
# to append 
#first open the file and write thn read

#creating the new file 
f=open("demo1.txt","x")
f.write("Now the file has more content!")
f.close()


#deleting the files
#first import the os than use remove()
#ex:  
import os
os.remove("30.1Demo.txt")

# check if file exist:
 import os
 if os.path.exists("30.1Demo.txt")
 os.remove("30.1Demo.txt")
 else:
  print("The file does not exist")
 
 # delete folder
 
 import os 
 os.rmdir("myfolder")# only empty folders can be remove....
 
