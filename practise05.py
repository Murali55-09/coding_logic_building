# Take coordinates (x, y) and check if the point lies on the X-axis, Y-axis, or at the 
# origin. 
x = 3
y = 0
if(x == 0 and y == 0):
    print("Origin") 
elif(x == 0):
    print("Y-axis")
elif(y == 0):
    print("X-axis")
else:
    print("Point lies neither on X-axis nor Y-axis")

# . Take three numbers and check if they can form a Pythagorean triplet 
# pythagoras triplet means a^2 + b^2 = c^2 (s a set of three positive integers a, b, and c, that satisfy the Pythagorean theorem:)

a = 3
b = 11
c = 5
if(a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or c**2 + a**2 == b**2):
    print("They form a Pythagorean triplet")
else:
    print("They do not form a Pythagorean triplet")


# Take time (hours and minutes) and print the smaller angle between the hour and minute hands
# logic: angle between hour and minute hands = |30*hours - (11/2)*minutes|
hours = 3
minutes = 15

# Calculate the angles
hour_angle = (hours * 30) + (minutes * 0.5)
minute_angle = minutes * 6

# Find the difference
angle_diff = abs(hour_angle - minute_angle)

# Get the smaller angle
smaller_angle = min(angle_diff, 360 - angle_diff)

print(f"The smaller angle between the hour and minute hands is: {smaller_angle} degrees")


# Take three numbers and check if they are in arithmetic progression.
num1 = 5
num2 = 10
num3 = 15
if(num2 - num1 == num3 - num2):
    print("The numbers are in arithmetic progression")
else:
    print("The numbers are not in arithmetic progression")

# Take three numbers and check if they are in geometric progression.
num1 = 2
num2 = 6
num3 = 18   
if(num2/num1 == num3/num2):
    print("The numbers are in geometric progression")
else:
    print("The numbers are not in geometric progression")

# Take a 3-digit number and check if the sum of the first and last digit equals the middle digit. 
number = 123
first_digit = number // 100
last_digit = number % 10
middle_digit = (number // 10) % 10

if(first_digit + last_digit == middle_digit):
    print("The sum of the first and last digit equals the middle digit.")
else:
    print("The sum of the first and last digit does not equal the middle digit.")