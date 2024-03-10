import random
import sympy
import sys
import test

sys.set_int_max_str_digits(10000)

def generateBBS():
    seed = random.randint(1, int(1e10))
    x = random.randint(3 * 10**10, 3 * 10**11)
    y = random.randint(4 * 10**11, 4 * 10**12)

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
    return (output_bits, int(output), M, seed, p, q, number_length)


def find_good_prime(x):
    p = sympy.nextprime(x)
    while p % 4 != 3:
        p = sympy.nextprime(p)
    return p


def euklides(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def find_coprime(x, y):
    while euklides(x, y) != 1:
        x += 1
    return x


if __name__ == '__main__':
    random_number_binary, random_number, M, seed, p, q, number_length = generateBBS()
    test = test.Test()
    print("Single bits test result: " + str(test.single_bits_test(random_number_binary, number_length)))
    print("Series test result: " + str(test.series_test(random_number_binary, number_length)))
    print("Long series test result: " + str(test.long_series_test(random_number_binary, number_length)))
    print("Poker test result: " + str(test.poker_test(random_number_binary, number_length)))