import matplotlib.pyplot
import operator
import random


#Empty or define the beginning of an agents list, remember lists are immutable, this means they cannot be changed
agents = []     
#This is a variable and will store whatever value I put in
num_of_agents = 10
#This will store the number of times the process will be repeated
num_of_iterations = 100          
"""so below this is saying for i range (num_of_agents) print random agents 
up to 10 times from 0-9 as this is the number of agents specified"""
for i in range(num_of_agents):
    agents.append([random.randint(0,100),random.randint(0,100)])
    print (agents)
"""Running all of the above code in one will show the process of this"""

    
  """The code below means if random boolean is less than 1 add 1 and if greater than 0.5
subtract 1, this will be done for the number of iterations specified which in this case is 
100. Using the modulous symbol (return the remainder) means the value will be set to 0 if the calculation is greater than 99. This will prevent the Index out range error. """  
for j in range (num_of_iterations):
            for i in range(num_of_agents):
                  if random.random() < 0.5:
                   agents[i][0] = (agents[i][0] + 1) % 100
                  else:
                   agents[i][0] = (agents[i][0] - 1) % 100

                  if random.random() < 0.5:
                   agents[i][1] = (agents[i][1] + 1) % 100
                  else:
                   agents[i][1] = (agents[i][1] - 1) % 100



print(max(agents))
#finds the max agents based upon the first integer of the co-ordinates

print(max(agents, key=operator.itemgetter(1)))
#finds the max agents based upon the first integer of the co-ordinates


for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i][1], agents[i][0])
    matplotlib.pyplot.scatter(agents[i][1], agents[i][0])

matplotlib.pyplot.show()
"""plots and shows the co-ordinates of all generated agents in position 0 (so the first value in our pair of
co-ordinates) and position 1 (Our second value in our pair of co-ordinates), plotting using a for loop ensures
    that all co-ordinates are displayed on the map.""" 




#END OF CODE!!!!!
