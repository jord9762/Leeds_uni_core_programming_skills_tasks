import random

"""init behaves like a constructor for the class agent. Adding additional arguments after self requires 
specification of values otherwise an error will show up claiming positional arguments are missing. Self is automatically provided for the 
class. Look here for more info on self: https://www.youtube.com/watch?v=AjYOMk-4NIU"""
class agent:
    #object being created
    def __init__(self):
        self._y = random.randint(0, 99)
        self._x = random.randint(0, 99)
        

    # Getters and Setters for x and y properties
   
    def get_x(self):
        """getter for x."""
        return self._x
      
    
   
    def set_x(self, value):
        """setter for X."""
      
        
  
    def get_y(self):
        """getter for Y."""
        return self._y
   
    
    def set_y(self, value):
        """setter for Y."""
      
       
     

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

   
    



            
