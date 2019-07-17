import random
import operator
import matplotlib.pyplot

#Number of Agents Variable
num_of_agents = 10
num_of_itterations = 100

#Agents List
agents = []


#Generates a number of agents in random locations
for i in range(num_of_agents):
    agents.append([random.randint(0,99),random.randint(0,99)])  

#Moves each agent a number of times
for i in range(num_of_agents):
    for j in range(num_of_itterations): 
        if random.random() < 0.5:
            agents[i][0] = (agents[i][0] + 1) % 100
        else:
            agents[i][0] = (agents[i][0] - 1) % 100
        if random.random() < 0.5:
            agents[i][1] = (agents[i][1] + 1) % 100
        else:
            agents[i][1] = (agents[i][1] - 1) % 100

#Calculate distance between xy0/xy1
##distance = (((agents[0][0]-agents[1][0])**2) + ((agents[0][1]-agents[1][1])**2))**0.5
##print(distance)

#Print the coord pair with the highest index 1 (X-Coord east) value

###
##eastmost = max(agents, key=operator.itemgetter(1))
###########All below may need altering if the tutor says so, then revert to plotting each point.#########
##noteastmost = agents
##del noteastmost[noteastmost.index(eastmost)]
##notestmostsingle = noteastmost[0]


###Plots points, with the most Eastern in Red
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i][1],agents[i][0])
##matplotlib.pyplot.scatter(notestmostsingle[1],notestmostsingle[0])
##matplotlib.pyplot.scatter(eastmost[1], eastmost[0], color='red')
matplotlib.pyplot.show()
