#(10 points): As a developer, I want to instantiate three Robot objects and three Dinosaur objects and assign the appropriate values to all the objects.  
#(10 points): As a developer, I want the created Robot objects to be stored in a Fleet and the created Dinosaur objects to be stored in a Herd 
    # (the Fleet and Herd must use a List to store the objects). 

from dinosaur import Dinosaur

class Herd:
     
    def __init__(self):
        self.dinosaurs = []
        self.create_herd()

    def create_herd(self):
        dino_one = Dinosaur('Godzilla', 50)
        dino_two = Dinosaur('Sauron', 45)
        dino_three = Dinosaur('Yoshi', 40)

        self.dinosaurs = [dino_one, dino_two, dino_three]
