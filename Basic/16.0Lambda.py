#lambda = anonymous function
#takes the number of arguments but can only have one expression.

#syntax  
#lambada arguments : expression
#ex

x=lambda a,b:a+b;
print(x(5,6));

#power of lambada is better than as an anonymous fuction inside another function.
# ex
def multiply(n):
    return lambda a:a*n;

mydoubler =multiply(2)
print(mydoubler(16))