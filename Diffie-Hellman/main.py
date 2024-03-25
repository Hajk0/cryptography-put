from generator import Generator
from person import Person
import random

class DiffieHellman:
    def __init__(self):
        pass

    def main(self):
        n, g = self.generate_n_g(1000, 5000)
        person_a = Person(10000, 50000)
        person_b = Person(10000, 50000)
        X = person_a.calc_X(g, n)
        Y = person_b.calc_X(g, n)
        person_a.calc_k(Y, n)
        person_b.calc_k(X, n)

    def main_group_of_three(self):
        n, g = self.generate_n_g(100000, 500000)
        person_a = Person(100000, 500000)
        person_b = Person(100000, 500000)
        person_c = Person(100000, 500000)
        X = person_a.calc_X(g, n)
        Y = person_b.calc_X(g, n)
        Z = person_c.calc_X(g, n)

        Z_prim = person_a.calc_k(Z, n)
        X_prim = person_b.calc_k(X, n)
        Y_prim = person_c.calc_k(Y, n)

        Y_bis = person_a.calc_k(Y_prim, n)
        Z_bis = person_b.calc_k(Z_prim, n)
        X_bis = person_c.calc_k(X_prim, n)
        print(X_bis)
        print(Y_bis)
        print(Z_bis)
        
    def main_groups(self, group):
        X = [0 for _ in range(len(group))]
        for person in range(len(group)):
            X[person] = group[person].calc_X(g, n)
        for i in range(len(group) - 1):
            for j in range(len(group)):
                sent = (j + i + 1) % len(group)
                X[sent] = group[j].calc_k(X[sent], n)
        print(X)
        
    def generate_n_g(self, min: int, max: int):
        n = random.choice(Generator.find_primes(min, max, 1))
        g = random.choice(Generator.find_primitive_roots(n))
        return (n, g)


if __name__ == '__main__':
    diffie_hellman = DiffieHellman()

    n, g = diffie_hellman.generate_n_g(100000, 500000)
    person_a = Person(100000, 500000)
    person_b = Person(100000, 500000)
    person_c = Person(100000, 500000)
    person_d = Person(100000, 500000)
    diffie_hellman.main_groups([person_a, person_b, person_c, person_d])
    