#(10 points): As a developer, I want a Robot to have the ability to attack a Dinosaur and a Dinosaur to have the ability to attack a Robot on a Battlefield. 
#(10 points): As a developer, I want a Robot/Dinosaur to lose health points (loss based on attack power) when another Robot/Dinosaur successfully attacks it. 


from fleet import Fleet
from herd import Herd
import random


class Battlefield:
     
    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()

    #the method that runs the entire game (from other methods)
    def run_game(self): 
        self.display_welcome()
        self.battle()
        self.display_winners()

    #a method to display a Welcome and Intro to the game
    def display_welcome(self):
        print('Welcome to "Machines vs. Extinct Animals" a.k.a. "Robots vs. Dinosaurs". The following are the rules of the game:') 
        print('Each side entails a team of three. The three Robots are a "Fleet" and the three Dinosaurs are a "Herd".') 
        print(f'Fleet Team: "{self.fleet.robots[0].name}", "{self.fleet.robots[1].name}", "{self.fleet.robots[2].name}"') 
        print(f'Herd Team: "{self.herd.dinosaurs[0].name}", "{self.herd.dinosaurs[1].name}", "{self.herd.dinosaurs[2].name}"') 
        print("Each robot and dinosaur has a 100 health and health gradually decreases per attack. You'll get to select attackers and attack method for both sides.")
        print('Please note that turns are RANDOM. A winner is declared when all three Robots or three Dinosaurs health reach "0". Let us begin! \n')

    #a method to initiate the battle
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
        
    #a method for the dinosaurs turn and which robot to attack
    def dino_turn(self): 
        dinosaur = self.show_dino_opponent_options()
        negative_health_to_zero = 0

        if self.fleet.robots[0].health > 0:
            self.herd.dinosaurs[dinosaur].dino_attack(self.fleet.robots[0])
            if self.fleet.robots[0].health < 0:
                print(f'\nYou hit {self.fleet.robots[0].name} and its health is now {negative_health_to_zero}!\n')
            else:
                print(f'\nYou hit {self.fleet.robots[0].name} and its health is now {self.fleet.robots[0].health}!\n')
        elif self.fleet.robots[1].health > 0:
            self.herd.dinosaurs[dinosaur].dino_attack(self.fleet.robots[1])
            if self.fleet.robots[1].health < 0:
                print(f'\nYou hit {self.fleet.robots[1].name} and its health is now {negative_health_to_zero}!\n')
            else:
                print(f'\nYou hit {self.fleet.robots[1].name} and its health is now {self.fleet.robots[1].health}!\n')
        elif self.fleet.robots[2].health > 0:
            self.herd.dinosaurs[dinosaur].dino_attack(self.fleet.robots[2])
            if self.fleet.robots[2].health < 0:
                print(f'\nYou hit {self.fleet.robots[2].name} and its health is now {negative_health_to_zero}!\n')
            else:
                print(f'\nYou hit {self.fleet.robots[2].name} and its health is now {self.fleet.robots[2].health}!\n')

    #a method for the robots turn and which dinosaur to attack
    def robo_turn(self): 
        robot = self.show_robo_opponent_options()
        negative_health_to_zero = 0

        if self.herd.dinosaurs[0].health > 0:
            self.fleet.robots[robot].robot_attack(self.herd.dinosaurs[0])
            if self.herd.dinosaurs[0].health < 0:
                print(f'\nYou hit {self.herd.dinosaurs[0].name} and its health is now {negative_health_to_zero}!\n')
            else:
                print(f'\nYou hit {self.herd.dinosaurs[0].name} and its health is now {self.herd.dinosaurs[0].health}!\n')
        elif self.herd.dinosaurs[1].health > 0:
            self.fleet.robots[robot].robot_attack(self.herd.dinosaurs[1])
            if self.herd.dinosaurs[1].health < 0:
                print(f'\nYou hit {self.herd.dinosaurs[1].name} and its health is now {negative_health_to_zero}!\n')
            else:
                print(f'\nYou hit {self.herd.dinosaurs[1].name} and its health is now {self.herd.dinosaurs[1].health}!\n')
        elif self.herd.dinosaurs[2].health > 0:
            self.fleet.robots[robot].robot_attack(self.herd.dinosaurs[2])
            if self.herd.dinosaurs[2].health < 0:
                print(f'\nYou hit {self.herd.dinosaurs[2].name} and its health is now {negative_health_to_zero}!\n')
            else:
                print(f'\nYou hit {self.herd.dinosaurs[2].name} and its health is now {self.herd.dinosaurs[2].health}!\n')
  

    #a method to give the user options to choose which dino to use
    def show_dino_opponent_options(self):
        user_select = 0
        confirmed_select = 0
        selection = False
        negative_number_to_zero = 0

        print('Current Dinosaur Herd:')
        if self.herd.dinosaurs[0].health < 0:
            print(f'Press "0" to select {self.herd.dinosaurs[0].name} ({negative_number_to_zero} health)')
        else:
            print(f'Press "0" to select {self.herd.dinosaurs[0].name} ({self.herd.dinosaurs[0].health} health)')
        if self.herd.dinosaurs[1].health < 0:
            print(f'Press "1" to select {self.herd.dinosaurs[1].name} ({negative_number_to_zero} health)')    
        else:
            print(f'Press "1" to select {self.herd.dinosaurs[1].name} ({self.herd.dinosaurs[1].health} health)')
        if self.herd.dinosaurs[2].health < 0:    
            print(f'Press "2" to select {self.herd.dinosaurs[2].name} ({negative_number_to_zero} health)')
        else:
            print(f'Press "2" to select {self.herd.dinosaurs[2].name} ({self.herd.dinosaurs[2].health} health)')
        
        user_select = int(input('Select a dinosaur for your attack: '))
        while selection is False:
            if user_select >= 0 and user_select <= 2:
                if self.herd.dinosaurs[user_select].health > 0:
                    confirmed_select = user_select
                    selection = True
                elif self.herd.dinosaurs[user_select].health <= 0:
                    print('Your Dino is already re-extinct. Please select another Dino.')
                    user_select = int(input('Select another robot for your attack: '))
            elif user_select > 2 or user_select < 0:
                user_select = int(input('Invalid entry. Select a dino for your attack: '))
        return confirmed_select

    #a method to give the user options to choose which robot to use
    def show_robo_opponent_options(self):
        user_select = 0
        confirmed_select = 0
        selection = False
        negative_number_to_zero = 0

        print('Current Robot Fleet:')
        if self.fleet.robots[0].health < 0:
            print(f'Press "0" to select {self.fleet.robots[0].name} ({negative_number_to_zero} health)')   
        else: 
            print(f'Press "0" to select {self.fleet.robots[0].name} ({self.fleet.robots[0].health} health)')
        if self.fleet.robots[1].health < 0:
            print(f'Press "1" to select {self.fleet.robots[1].name} ({negative_number_to_zero} health)')
        else:    
            print(f'Press "1" to select {self.fleet.robots[1].name} ({self.fleet.robots[1].health} health)')
        if self.fleet.robots[2].health <0:
             print(f'Press "2" to select {self.fleet.robots[2].name} ({negative_number_to_zero} health)')
        else:
            print(f'Press "2" to select {self.fleet.robots[2].name} ({self.fleet.robots[2].health} health)')

        user_select = int(input('Select a robot for your attack: '))
        while selection is False:
            if user_select >= 0 and user_select <= 2:
                if self.fleet.robots[user_select].health > 0:
                    confirmed_select = user_select
                    selection = True
                elif self.fleet.robots[user_select].health <= 0:
                    print('Your Robot is already demolished. Please select another Robot.')
                    user_select = int(input('Select another robot for your attack: '))
            elif user_select > 2 or user_select < 0:
                user_select = int(input('Invalid entry. Select a robot for your attack: '))
        return confirmed_select


    #a method to display the winner of the game
    def display_winners(self):
        zero_health = 0
        if (self.fleet.robots[0].health <= 0 and self.fleet.robots[1].health <= 0 and self.fleet.robots[2].health <= 0):
            print('The Extinct Animals Won! (a.k.a. Dinosaurs)')
            print(f'Destruction Summary: "{self.fleet.robots[0].name}" ({zero_health} health), "{self.fleet.robots[1].name}" ({zero_health} health), "{self.fleet.robots[2].name}" ({zero_health} health).')
        elif (self.herd.dinosaurs[0].health <= 0 and self.herd.dinosaurs[1].health <= 0 and self.herd.dinosaurs[2].health <= 0):
            print('The Machines Won! (a.k.a. the Robots)')
            print(f'Extinction Summary: "{self.herd.dinosaurs[0].name}" ({zero_health} health), "{self.herd.dinosaurs[1].name}" ({zero_health} health), "{self.herd.dinosaurs[2].name}" ({zero_health} health).')


    