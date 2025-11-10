# Take a number and print whether it’s positive, negative, or zero.
num = -7
if(num > 0):
    print("Positive Number")

elif(num < 0):
    print("Negative Number")

else:
    print("Zero")


#Check if a number is even or odd. 
num =9

if(num %2 == 0):
    print("Number is even")

else:
    print("Number is Odd")

#Check if a number is divisible by 5. 
num = 15
if(num % 5 == 0):
    print("Number is divisible by 5")

else:
    print("Number is not divisible by 5")

#Check if a number is divisible by both 3 and 5.
num = 15
if(num % 3 == 0 and num % 5 == 0):
    print("Number is dividsible by both 3 and 5") 

else:
    print("Number is not divisible by both 3 and 5")

# Check if a given year is a leap year.
# Conditions 1. must year % 4 ==0 and must year % 100 != 0, or year % 400 == 0
#If divisible by 400 → ALWAYS leap year.
#If divisible by 100 but not 400 → NOT leap year.
#If divisible by 4 but not 100 → Leap year.
#Else → Not a leap year.

year = 2020

if (year % 400 == 0) or (year % 4 ==0 and year % 100 != 0):
    print(f"{year} is leap year")

else:
    print(f"{year} is not a leap year")

# Take two numbers and print the larger one. 

num1 = 55
num2 = 53

if(num1 > num2):
    print(f"{num1} is larger")

elif(num2 > num1):
    print(f"{num2} is larger")

else:
    print("Both are same")

# print("number is large is: ", max(num1, num2))


#Take three numbers and print the largest. max(num1, num2, num3)

a = 53
b = 54
c = 23

print("largest among the numbers is:", max(a, b, c))


#Take a temperature value and print “Cold”, “Warm”, or “Hot” using range conditions.
tempt = 34
if (tempt < 20):
    print("Cold")

elif(20 < tempt < 30):
    print("Warm")

else:
    print("Hot")


#Take a character and check if it’s a vowel or consonant.
vol = ['a', 'e', 'i', 'o', 'u']
alph = 'i'

if alph in vol :
    print("It's Vowel")

else:
    print("Its Consonents")

#  Take a character and check whether it’s uppercase, lowercase, a digit, or a special character. 

ch = input("Enter a character: ")

if 'A' <= ch <= 'Z':
    print(ch, "is an Uppercase letter")
elif 'a' <= ch <= 'z':
    print(ch, "is a Lowercase letter")
elif '0' <= ch <= '9':
    print(ch, "is a Digit")
else:
    print(ch, "is a Special character")
