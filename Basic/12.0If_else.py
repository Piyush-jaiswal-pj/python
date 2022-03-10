#If else 
#syntax : if condition : 
    #       statement with proper indentation
x=10;
y=5;
if x>y :
 print("x is greater than y")# if we have single statement than we can code statement with if in single line and same goes for other syntax also...
  # ex : if x>y : print("x is greater than y")
  # ex : print("A") if a > b else print("B") // short hand if else
 
 #The elif keyword is pythons way of saying "if the previous conditions were not true, then try this condition"
 # basically it is else if (in other programing language)
#syntax : elif condition : 
    #       statement with proper indentation

#else = if condition is false than it will execute;
#syntax : else : 
    #       statement with proper indentation
    
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

#and keyword is a logical operator, and is used to combine conditional statements:
# and basically for both the condition are true
a = 250
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")
  
  # or is basically any one oof the condition is true
  
  # Nested if else 
x=50

if x > 10:
  print("Above ten,")# note the indentation 
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")
    
    # IF condition should not be empty if it is than  use pass
    #ex : if a>b
      #      pass;