from robot import Robot

class Fleet:
     
    def __init__(self):   # make a fleet on battlefield fleet = Fleet()
        self.robots = []

    def create_fleet(self): # call this method to "assemble" our robots , make 3 object and append them to the list above
        robot_one = Robot('Ultron')
        robot_two = Robot('Vision')
        robot_three = Robot('Nimrod')

        self.robots = [robot_one, robot_two, robot_three]