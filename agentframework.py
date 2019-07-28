import random

#The Class controlling all agent behviours
class Agent: 
    #Initialises instances of Agent class, sets up y,x,environment and store
    #to be passed from the call
    def  __init__(self, y, x, environment, store=0):
        self._x = x
        self._y = y
        self.environment = environment
        self.store = store
           
    #Sets up x/y properties to conceal _x,_y in from the caller 
    def get_x(self):
        return self._x
    def get_y(self):
        return self._y
    def set_x(self, value):
        self._x = value
    def set_y(self, value):
        self._y = value     
    x = property(get_x, set_x)
    y = property(get_y, set_y)
    
    #Controls agent movement, recieves movement limitation from the call
    #which controls the boundaries for edge effect handling
    def move(self, yrange, xrange):
        yrange = yrange
        xrange = xrange
        if random.random() < 0.5:
            self.x = (self.x + 1) % xrange
        else:
            self.x = (self.x - 1) % xrange
        if random.random() < 0.5:
            self.y = (self.y + 1) % yrange
        else:
            self.y = (self.y - 1) % yrange
    
    #Controls eating behaviour
    def eat (self):
        #Default is for agents to eat n units per itteration, adding those
        #units to it's store and subtractng them from the enviroment location
        if self.environment[self.y][self.x] > 10:
            self.environment[self.y][self.x] -= 10
            self.store += 10
        else:
        #Overrides default unit consumtion, if enviroment has less than n units
        #agent is to eat remaining units. Adding the different amount to agents
        #store variable and setting the environment variable to 0
            self.store += self.environment[self.y][self.x]
            self.environment[self.y][self.x] = 0
    
    #Sets up behaviour to test the agent store level, when the store level
    #exceeds 100 the store is emptied to the environment.
    def vomit(self):
        if self.store > 100:
            self.environment[self.y][self.x] += self.store
            self.store = 0
    
    #Overides standard string function, to return the enviroment and store
    #value for each agent    
    def __str__(self):
        return "Environment=" + str(self.environment[self.y][self.x]) + \
    " ,Store=" + str(self.store)
    
    