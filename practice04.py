# Take a 3-digit number and check if all digits are distinct. 

num = int(input("Enter a 3-digit number: "))

a = num // 100      
b = (num // 10) % 10     
c = num % 10             

if a != b and b != c and a != c:
    print("All digits are distinct")
else:
    print("Digits are not distinct")


# 2. Take a 3-digit number and determine if the middle digit is the largest, smallest, or neither. 

num = int(input("Enter a 3-digit number: "))

a = num // 100
b = (num // 10) % 10
c = num % 10

if b > a and b > c:
    print("Middle digit is the largest")
elif b < a and b < c:
    print("Middle digit is the smallest")
else:
    print("Middle digit is neither largest nor smallest")



# 3. Take a 4-digit number and check if the first and last digits are equal. 


num = int(input("Enter a 4-digit number: "))

first = num // 1000
last = num % 10

if first == last:
    print("First and last digits are equal")
else:
    print("First and last digits are not equal")

# 4. Check whether a given integer is single-digit, double-digit, or multi-digit.

num = int(input("Enter an integer: "))

num = abs(num)  # handle negative numbers

if num < 10:
    print("Single-digit number")
elif num < 100:
    print("Double-digit number")
else:
    print("Multi-digit number")
