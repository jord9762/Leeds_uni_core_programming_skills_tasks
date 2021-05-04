import random
import operator
import matplotlib.pyplot
#specifies the number of agents which will be created for the variable num_of_agents
num_of_agents = 10
#specifies the number of iterations or in other words the amount of times the code will be run
num_of_iterations = 100
#creates an empty list for agents
agents = []

# Make the agents. Creates 10 agents randomly. .Append adds element to the end of the list. 
for i in range(num_of_agents):
    agents.append([random.randint(0,99),random.randint(0,99)])

# Move the agents.
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

'''
answer = (((agents[0][0] - agents[1][0])**2) + ((agents[0][1] - agents[1][1])**2))**0.5
print(answer)
'''
#plots agents on a pyplot, this is done for all agents with the foor loop present on line 37. [i][1] represents the Y of the agents co-ordinate and [i][0] represents the X.
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)

for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i][1],agents[i][0])
    #code on line 40 plots the agents created in this script
matplotlib.pyplot.show()
