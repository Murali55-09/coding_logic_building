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