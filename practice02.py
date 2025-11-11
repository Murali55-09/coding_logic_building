# Nested If & Multiple Conditions 

#Take three sides and check if they form a valid triangle.
# conditions for valid triangle 1. a + b > c, b + c > a, a + c > b

side1 = 43
side2 = 43
side3 = 44

if(side1 + side2 > side3 and side3 + side2 > side1 and side1 + side3 > side2):
    print("Sides can form valid triangle")

else:
    print("Sides will not form a valid triangle")

# f the sides form a valid triangle, determine whether it is equilateral, isosceles, or scalene.

"""conditions:
 equilateral --> all sides are equal, 
 isosceles --> 2 sides are equal, 
 scalene --> all sides are different"""

if( side1 == side2 == side3 ):
    print("sides will form equilateral triangle")

if(side1 == side2 or side2 == side3 or side1 == side3):
    print("sides will form isosceles triangle")

else:
     print("sides will form scalene triangle")

# Take marks (0–100) and print the corresponding grade (A/B/C/D/F). 
""" conditions:
marks >= 90 --> A
marks >= 80 --> B
marks >= 70 --> C
marks >= 60 --> D
else --> Fail"""

marks = int(input("Enter the Marks"))
if( 0 <marks <=100):
    if(marks >= 90):
        print("A Grade")

    elif(marks >= 80):
        print("B Grade")

    elif(marks >= 70):
        print("C Grade")

    else:
        print("Fail")

#Check if one of two given numbers is a multiple of the other. 
""" Conditions:
num 1 % num2 == 0 else num2 % num1 == 0"""

num1 = float(input("Enter the first number"))
num2 = float(input("Enter the second number"))

if(num1 % num2 == 0 or num2 % num1 == 0 ):
    print("Both are multiples of each")
else:
    print("Both are not multiple of each")

# Take the hour of the day (0–23) and print “Good Morning”, “Good Afternoon”, “Good Evening”, or “Good Night”. 

time = int(input("Enter the Time"))

if(1 <= time <12):
    print("Morning")

elif(12 <= time <17):
    print("Afternooon")

elif(17 <= time <20):
    print("Evening")

else:
    print("Night")


#Take a day number (1–7) and print the corresponding day name. 
""" switch statements"""

day_number = 7

match day_number:
    case 1:
        print("MONDAY")
    case 2:
        print("TUESDAY")
    case 3:
        print("WENSDAY")
    case 4:
        print("THURSDAY")
    case 5:
        print("FRIDAY")
    case 6:
        print("SATURDAY")
    case 7:
        print("SUNDAY")

