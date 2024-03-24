import random
import sympy
from math import isqrt

class Generator:
    @staticmethod
    def find_primes(min: int, max: int, quantity: int):
        primes = []
        for i in range(quantity):
            p = sympy.randprime(min, max)
            while p in primes:
                p = sympy.randprime(min, max)
            primes.append(p)
        return primes
    
    @staticmethod
    def find_primes2(min: int, max: int, quantity: int):
        primes = []
        for i in range(quantity):
            p = random.randint(min, max)
            while not Generator.is_prime(p):
                p = random.randint(min, max)
            primes.append(p)
        return primes
    
    @staticmethod
    def find_primes3(min: int, max: int, quantity: int):
        if min % 2 == 0:
            min += 1
        primes = [i for i in range(min, max, 2) if Generator.is_prime(i)]
        returned_primes = []
        for i in range(quantity):
            p = random.choice(primes)
            while p in returned_primes:
                p = random.choice(primes)
            returned_primes.append(p)
        return returned_primes

    @staticmethod
    def is_prime(n: int) -> bool:
        if n <= 3:
            return n > 1
        if n % 2 == 0 or n % 3 == 0:
            return False
        limit = isqrt(n)
        for i in range(5, limit+1, 6):
            if n % i == 0 or n % (i+2) == 0:
                return False
        return True

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