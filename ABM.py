import random
import operator
import matplotlib.pyplot

#Agents List
agents = []

agents.append([random.randint(0,99),random.randint(0,99)]) #adds x0 and y0 to agents


#Generates a ramdon number and checks the value
#if less than 0.5, 1 is added to y0
#otherwise 1 is subtracted from y0
if random.random() < 0.5: #random.random() replaces ramdon_number
    agents[0][0] += 1
else:
    agents[0][0] -=1

#above codeblock repeated for x0
if random.random() < 0.5: #random.random() replaces ramdon_number
    agents[0][1] += 1
else:
    agents[0][1] -=1

#repeat step
if random.random() < 0.5: #random.random() replaces ramdon_number
    agents[0][0] += 1
else:
    agents[0][0] -=1

#above codeblock repeated for x0
if random.random() < 0.5: #random.random() replaces ramdon_number
    agents[0][1] += 1
else:
    agents[0][1] -=1

#creates variables y0/x0
#and assigns ramdom start values between 0 and 99
agents.append([random.randint(0,99),random.randint(0,99)]) #adds x0 and y0 to agents

#Generates a ramdon number and checks the value
#if less than 0.5, 1 is added to y1
#otherwise 1 is subtracted from y1
if random.random() < 0.5: #random.random() replaces ramdon_number
    agents[1][0] += 1
else:
    agents[1][0] -=1

#above codeblock repeated for x0
if random.random() < 0.5: #random.random() replaces ramdon_number
    agents[1][1] += 1
else:
    agents[1][1] -=1

#repeat step
if random.random() < 0.5: #random.random() replaces ramdon_number
    agents[1][0] += 1
else:
    agents[1][0] -=1

#above codeblock repeated for x0
if random.random() < 0.5: #random.random() replaces ramdon_number
    agents[1][1] += 1
else:
    agents[1][1] -=1
    
print(agents)

#Calculate distance between xy0/xy1
distance = (((agents[0][0]-agents[1][0])**2) + ((agents[0][1]-agents[1][1])**2))**0.5
print(distance)

#Print the coord pair with the highest index 1 (X-Coord east) value

###
eastmost = max(agents, key=operator.itemgetter(1))
###########All below may need altering if the tutor says so, then revert to plotting each point.#########
noteastmost = agents
del noteastmost[noteastmost.index(eastmost)]
notestmostsingle = noteastmost[0]


###Plots points, with the most Eastern in Red
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.scatter(notestmostsingle[1],notestmostsingle[0])
matplotlib.pyplot.scatter(eastmost[1], eastmost[0], color='red')
matplotlib.pyplot.show()
