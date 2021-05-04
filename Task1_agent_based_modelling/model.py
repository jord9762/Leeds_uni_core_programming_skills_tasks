#importing the random package
import random 
#assigning the integer 50 to both of the above variables 
y0 = 50
x0 = 50
#either subtracts by one or adds by one at random, adding if less than 0.5 
#subtracting if greater than 0.5, in this sense it is not truly random. 
if random.random() < 0.5:
    y0 += 1
else:
    y0 -= 1

if random.random() < 0.5:
    x0 += 1
else:
    x0 -= 1
#prints variables after being randomised
print(y0, x0)



#lines 23 to 36 repeat the previous process for a second set of co-ordinates.
y1 = 50
x1 = 50

if random.random() < 0.5:
    y1 += 1
else:
    y1 -= 1

if random.random() < 0.5:
    x1 += 1
else:
    x1 -= 1

print(y1, x1)
#Whole equation I initially came up with, efficent but potentially difficult to understand. 
answer = (((y0 - y1)**2) + ((x0 - x1)**2))**0.5 
print (answer)


#Below may be a more sensible way to calculate distance
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

