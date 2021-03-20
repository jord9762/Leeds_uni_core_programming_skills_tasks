import random

"""https://www.youtube.com/watch?v=oE_dWWWqxQ0 init behaves like a contructor for the class agent. """
class agent:
    def __init__(self):
        self._y = random.randint(0, 99)
        self._x = random.randint(0, 99)

    # Getters and Setters for x and y properties
   
    def get_x(self):
        """getter for x."""
        return self._x
      
    
    @get_x.setter
    def set_x(self, value):
        """setter for X."""
      
        
    @property
    def get_y(self):
        """getter for Y."""
        return self._y
   
    @get_y.setter
    def set_y(self, value):
        """setter for Y."""
      
       
     

    def move(self):
        if random.random() < 0.5:
            self._y = (self._y + 1) % 100
        else:
            self._y = (self._y - 1) % 100

        if random.random() < 0.5:
            self._x = (self._x + 1) % 100
        else:
            self._x = (self._x - 1) % 100

   
    



            
