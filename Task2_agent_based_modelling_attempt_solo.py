import random
x0= random.randint(0,99)
y0= random.randint(0,99)
x1= random.randint(0,99)
y1= random.randint(0,99)

x_diffe = x0-x1
y_diffe = y0-y1
x_square = x_diffe**2
y_square = y_diffe**2
xy_added = x_square + y_square
answer = xy_added**0.5
print(answer)