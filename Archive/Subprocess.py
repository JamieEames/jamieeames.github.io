"""ABM Subprocess Run
Created by Jamie Eames
Date of Last Update: 07/08/2019

Runs ABM Program N times, and records the running time of each cycle;
plotting all running times vs agent numbers
"""

import subprocess
import time
import matplotlib.pyplot


base = 10
counter = 0
increment = 10
file = "ABM.py"
itterations = "100"
neighbourhood = "30"
mapper = "True"
times = []
agentslist = []
runs = 10


for i in range (0,runs):
    start = time.perf_counter()
    agents = base+(counter*increment)
    agentslist.append(agents)
    agentsstr = str(agents)
    subprocess.call([file, agentsstr, itterations, neighbourhood, mapper]\
                    , shell = True)
    counter += 1
    
    end = time.perf_counter()
    times.append(end-start)

print(len(agentslist))


matplotlib.pyplot.plot(agentslist, times,linestyle ='-', color = 'black'\
                       , marker = 'x', mec = 'red', markersize=10.0)
matplotlib.pyplot.savefig('C:/GEOG5991/jamiee7.github.io/Images/times.png', format="png")
matplotlib.pyplot.show()