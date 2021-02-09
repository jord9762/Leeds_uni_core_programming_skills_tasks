import matplotlib.pyplot

import operator

import agents

import random

agents = []

agents.append([random.randint(0,99),random.randint(0,99)])

print (agents)

#rinning the line of code whcih says agents [] as well as agents. append will change the specified co-ordinates
#running the agents.append will add new values onto the end of our agents tuple, while preserving the previous
#from left to right we have y0,x0,y1,x1

print(max(agents))

print(max(agents, key=operator.itemgetter(1)))
#this will get the co-ordinates with the max x value, remeber that 1 is the second element as containers are
#indexed from 0 and not 1. 

matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.scatter(agents[0][1],agents[0][0])
matplotlib.pyplot.scatter(agents[1][1],agents[1][0])
matplotlib.pyplot.show()
matplotlib.pyplot.scatter(agents[0][1], agents[0][0], color='red')
matplotlib.pyplot.scatter(agents[1][1],agents[1][0], color='blue')
#with the matplot co-ordinates [0][1] is saying row 1 column 2 and this is the x0
#with the matplot co-ordinates [0][0] is saying row 1 column 1 and this is the y0
#with the matplot co-ordinates [1][0] is saying row 2 column 2 and this is the x1
#with the matplot co-ordinates [1][1] is saying row 2 column 2 and this is the y1
#final segments of code colour the co-ordinate furthest east red and the one furthest west blue