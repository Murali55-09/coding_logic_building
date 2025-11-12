# Math and Number Logic
# Take a 3-digit number and check if all digits are distinct. 

num = 444

a = num // 100      # returns integer part of the quotient (435//100 --> 4)
b = (num // 10) % 10        #remove hundred place number and extract next number (num // 10 --> 43) % 10 --> 3
c = num % 10        # extract number at tens place(num %10 --> 5)

if(a != b and b != c and c != a):
    print("Numbers are distinct")

else:
    print("Numbers are Same")


""" a // b divides a by b and returns the integer part of the quotient
Ex: 7 // 2   →   3
"""

# Take a 3-digit number and determine if the middle digit is the largest, smallest, or neither. 
n = 413

l = n // 100
m = (n // 10) % 10
o = n % 10

if(l<m>o ):
    print( "Middle Number is Largest")

elif( l>m<o):
    print("Middle is Smallest Number")

else:
    print("Middle Number is nither Large nor small")


# Take a 4-digit number and check if the first and last digits are equal. 
number = 3643

a = number // 1000
b = number % 10

if(a == b):
    print("Both Numbers are equal")

else:
    print("Both Numbers are distinct")

# Check whether a given integer is single-digit, double-digit, or multi-digit. 
digit = 45

if(digit <= 9):
    print("single digit")

elif(10 <= digit <=99):
    print("Double Digit")

elif(100 <= digit <= 99999):
    print("Multi digit Number")


# Check if a number is a multiple of 7 or ends with 7. 
s = 3437
if( s % 7 == 0):
    print("Multiple of 7")

s1 = s % 10
if (s1 == 7):
    print("Number is ending with 7")

else:
    print("neither divisible nor ending with 7")