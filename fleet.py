#(10 points): As a developer, I want to instantiate three Robot objects and three Dinosaur objects and assign the appropriate values to all the objects. 
#(10 points): As a developer, I want the created Robot objects to be stored in a Fleet and the created Dinosaur objects to be stored in a Herd 
    # (the Fleet and Herd must use a List to store the objects). 

from robot import Robot

class Fleet:
     
    def __init__(self):   
        self.robots = []
        self.create_fleet()

    def create_fleet(self): 
        robot_one = Robot('Ultron')
        robot_two = Robot('Vision')
        robot_three = Robot('Nimrod')

        self.robots = [robot_one, robot_two, robot_three]
