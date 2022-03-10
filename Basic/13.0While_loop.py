#while loop we can execute a set of statements as long as a condition is true.
i = 1
while i < 6:
  print(i)
  i += 1
  
  #break statement we can stop the loop even if the while condition is 
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1
  
  #continue statement we can stop the current iteration, and continue with the next
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
  
  #we can use  else statement also 
  i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")