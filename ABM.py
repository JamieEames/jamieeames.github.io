"""ABM
Created by Jamie Eames
Date of Last Update: 28/07/2019"""


import random
import matplotlib.pyplot
import agentframework
import csv

def distance_between(agents_row_a, agents_row_b):
    """Sets up the function to calulate the distance between each agent"""
    return (((agents_row_a.x - agents_row_b.x)**2)\
    + ((agents_row_a.y - agents_row_b.y)**2))**0.5

#Reads in an environment csv file, and transforms it into a 2D list
data = open('in.txt', newline='')
dataset = csv.reader(data, quoting=csv.QUOTE_NONNUMERIC)
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
num_of_agents = 10
num_of_itterations = 100

#Agents List
agents = []

#Generates a number of agents in random locations
for i in range(num_of_agents):
    agents.append(agentframework.Agent(random.randint(0,yrange)\
    , random.randint(0,xrange), environment)) 
   
#Moves each agent a number of times
for j in range(num_of_itterations):
    for i in range(num_of_agents): 
        agents[i].move(yrange, xrange)
        agents[i].eat()
        agents[i].vomit()

#Plots points and envronment in final arranngement
matplotlib.pyplot.ylim(0, yrange)
matplotlib.pyplot.xlim(0, xrange)
matplotlib.pyplot.imshow(environment)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i].x, agents[i].y)
matplotlib.pyplot.show()

#calculates distance between each point
for agents_row_a in agents:
    for agents_row_b in agents:
        distance = distance_between(agents_row_a, agents_row_b)

#Writes final enviroment to new file
finalenvironment = open('finalenvironment.csv', 'w', newline = '')
writer = csv.writer(finalenvironment, delimiter = ',')
for row in environment:
    writer.writerow(row)
finalenvironment.close()

#Writes agent store values to new file, appending a new line to the file
#if it already exists on each subsequent exectuion
agentstore = open('agentstore.csv', 'a', newline = '')
writestore = csv.writer(agentstore, delimiter=',')
storelist = []
for i in range(num_of_agents):
    storelist.append(agents[i].store)
writestore.writerow(storelist)
    
agentstore.close()

#Prints enviroment value at the location of each agent and the store value
for i in range(num_of_agents):
    print(agents[i], end='\n')
