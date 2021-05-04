import random


class agent:
    
    def __init__(self,environment):
        self._y = random.randint(0, 99)
        self._x = random.randint(0, 99)
        self.environment = environment
        self.store = 0 
        
        
        
    def __str__(self):
        return "x=" + str(self._x) + ", y=" + str(self._y) + ", store=" + str(self.store)

    # Getters and Setters for x and y properties
    def get_x(self):
        return self._x
         
    
    
    def set_x(self, value):
        """setter for X."""
        self._x = value
        
    
    def get_y(self):
        """getter for Y."""
        return self._y
   
    
    def set_y(self, value):
        """setter for Y."""
        self._y = value


    def move(self):
        """
        Moves the x and y variables or agents using the random library features
        -------
        None.

        """
        if random.random() < 0.5:
            self._y = (self._y + 1) % 100
        else:
            self._y = (self._y - 1) % 100

        if random.random() < 0.5:
            self._x = (self._x + 1) % 100
        else:
            self._x = (self._x - 1) % 100

    value=property(get_x,set_x,get_y,set_y)
    print(value)
    
 #https://www.youtube.com/watch?v=AEOuYv699K4&t=26s this assisted with understanding property, although still 
#unsure on the functionality, will revisit later.   
    def eat(self): # can you make it eat what is left?
        if self.environment[self._y][self._x] > 10:
            self.environment[self._y][self._x] -= 10
            self.store += 10

            

    