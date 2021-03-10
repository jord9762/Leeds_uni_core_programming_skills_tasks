import random
import operator
import matplotlib.pyplot
import agentframework


def distance_between(agents_row_a, agents_row_b):
    return (((agents_row_a.get_x() - agents_row_b.get_x())**2) +
            ((agents_row_a.get_y() - agents_row_b.get_y())**2))**0.5


num_of_agents = 10
num_of_iterations = 100
agents = []

# Make the agents.
for i in range(num_of_agents):
    agents.append(agentframework.Agent())

# Move the agents.
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        a = agents[i]
        print("Original", a.get_y(), a.get_x()) # using getter to get the x and y values of the object
        a.move()
        print("Moved: ", a.get_y(), a.get_x())

matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.ylim(0, 99)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i].get_x(), agents[i].get_y())
matplotlib.pyplot.show()

for agents_row_a in agents:
    for agents_row_b in agents:
        distance = distance_between(agents_row_a, agents_row_b)
        
    