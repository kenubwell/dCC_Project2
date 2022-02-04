from dinosaur import Dinosaur

class Herd:
     
    def __init__(self):
        self.dinosaurs = []
        self.create_herd()

    def create_herd(self):
        dino_one = Dinosaur('Godzilla', 50)
        dino_two = Dinosaur('Sauron', 40)
        dino_three = Dinosaur('Yoshi', 30)

        self.dinosaurs = [dino_one, dino_two, dino_three]