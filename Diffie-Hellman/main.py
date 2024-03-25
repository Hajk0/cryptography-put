from generator import Generator
from person import Person
import random

class DiffieHellman:
    def __init__(self):
        self.n = None
        self.g = None

    def main(self):
        n, g = self.generate_n_g(1000, 5000)
        person_a = Person(10000, 50000)
        person_b = Person(10000, 50000)
        X = person_a.calc_X(g, n)
        Y = person_b.calc_X(g, n)
        person_a.calc_k(Y, n)
        person_b.calc_k(X, n)
        
        
    def generate_n_g(self, min: int, max: int):
        n = random.choice(Generator.find_primes(min, max, 1))
        g = random.choice(Generator.find_primitive_roots(n))
        return (n, g)


if __name__ == '__main__':
    diffie_hellman = DiffieHellman()
    diffie_hellman.main()
    