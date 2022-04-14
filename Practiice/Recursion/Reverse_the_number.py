def reverse(n) :
    if(n==0) :
        return 0;
    
    else : 
      x = n % 10;
      n = reverse(int(n / 10));
      return x;
  
a = int(input("Enter the number to be reverse"));
c = reverse(a);
print(c);