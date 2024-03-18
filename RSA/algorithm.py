from generator import Generator
import random

class Algorithm:
    def __init__(self):
        self.n = None
        self.phi = None
        self.e = None
        self.d = None
        self.public_key = None
        self.private_key = None

    def main(self):
        primes = Generator.find_primes(100, 500, 2)
        self.generate_keys(primes[0], primes[1])
        message = 123
        encrypted_message = self.encrypt(message)
        decrypted_message = self.decrypt(encrypted_message)
        print("Message: ", message)
        print("Encrypted message: ", encrypted_message)
        print("Decrypted message: ", decrypted_message)

    def generate_keys(self, p, q):
        self.n = p * q
        self.phi = (p - 1) * (q - 1)
        self.e = Generator.find_coprime(random.randint(1, self.phi), self.phi)
        self.d = self.generate_d(100, 500)
        self.public_key = {'e': self.e, 'n': self.n}
        self.private_key = {'d': self.d, 'n': self.n}
        
    def generate_d(self, min: int, max: int):
        generated_d = random.randint(min, max)
        while (generated_d * self.e) % self.phi != 1:
            generated_d += 1
        return generated_d

    def encrypt(self, message: int):
        return pow(message, self.public_key['e'], self.public_key['n'])

    def decrypt(self, message: int):
        return pow(message, self.private_key['d'], self.private_key['n'])
         

if __name__ == '__main__':
    algorithm = Algorithm()
    algorithm.main()
