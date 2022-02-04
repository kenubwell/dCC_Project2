from weapon import Weapon

class Robot:
     
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.weapon = Weapon("Sword", 50)  # all robots will be made with a sword


    def robot_attack(self, targeted_dinosaur): 
        targeted_dinosaur.health -= self.weapon.attack_power

    