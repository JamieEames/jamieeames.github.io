import random
import operator
import matplotlib.pyplot
import time

def distance_between(agents_row_a, agents_row_b):
        return (((agents_row_a[0] - agents_row_b[0])**2)\
                + ((agents_row_a[1] - agents_row_b[1])**2))**0.5

#timings =[]
#powers = [0,1,2,3]
#for i in powers:
    
#    start = time.clock()
    #Number of Agents Variable
num_of_agents = 10#**i
   # agentslable = "10" + "^" + str(i)
num_of_itterations = 10

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

distances = []
for agents_row_a in agents:
    for agents_row_b in agents:
        if agents_row_a > agents_row_b or agents_row_a == agents_row_b:
            continue
        distances.append(distance_between(agents_row_a, agents_row_b))

print("Min Dist = ",min(distances))
print("Max Dist = ",max(distances))

#print(min(distance))
#    end = time.clock()
#    timings.append(end-start)
#
#print(timings)
#
#for i in powers:
#    matplotlib.pyplot.scatter(powers[i], timings[i])
###matplotlib.pyplot.scatter(notestmostsingle[1],notestmostsingle[0])
###matplotlib.pyplot.scatter(eastmost[1], eastmost[0], color='red')
#matplotlib.pyplot.show()
