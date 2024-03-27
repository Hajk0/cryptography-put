import random
import sympy
import sys
import test
from math import isqrt

sys.set_int_max_str_digits(10000)

def generateBBS():
    seed = random.randint(1, int(1e10))
    x = random.randint(3 * 10**3, 3 * 10**4)  # (3 * 10**10, 3 * 10**11)
    y = random.randint(4 * 10**4, 4 * 10**5)  # (4 * 10**11, 4 * 10**12)

    p = find_good_prime(x) # find prime number p such that p = 3 mod 4
    q = find_good_prime(y)
    M = p * q
    seed = find_coprime(seed, M)
    print("Seed: ", seed, "p: ", p, "q: ", q, "M: ", M)

    number_length = 20000 # legnth of the number to be generated in bits
    output_bits = ""
    output = 0

    current_seed = seed
    for i in range(number_length):
        current_seed = (current_seed**2) % M
        calculated_bit = current_seed % 2
        output += 2**(number_length - i - 1) * calculated_bit
        output_bits += str(calculated_bit)
    print("Output bits: ", output_bits)
    print("Output: ", output)
    return (output_bits, int(output), seed, p, q, M, number_length)


def find_good_prime(x):
    p,  = find_primes(x, x * 2, 1)
    print(p)
    while p % 4 != 3:
        p,  = find_primes(x, x * 2, 1)
        print(p)
    print("Znalazło")
    return p


def euklides(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def find_coprime(x, y):
    while euklides(x, y) != 1:
        x += 1
    return x


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


def find_primes(min: int, max: int, quantity: int):
    if min % 2 == 0:
        min += 1
    primes = [i for i in range(min, max, 2) if is_prime(i)]
    returned_primes = []
    for i in range(quantity):
        p = random.choice(primes)
        while p in returned_primes:
            p = random.choice(primes)
        returned_primes.append(p)
    return returned_primes


if __name__ == '__main__':
    random_number_binary, random_number, M, seed, p, q, number_length = generateBBS()
    test = test.Test()
    print("Single bits test result: " + str(test.single_bits_test(random_number_binary, number_length)))
    print("Series test result: " + str(test.series_test(random_number_binary, number_length)))
    print("Long series test result: " + str(test.long_series_test(random_number_binary, number_length)))
    print("Poker test result: " + str(test.poker_test(random_number_binary, number_length)))