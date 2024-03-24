import random
from math import isqrt

class Generator:
    @staticmethod
    def find_primes(min: int, max: int, quantity: int):
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

    @staticmethod
    def find_primitive_roots(n: int):
        roots = []
        x = n - 1
        factors = Generator.prime_factors(x)
        print("factors: ", factors)
        arr = []
        for i in factors:
            arr.append(x // i)
        for i in range(2, n):
            for j in arr:
                if pow(i, j, n) == 1:
                    print("break")
                    break
                elif arr[-1] == j:
                    roots.append(i)
        return roots
    
    @staticmethod
    def prime_factors(n):
        factors = []
        while n % 2 == 0:
            factors.append(2)
            n //= 2
        for i in range(3, int(n**0.5) + 1, 2):
            while n % i == 0:
                factors.append(i)
                n //= i
        if n > 2:
            factors.append(n)
        return factors