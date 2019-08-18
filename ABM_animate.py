"""ABM
Created by Jamie Eames
Date of Last Update: 07/08/2019"""

import sys
import random
import matplotlib.pyplot
import agentframework
import csv
import matplotlib.animation 

"""For Testing Command Line Sys.Argv Functionality"""
sys.argv[1:] = [None,None,None,"True"]
sys.argv[1] = 10
sys.argv[2] = 100
sys.argv[3] = 30
sys.argv[4] = "True"

fig = matplotlib.pyplot.figure(figsize=(5, 5))
ax = fig.add_axes([0, 0, 1, 1])
carry_on = True

def distance_between(agents_row_a, agents_row_b):
    """Sets up the function to calulate the distance between each agent"""
    return (((agents_row_a.x - agents_row_b.x)**2)\
        + ((agents_row_a.y - agents_row_b.y)**2))**0.5
                
def update(frame_number):
    fig.clear()
    #Moves each agent a number of times
    for j in range(num_of_itterations):
        for i in range(num_of_agents):
            random.shuffle(agents)
            agents[i].move(yrange, xrange)
            agents[i].eat()
            agents[i].share_with_neighbours(neighbourhood)

    #Plots points and envronment in final arranngement
    matplotlib.pyplot.ylim(0, yrange)
    matplotlib.pyplot.xlim(0, xrange)
    matplotlib.pyplot.imshow(environment)
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i].x, agents[i].y)

def gen_function(b = [0]):
    a = 0
    global carry_on #Not actually needed as we're not assigning, but clearer
    while  (a < num_of_itterations) & (carry_on): 
        yield a			#: Returns control and waits next call.
        a = a + 1
        
if len(sys.argv) == 5:
    
    #Reads in an environment csv file, and transforms it into a 2D list
    data = open('in.txt')
    dataset = csv.reader(data, quoting=csv.QUOTE_NONNUMERIC, lineterminator='')
    environment = []
    for row in dataset:
        rowlist = []
        for value in row:
            rowlist.append(value)
        environment.append(rowlist)
    data.close()
    
    #Sets up envrioment size variables for use in chart plotter and
    #start location randomiser
    xrange = len(rowlist)-1
    yrange = len(environment)-1
    
    #Number of Agents Variable and itterations 
    try:
        num_of_agents = int(sys.argv[1])
    except ValueError:
        num_of_agents =\
        input('Please enter an integer for Number of Agents: ')

    try:
        num_of_itterations = int(sys.argv[2])
    except ValueError:
        num_of_itterations =\
        input('Please enter an integer for Number of Itterations: ')
    try:
        neighbourhood = int(sys.argv[3])
    except ValueError:
          neighbourhood =\
          int(input('Please enter an integer for Neighbourhood Size: '))

    #Agents List
    agents = []    
          
    #Generates a number of agents in random locations
    for i in range(num_of_agents):
        agents.append(agentframework.Agent(random.randint(0,yrange)\
        , random.randint(0,xrange), environment, agents, neighbourhood)) 

    
   
    #carry_on = True
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, interval=1, repeat=False)
    matplotlib.pyplot.show()
    
    #Saves final environment to png, appending the number of agents in the
    matplotlib.pyplot.ylim(0, yrange)
    matplotlib.pyplot.xlim(0, xrange)
    matplotlib.pyplot.imshow(environment)
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i].x, agents[i].y)
    matplotlib.pyplot.savefig('C:/GEOG5991/jamiee7.github.io/Images/agents-{}.jpg'.format(sys.argv[1]),  format="png")   
      
    #calculates distance between each point
    for agents_row_a in agents:
        for agents_row_b in agents:
            distance = distance_between(agents_row_a, agents_row_b)
    
    #Writes final enviroment to new file
    finalenvironment = open('finalenvironment.csv', 'w')
    writer = csv.writer(finalenvironment, delimiter = ',' , \
                        lineterminator='\n')
    for row in environment:
        writer.writerow(row)
    finalenvironment.close()
    
    #Writes agent store values to new file, appending a new line to the file
    #if it already exists on each subsequent exectuion
    agentstore = open('agentstore.csv', 'a')
    writestore = csv.writer(agentstore, delimiter=',', lineterminator='\n')
    storelist = []
    for i in range(num_of_agents):
        storelist.append(agents[i].store)
    writestore.writerow(storelist)
        
    agentstore.close()
    
    #Prints enviroment value at the location of each agent and the store value
    for i in range(num_of_agents):
        print(agents[i])

else:
    """Failure message if all arguements aren't returned"""
    print("""3 Arguments required: Number of Agents, Number of itterations
           , Neighbourhood Size. Each separated by a space.""")
    
