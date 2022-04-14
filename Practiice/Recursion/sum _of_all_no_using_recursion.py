#sum _of_all_no_using_recursion.py
def  sum_of_all_no(n) :

 if n==0 :
     return 0;
 else :
    return (n % 10 + sum_of_all_no(int(n/10)))


x =int(input("enter the numbers"))
c = sum_of_all_no(x);
print (c);