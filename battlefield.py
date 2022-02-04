#(10 points): As a developer, I want a Robot to have the ability to attack a Dinosaur and a Dinosaur to have the ability to attack a Robot on a Battlefield. 
#(10 points): As a developer, I want a Robot/Dinosaur to lose health points (loss based on attack power) when another Robot/Dinosaur successfully attacks it. 


from fleet import Fleet
from herd import Herd
import random

class Battlefield:
     
    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()

    def run_game(self): 
        self.display_welcome()
        self.battle()
        self.display_winners()

    def display_welcome(self):
        print('Welcome to "Machines vs. Extinct Animals" a.k.a. "Robots vs. Dinosaurs". The following are the rules of the game:') 
        print('Each side entails a team of three. The three Robots are a "Fleet" and the three Dinosaurs are a "Herd".') 
        print(f'Fleet Team: "{self.fleet.robots[0].name}", "{self.fleet.robots[1].name}", "{self.fleet.robots[2].name}"') 
        print(f'Herd Team: "{self.herd.dinosaurs[0].name}", "{self.herd.dinosaurs[1].name}", "{self.herd.dinosaurs[2].name}"') 
        print("Each robot and dinosaur has a 100 health and health gradually decreases per attack. You'll get to select attackers on both sides and turns are random.")
        print('A winner is declared when all three Robots or three Dinosaurs health reach "0" or below. Let us begin! \n')

    def battle(self):
        match_off = False

        while match_off is False:
            turn = random.randint(1,2)
            if turn == 1:
                if (self.herd.dinosaurs[0].health > 0 or self.herd.dinosaurs[1].health > 0 or self.herd.dinosaurs[2].health > 0) and (self.fleet.robots[0].health > 0 or self.fleet.robots[1].health > 0 or self.fleet.robots[2].health > 0):
                    self.robo_turn()
                elif self.herd.dinosaurs[0].health <= 0 and self.herd.dinosaurs[1].health <= 0 and self.herd.dinosaurs[2].health <= 0:
                    match_off = True        
            elif turn == 2:
                if (self.fleet.robots[0].health > 0 or self.fleet.robots[1].health > 0 or self.fleet.robots[2].health > 0) and (self.herd.dinosaurs[0].health > 0 or self.herd.dinosaurs[1].health > 0 or self.herd.dinosaurs[2].health > 0):
                    self.dino_turn()
                elif self.fleet.robots[0].health <= 0 and self.fleet.robots[1].health <= 0 and self.fleet.robots[2].health <= 0:
                    match_off = True      
        return match_off
        

    def dino_turn(self): #for loops
        dinosaur = self.show_dino_opponent_options()
        if self.fleet.robots[0].health > 0:
            self.herd.dinosaurs[dinosaur].dino_attack(self.fleet.robots[0])
            print(f'You hit {self.fleet.robots[0].name} and its health is now {self.fleet.robots[0].health}!\n')
        elif self.fleet.robots[1].health > 0:
            self.herd.dinosaurs[dinosaur].dino_attack(self.fleet.robots[1])
            print(f'You hit {self.fleet.robots[1].name} and its health is now {self.fleet.robots[1].health}!\n')
        elif self.fleet.robots[2].health > 0:
            self.herd.dinosaurs[dinosaur].dino_attack(self.fleet.robots[2])
            print(f'You hit {self.fleet.robots[2].name} and its health is now {self.fleet.robots[2].health}!\n')

    def robo_turn(self): #for loops
        robot = self.show_robo_opponent_options()
        if self.herd.dinosaurs[0].health > 0:
            self.fleet.robots[robot].robot_attack(self.herd.dinosaurs[0])
            print(f'You hit {self.herd.dinosaurs[0].name} and its health is now {self.herd.dinosaurs[0].health}!\n')
        elif self.herd.dinosaurs[1].health > 0:
            self.fleet.robots[robot].robot_attack(self.herd.dinosaurs[1])
            print(f'You hit {self.herd.dinosaurs[1].name} and its health is now {self.herd.dinosaurs[1].health}!\n')
        elif self.herd.dinosaurs[2].health > 0:
            self.fleet.robots[robot].robot_attack(self.herd.dinosaurs[2])
            print(f'You hit {self.herd.dinosaurs[2].name} and its health is now {self.herd.dinosaurs[2].health}!\n')
  

    def show_dino_opponent_options(self):
        user_select = 0
        confirmed_select = 0
        selection = False

        print('Current Dinosaur Herd:')
        print(f'Press "0" to select {self.herd.dinosaurs[0].name} ({self.herd.dinosaurs[0].health} health)')
        print(f'Press "1" to select {self.herd.dinosaurs[1].name} ({self.herd.dinosaurs[1].health} health)')
        print(f'Press "2" to select {self.herd.dinosaurs[2].name} ({self.herd.dinosaurs[2].health} health)')
        user_select = int(input('Select a dinosaur for your attack: '))
        
        while selection is False:
            if self.herd.dinosaurs[user_select].health > 0:
                confirmed_select = user_select
                selection = True
            elif self.herd.dinosaurs[user_select].health <= 0:
                print('Your Dino is already re-extinct (dead). Please select another Dino.')
                user_select = int(input('Select another robot for your attack: '))
        return confirmed_select

    def show_robo_opponent_options(self):
        user_select = 0
        confirmed_select = 0
        selection = False

        print('Current Robot Fleet:')
        print(f'Press "0" to select {self.fleet.robots[0].name} ({self.fleet.robots[0].health} health)')
        print(f'Press "1" to select {self.fleet.robots[1].name} ({self.fleet.robots[1].health} health)')
        print(f'Press "2" to select {self.fleet.robots[2].name} ({self.fleet.robots[2].health} health)')
        user_select = int(input('Select a robot for your attack: '))
        while selection is False:
            if self.fleet.robots[user_select].health > 0:
                confirmed_select = user_select
                selection = True
            elif self.fleet.robots[user_select].health <= 0:
                print('Your Robot is already demolished (dead). Please select another Robot.')
                user_select = int(input('Select another robot for your attack: '))
        return confirmed_select

    def display_winners(self):
        if (self.fleet.robots[0].health <= 0 and self.fleet.robots[1].health <= 0 and self.fleet.robots[2].health <= 0):
            print('The Extinct Animals Won! (a.k.a. Dinosaurs)')
            print(f'Destruction Summary: "{self.fleet.robots[0].name}" ({self.fleet.robots[0].health} health), "{self.fleet.robots[1].name}" ({self.fleet.robots[1].health} health), "{self.fleet.robots[2].name}" ({self.fleet.robots[2].health} health).')
        elif (self.herd.dinosaurs[0].health <= 0 and self.herd.dinosaurs[1].health <= 0 and self.herd.dinosaurs[2].health <= 0):
            print('The Machines Won! (a.k.a. the Robots)')
            print(f'Extinction Summary: "{self.herd.dinosaurs[0].name}" ({self.herd.dinosaurs[0].health} health), "{self.herd.dinosaurs[1].name}" ({self.herd.dinosaurs[1].health} health), "{self.herd.dinosaurs[2].name}" ({self.herd.dinosaurs[2].health} health).')


    