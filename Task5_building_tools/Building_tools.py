import random
import operator
import matplotlib.pyplot
import time
def distance_between(agents_row_a, agents_row_b):
    return (((agents_row_a[0] - agents_row_b[0])**2) + ((agents_row_a[1] - agents_row_b[1])**2))**0.5
"""we enter in agents row a and row b because this reduces our code for when the function is called, we now no longer need to express an agent 
as ([0][1],[0][0]) and we can now express in the more logical [0] and [1]"""
start = time.clock()
num_of_agents = 10
num_of_iterations = 100
agents = []

# Make the agents.
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


answer = (((agents[0][0] - agents[1][0])**2) + ((agents[0][1] - agents[1][1])**2))**0.5
print(answer)

"""answer = (((agents[2][0] - agents[3][0])**2) + ((agents[0][1] - agents[1][1])**2))**0.5
print(answer) could get distance between different agents individually but obviously this would be very inefficent"""


matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i][1],agents[i][0])
matplotlib.pyplot.show()
"""The code below will print the distance between agent 0 and agent 1 which in this case is [67,55] and [6, 85], this will change due to the
pseudo random nature in which agents are generated."""

answer = distance_between(agents[0], agents[1])
print(answer)
"""so below here we are saying for everything i and j in our agents, do not calculate distance between the same agent, then calculate the distance
in positions 0 and 1 using the function specified at the start of our code in the distance between function."""

"""You can test to see if the outputs are correct manually using the pythagoras equation found in model.py"""

"""Note that code must be ran on lines 56 to 62 in order to get the distance between each of the respective distances between each agent"""
for i in range(num_of_agents):
    for j in range(num_of_agents):

        if agents[i] != agents[j]: # omitts distance between agents which are the same
            distance = distance_between(agents[0], agents[1])
            answer = distance_between(agents[i], agents[j])
            print(answer)
            #(max(str(answer)))  tried something like this to get max but didn't work
            

print (agents)         
end = time.clock()
print("time = " + str(end - start))
"""Time for 10 agents 0.15 seconds
Time for 100 agents 1.52 seconds
Time for 1000 agents 114 seconds """


"""Remember lines 56 to 62 will get the agents distance between all the agents providing agents are created"""