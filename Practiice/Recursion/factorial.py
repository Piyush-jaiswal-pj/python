def fact(num):
 if(num==0):
   return 1;

 else:
   return num*fact(num-1);
 
read=int(input("enter fac"));
x=fact(read);

print(x)
