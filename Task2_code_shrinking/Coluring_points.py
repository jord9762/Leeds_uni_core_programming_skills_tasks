import matplotlib.pyplot

import operator

import random

agents = []

num_of_agents = 10
num_of_iterations = 100
agents = []

for i in range(num_of_agents):
    agents.append([random.randint(0,99),random.randint(0,99)])
print (agents)

for j in range(num_of_iterations):
    for i in range(num_of_agents):

        if random.random() < 0.5:
            agents[i][0] = (agents[i][0] + 1) % 100
        else:
            agents[i][0] = (agents[i][0] - 1) % 100

        if random.random() < 0.5:
            agents[i][1] = (agents[i][1] + 1) % 100
        else:
            agents[i][1] = (agents[i][1] - 1) % 100

#running the line of code whcih says agents [] as well as agents. append will change the specified co-ordinates
#running the agents.append will add new values onto the end of our agents tuple, while preserving the previous
#from left to right we have y0,x0,y1,x1

print(max(agents))

#this will get the co-ordinates with the max x value, remeber that 1 is the second element as containers are
#indexed from 0 and not 1. 
print(max(agents, key=operator.itemgetter(1)))


matplotlib.pyplot.ylim(0, 100)
matplotlib.pyplot.xlim(0, 100)
matplotlib.pyplot.scatter(agents[0][1],agents[0][0])
matplotlib.pyplot.scatter(agents[1][1],agents[1][0])
m = max(agents, key=operator.itemgetter(1))

matplotlib.pyplot.scatter(m[1],m[0], color='red')
matplotlib.pyplot.show()
#with the matplot co-ordinates [0][1] is saying row 1 column 2 and this is the x0
#with the matplot co-ordinates [0][0] is saying row 1 column 1 and this is the y0
#with the matplot co-ordinates [1][0] is saying row 2 column 2 and this is the x1
#with the matplot co-ordinates [1][1] is saying row 2 column 2 and this is the y1
#final segments of code colour the co-ordinate furthest east red and the one furthest west blue
