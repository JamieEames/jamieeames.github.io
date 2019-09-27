"""ABM
Created by Jamie Eames
Date of Last Update: 07/08/2019"""
import sys
import random
import matplotlib
matplotlib.use('TkAgg')
import tkinter
import matplotlib.pyplot
import agentframework
import csv
import matplotlib.animation 

"""For Testing Command Line Sys.Argv Functionality"""
num_of_agents = 10
num_of_itterations = 100
neighbourhood = 30


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

#Agents List
agents = []    
      
#Generates a number of agents in random locations
def run():
    for i in range(num_of_agents):
        agents.append(agentframework.Agent(random.randint(0,yrange)\
        , random.randint(0,xrange), environment, agents, neighbourhood)) 
    
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, interval=1, repeat=False)
    canvas.draw()
    
root = tkinter.Tk()
root.wm_title("Model")
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command=run)
   
tkinter.mainloop()


