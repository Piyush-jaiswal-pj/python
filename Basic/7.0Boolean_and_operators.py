#Booleans represent one of two values: True or False.
a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")
  
#  bool() function allows you to evaluate any value, and give you True or False in return,

  print(bool("Hello"))
  
# Operators are used to perform operations on variables and values.
# types of operator

#Arithmetic operators
# +	Addition		
# -	Subtraction		
# *	Multiplication		
# /	Division		
# %	Modulus		
# **Exponentiation		
# //  Floor division

#Assignment operators
#    =	, += , -= , *= , /=	, %= , //=	, **= , &=	, |= , ^= , >>=	, <<=

# Comparison Operators
# ==	Equal , !=	Not equal , >	Greater than ,	<	Less than	, >=	Greater than or equal to ,	<= Less than or equal to


# Logical Operators
# and 	Returns True if both statements are true	
# or	Returns True if one of the statements is true	
# not	Reverse the result, returns False if the result is true

#Identity Operators
#is 	Returns True if both variables are the same object
#is not	Returns True if both variables are not the same object

# Membership Operators
#in 	Returns True if a sequence with the specified value is present in the object
# not in	Returns True if a sequence with the specified value is not present in the object

# Bitwise Operators

# & 	AND	    Sets each bit to 1 if both bits are 1
# |	     OR	    Sets each bit to 1 if one of two bits is 1
 # ^	XOR	    Sets each bit to 1 if only one of two bits is 1
# ~ 	NOT	    Inverts all the bits
# <<	Zero    fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off
# >>	Signed right shift