from weapon import Weapon

class Robot:
     
    def __init__(self, robot_name):
        self.robot_name = robot_name
        self.health = 100
        self.weapon = Weapon("Sword", 50)  

    def robot_attack(self, targeted_dinosaur): 
        targeted_dinosaur.health -= self.weapon.attack_power #tentative need to evaluate
