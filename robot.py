# (10 points): As a developer, I want a Robot to have a name, health, and a Weapon (this needs to be its own class and object) with a name (i.e. sword) and attack power. 

from weapon import Weapon

class Robot:
     
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.weapon = Weapon('Laser', 60) 

    def robot_attack(self, targeted_dinosaur): 
        targeted_dinosaur.health -= self.weapon.attack_power

    
