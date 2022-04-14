#RegEX = regular expression ,it s a sequance of character that forms a search patterns
# used to check if a string contains the specified search pattern
#python have built in module for regex (re)

import re

txt = "The rain in Spain"
#search ()function
x = re.search("^The.*Spain$", txt)#Search the string to see if it starts with "The" and ends with "Spain
x1 = re.search("\s", txt) #\s return white space
print("The first white-space character is located in position:", x1.start())
#RegEx Functions

#Function	Description
#findall	Returns a list containing all matches
#search	    Returns a Match object if there is a match anywhere in the string
#split	    Returns a list where the string has been split at each match
#sub	    Replaces one or many matches with a string

#learn all metacharacters (ref ...w3)
# also Special sequence(\)
#also sets

#the findall()function

x = re.findall("ai", txt)# return el list
print(x)
x = re.findall("Portugal", txt)# returnn  empty list
print(x)

#split()
x = re.split("\s", txt)
print(x)

#sub ()
x = re.sub("\s", "9", txt)
print(x)

#Match Object contains info about search and result if empty or not match return none
#span() returns a tuple containing the start-, and end positions of the match.
#.string returns the string passed into the function
#.group() returns the part of the string where there was a match
x = re.search(r"\bS\w+", txt)
print(x.span())
print(x.string)
print(x.group())