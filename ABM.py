import random
import operator
import matplotlib.pyplot
import agentframework
import csv

def distance_between(agents_row_a, agents_row_b):
        return (((agents_row_a.x - agents_row_b.x)**2)\
                + ((agents_row_a.y - agents_row_b.y)**2))**0.5

data = open('in.txt', newline='')
dataset = csv.reader(data, quoting=csv.QUOTE_NONNUMERIC)

environment = []

for row in dataset:
    rowlist = []
    for value in row:
        rowlist.append(value)
    environment.append(rowlist)
data.close()

matplotlib.pyplot.imshow(environment)
matplotlib.pyplot.show()

#Number of Agents Variable
num_of_agents = 100
num_of_itterations = 1000

#Agents List
agents = []

#Generates a number of agents in random locations
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment))  

#Moves each agent a number of times
for j in range(num_of_itterations):
    for i in range(num_of_agents): 
        agents[i].move()
        agents[i].eat()
        #agents[i].vomit()

###Plots points, with the most Eastern in Red
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.imshow(environment)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i].x, agents[i].y)
matplotlib.pyplot.show()

for agents_row_a in agents:
    for agents_row_b in agents:
        distance = distance_between(agents_row_a, agents_row_b)
        
finalenvironment = open('finalenvironment.csv', 'w', newline = '')
writer = csv.writer(finalenvironment, delimiter = ',')
for row in environment:
    writer.writerow(row)
finalenvironment.close()


agentstore = open('agentstore.csv', 'a', newline = '')
writestore = csv.writer(agentstore, delimiter=',')
storelist = []
for i in range(num_of_agents):
    storelist.append(agents[i].store)
writestore.writerow(storelist)
    
agentstore.close()

for i in range(num_of_agents):
    print(agents[i], end='\n')