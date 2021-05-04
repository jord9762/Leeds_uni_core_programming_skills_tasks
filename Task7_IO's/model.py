import random
import operator
import matplotlib.pyplot
import csv
import agentframework
import os
import sys


environment = []
agents = []
num_of_agents = 10
num_of_iterations = 100



f = open('in.csv', newline='')
#Note that the correct directory must be navigated to in the terminal else the full file path will be needed
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
for row in reader: # A list of rows
    rowlist = []
    for value in row: # A list of value
     rowlist.append(value)
     environment.append(rowlist)
    
     
# Make the agents.
for i in range(num_of_agents):
    agents.append(agentframework.agent(environment))

#check agents
for i in range(num_of_agents):
   print(agents[i])    

# Move the agents.
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat()
    
        
        

matplotlib.pyplot.xlim(0, 100)
matplotlib.pyplot.ylim(0, 100)
matplotlib.pyplot.imshow(environment)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i]._x, agents[i]._y)
matplotlib.pyplot.show()
#Extras!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
f = open("in.csv", "r")
print(f.read())





"""Final thoughts: since environment has been defined in agents __init__(self,environment) we are able to 
move the environmental data the same way in which we would move the agents. I expanded the matplot axes 
in order to visualise the full breadth of the data"""

""" I think the previous plot code matplotlib.pyplot.imshow(environment)
matplotlib.pyplot.show() plotted the data but in a linear fashion rather than an X/Y grid and that's why the 
plot output looked odd"""


