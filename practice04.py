# Take a 3-digit number and check if all digits are distinct. 

num = int(input("Enter a 3-digit number: "))

a = num // 100      
b = (num // 10) % 10     
c = num % 10             

if a != b and b != c and a != c:
    print("All digits are distinct")
else:
    print("Digits are not distinct")




# 2. Take a 3-digit number and determine if the middle digit is the largest, smallest, or 
# neither. 
# 3. Take a 4-digit number and check if the first and last digits are equal. 
# 4. Check whether a given integer is single-digit, double-digit, or multi-digit.