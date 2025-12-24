# find distance between two co-ordinates

import math

x1 = float(input('Enter x1'))
y1 = float(input('Enter x1'))
x2 = float(input('Enter x1'))
y2 = float(input('Enter x1'))

distance = math.sqrt((x2 - x1)**2 + (y2-y1)**2)
print(f"Distance is {distance}")

# another method

point1 = (x1,y1)
point2 = (x2,y2)

distance = math.dist(point1, point2)
print(f"Distance is {distance}")