import random

class Person:
    def __init__(self, min: int, max: int):
        self.pick_private_key(min, max)

    def pick_private_key(self, min: int, max: int):
        self.private_key = random.randint(min, max)
    
    def get_private_key(self):
        return self.private_key

    def calc_X(self, g: int, n: int):
        self.X = pow(g, self.private_key, n)
        return self.X

    def calc_k(self, Y: int, n: int):
        self.k = pow(Y, self.private_key, n)
        return self.k
