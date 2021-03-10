#imports the random module
import random
#Make y0 and x0 = 50
y0 = 50
x0 = 50
# Move y0 randomly
if random.random() < 0.5:
    y0 += 1
else:
    y0 -= 1
# Move x0 randomly
if random.random() < 0.5:
    x0 += 1
else:
    x0 -= 1
# Make y1 and x1 = 50    
y1 = 50
x1 = 50
# Move y1 randomly
if random.random() < 0.5:
    y1 += 1
else:
    y1 -= 1
# Move x1 randomly
if random.random() < 0.5:
    x1 += 1
else:
    x1 -= 1
# print answer
print(y0, x0, y1, x1)

x0= random.randint(0,99)
y0= random.randint(0,99)
x1= random.randint(0,99)
y1= random.randint(0,99)
#sets a random integer for x0.......
#the below code can be run with from line 32 down to get random integers
x_diffe = x0-x1
y_diffe = y0-y1
#creates a variable which will store the difference between x0-x1 and y0-y1
x_square = x_diffe**2
y_square = y_diffe**2
#creates squared variables 
xy_added = x_square + y_square
answer = xy_added**0.5
print(answer)
#calculates and prints euclidian distance between co-rdinates



