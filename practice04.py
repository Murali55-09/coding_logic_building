# Take a character and check if it is a letter, a digit, or neither.

ch = '34'

if 'a' <= ch <= 'z' or 'A' <= ch <= 'Z':
    print(f"Letter is", ch)

elif '0' <= ch <= '9':
    print(f"Digit is", ch)


# logic for the given character not a letter and digit
def chacheck(chart):
    if('a' <= chart <= 'z' or 'A' <= chart <= 'Z' or '0' <= chart <= '9'):
        return False

    else:
        return True

chart = input("Enter the Character")
print(chacheck(chart))
# Learning: All comparisons are numeric.
# Characters are compared using ASCII/Unicode values.
# C allows implicit conversion, Python does not.

# ASCII comparison is fast, predictable, and interview-preferred
# Built-ins handle Unicode, not ideal for systems/DSA
# Letters & digits occupy fixed ASCII ranges
# Unicode characters will fail ASCII-based checks


# Take a number and print “Fizz” if divisible by 3, “Buzz” if divisible by 5, and 
# “FizzBuzz” if divisible by both.

num = int(input("Enter the number"))

result = "FizzBuzz" if num % 3 == 0 and num % 5 == 0 else "Fizz" if num % 3 == 0 else "Buzz" if num % 5 == 0 else "Not Divisible By 3 or 5"
print(result)

# Take three numbers and print the median value (neither maximum nor minimum).

num1 = 4
num2 = 5
num3 = 3

if (num1 < num2 and num1 > num3) or (num1 > num2 and num1 < num3 ):
    print(f"Median =", num1)

elif (num2 > num1 and num2 < num3) or (num2 <num1 and num2 > num3):
    print(f"Median is", num2)

else:
    print(f"Median is", num3)

# Take 24-hour time (hours and minutes) and print whether it is AM or PM

a = int(input("Enter the time "))

if(12 <= a ):
    print("PM")

else:
    print("AM")
