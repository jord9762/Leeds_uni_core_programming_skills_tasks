import random
import operator
import matplotlib.pyplot
import csv
import agentframework
import matplotlib.animation 
"""Note to visualise the code in this file the code %matplotlib qt must be inputted in to the ipython console first. Or alternatively
the code can be ran in the command prompt"""
environment = []
agents = []
num_of_agents = 10
num_of_iterations = 100
neighbourhood = 20

fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])

carry_on = True

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
    agents.append(agentframework.agent(environment, agents))   
 
def update(frame_number):
    
    fig.clear()   
    global carry_on
    
         
    
    # Move the agents.
    for j in range(num_of_iterations):
        for i in range(num_of_agents):
            agents[i].move()
            agents[i].eat()
            agents[i].share_with_neighbours(neighbourhood)
        
           
            
    #show agents on pyplot
    matplotlib.pyplot.xlim(0, 100)
    matplotlib.pyplot.ylim(0, 100)
    matplotlib.pyplot.imshow(environment)
    
    
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i]._x, agents[i]._y)


"""In the gen_function function we are assigning the number of iterations the animation will go through. a=0
means starting at 0 and carry_on while a =<10 leads to 10 iterations being called as the anmation will carry
on"""
def gen_function(b = [0]):
    store = 0
    global carry_on #Not actually needed as we're not assigning, but clearer
    while (store < 10) & (carry_on) :
        yield store			# Returns control and waits next call.
        store = store + 1

animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)


matplotlib.pyplot.show()

#Extras!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
"""below is an attempt to carry on with the animation until store reaches 10"""




def gen_function(b = [0]):
    a = 0
    global carry_on #Not actually needed as we're not assigning, but clearer
    while (a < 10) & (carry_on) :
        yield a			# Returns control and waits next call.
        a = a + 1


