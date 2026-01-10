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