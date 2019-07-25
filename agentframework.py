import random


class Agent:
#    def  __init__(self):
#       self.x = random.randint(0,99)
#       self.y = random.randint(0,99)
#       
#    def move(self):
#        if random.random() < 0.5:
#            self.x = (self.x + 1) % 100
#        else:
#            self.x = (self.x - 1) % 100
#        if random.random() < 0.5:
#            self.y = (self.y + 1) % 100
#        else:
#            self.y = (self.y - 1) % 100
    
    def  __init__(self):
           self._x = random.randint(0,99)
           self._y = random.randint(0,99)
       
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
    
    def move(self):
        if random.random() < 0.5:
            self.x = (self.x + 1) % 100
        else:
            self.x = (self.x - 1) % 100
        if random.random() < 0.5:
            self.y = (self.y + 1) % 100
        else:
            self.y = (self.y - 1) % 100