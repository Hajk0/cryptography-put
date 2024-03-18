import random
import sympy

class Generator:
    @staticmethod
    def find_primes(min: int, max: int, quantity: int): # TODO(implement own primalyty test algorithm)
        primes = []
        for i in range(quantity):
            p = sympy.randprime(min, max)
            while p in primes:
                p = sympy.randprime(min, max)
            primes.append(p)
        return primes

    @staticmethod
    def euklides(x, y):
        while y != 0:
            x, y = y, x % y
        return x

    @staticmethod
    def find_coprime(x, y):
        while Generator.euklides(x, y) != 1:
            x += 1
        return x