import random



class agent:
    
    
    def __init__(self,environment,agents):
        self._y = random.randint(0, 99)
        self._x = random.randint(0, 99)
        self.environment = environment
        self.agents = agents
        self.store = 0
        
        
    def __str__(self):
        """
        

        Returns
        -------
        This will print the agents x and y co-ordinates once the iteration process is complete. str(self.store) allows the store value to be
        printed at each iteration.

        """
        return "x=" + str(self._x) + ", y=" + str(self._y) + ", store=" + str(self.store)

    # Getters and Setters for x and y properties
    
    def get_x(self):
        """
        

        Returns
        -------
        TYPE
             getter for x.

        """
       
        return self._x
        property(fget=self._x) 
    
    
    def set_x(self, value):
        """
        

        Parameters
        ----------
        value : TYPE
            setter for x

        Returns
        -------
        None.

        """
        self._x = value
     
   
    def get_y(self):
        return self._y

    
    def set_y(self, value):
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

    
    
  
    def eat(self): 
        if self.environment[self._y][self._x] > 10:
            self.environment[self._y][self._x] -= 10
            self.store += 10
            
            
    def share_with_neighbours(self, neighbourhood):
     random.shuffle(self.agents)
     for agent in self.agents:
        dist = self.distance_between(agent)
        if dist <= neighbourhood:
            sum = self.store + agent.store
            ave = sum /2
            self.store = ave
            agent.store = ave
            print("sharing " + str(dist) + " " + str(ave))

    def distance_between(self, agent):
       return (((self._x - agent._x)**2) + ((self._y - agent._y)**2))**0.5
        

            

    