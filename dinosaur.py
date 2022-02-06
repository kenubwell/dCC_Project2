#(10 points): As a developer, I want a Dinosaur to have a name, health, and attack power.  
#(5 points): As a developer, I want a Dinosaur to have the ability to choose its attack name from a tuple of different attack names before attacking a Robot in battle. 

class Dinosaur:
     
    def __init__(self, name, attack_power):
        self.name = name
        self.health = 100
        self.attack_power = attack_power

    def dino_attack(self, targeted_robot):
        attack_tuple = ("Smash", "Bite", "Stomp")

        print('\nSelect which attach method to use:')
        print(f'Press "0" for "{attack_tuple[0]}"')
        print(f'Press "1" for "{attack_tuple[1]}"')
        user_select = int(input(f'Press "2" for "{attack_tuple[2]}": '))
        if user_select >= 0 and user_select <= 2:
            if user_select == 0:
                self.attack_power = 55
            elif user_select == 1:
                self.attack_power = 50
            elif user_select == 2:
                self.attack_power = 45 
        elif user_select > 2 or user_select < 0:
            user_select = int(input('Invalid entry. Re-select an attack method: '))

        targeted_robot.health -= self.attack_power
