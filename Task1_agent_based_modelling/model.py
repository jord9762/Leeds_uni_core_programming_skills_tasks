import random 
#importing the random package
y0 = 67
x0 = 55
#assigning 50 to both of the above variables 
if random.random() < 0.5:
    y0 += 1
else:
    y0 -= 1
#basically either subtracting one or adding one at random, adding if less than 0.5 
#subtracting if greater than 0.5
if random.random() < 0.5:
    x0 += 1
else:
    x0 -= 1
#does the same as previous
print(y0, x0)
#prints



y1 = 6
x1 = 85

if random.random() < 0.5:
    y1 += 1
else:
    y1 -= 1

if random.random() < 0.5:
    x1 += 1
else:
    x1 -= 1

print(y1, x1)

answer = (((y0 - y1)**2) + ((x0 - x1)**2))**0.5 
print (answer)

"""So, how did you do with working out the distance?

Here's one solution:

answer = (((y0 - y1)**2) + ((x0 - x1)**2))**0.5
print(answer)

But sometimes it is more sensible to break complicated equations down into parts:

y_diff = (y0 - y1)
y_diffsq = y_diff * y_diff
x_diff = (x0 - x1)
x_diffsq = x_diff * x_diff
sum = y_diffsq + x_diffsq
answer = sum**0.5
print(answer)"""

y0 = random.randint(0,100)
x0 = random.randint(0,100)
y1 = random.randint(0,100)
x1 = random.randint(0,100)

y_diff = (y0 - y1)
y_diffsq = y_diff * y_diff
x_diff = (x0 - x1)
x_diffsq = x_diff * x_diff
sum = y_diffsq + x_diffsq
answer = sum**0.5
print(answer)
#alternate way the distance could have been calculated. 