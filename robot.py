# (10 points): As a developer, I want a Robot to have a name, health, and a Weapon (this needs to be its own class and object) with a name (i.e. sword) and attack power. 
# (5 points): As a developer, I want a Robot to have the ability to choose from a List of different weapons that will be then assigned as its own weapon.  

from weapon import Weapon

class Robot:
     
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.weapon = Weapon('', 0) 

    def robot_attack(self, targeted_dinosaur): 
        print('\nSelect which weapon you want to use for your robot:')
        print('"0" for "Laser Beam"')
        print('"1" for "Arm Blast"')
        user_select = int(input('"2" for "Missles": '))
        if user_select >= 0 and user_select <= 2:
            if user_select == 0:
                self.weapon = Weapon('Laser', 60)
            elif user_select == 1:
                self.weapon = Weapon('Blast', 50)
            elif user_select == 2:
                self.weapon = Weapon('Missle', 45) 
        elif user_select > 2 or user_select < 0:
            user_select = int(input('Invalid entry. Select a weapon to attack with: '))
        
        targeted_dinosaur.health -= self.weapon.attack_power

    
