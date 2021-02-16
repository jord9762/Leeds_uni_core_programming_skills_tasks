import matplotlib.pyplot
import operator
import random


#Below code can be used to empty or define the beginning of an agents list, remember lists are immutable, this means they cannot be changed
agents = []     
#Below is a variable and will store whatever value I put in
num_of_agents = 10
#This will store the number of times the process will be repeated
num_of_iterations = 100          
"""so below this is saying for i range (num_of_agents) print random agents 
up to 10 times from 0-9 as this is the number of agents specified"""
for i in range(num_of_agents):
    agents.append([random.randint(0,100),random.randint(0,100)])
    print (agents)


 """The code below is saying if random boolean is less than 0.5 add 1 and if greater than 0.5
subtract 1, this will be done for the number of iterations specified which in this case is 
100"""      
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

#maps all points as for i in range number of agents is used, remember [i][0] is the same as the y location and [i][1] is the x
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i][1], agents[i][0])
    matplotlib.pyplot.scatter(agents[i][1], agents[i][0])

matplotlib.pyplot.show()
"""plots and shows the co-ordinates of all generated agents in position 0 (so the first value in our pair of
co-ordinates) and position 1 (Our second value in our pair of co-ordinates), plotting using a for loop ensures
    that all co-ordinates are displayed on the map.""" 




#END OF CODE!!!!!


"""Final pointers:find out about what torus means 
  
