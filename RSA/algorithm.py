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
        primes = Generator.find_primes3(10000, 50000, 2)
        print("Primes: ", primes)
        self.generate_keys(primes[0], primes[1])
        message = 'Hello, World! This is a test message. I hope it works! :) 1234567890!@#$%^&*()_+{}|:"<>?~`-=[]\;\',./'
        encrypted_message = self.encrypt_message(message, self.public_key)
        decrypted_message = self.decrypt_message(encrypted_message, self.private_key)
        print("Message: ", message)
        print("Encrypted message: ", encrypted_message)
        print("Decrypted message: ", decrypted_message)

    def main(self, message: str):
        primes = Generator.find_primes3(1000, 5000, 2)
        print("Primes: ", primes)
        self.generate_keys(primes[0], primes[1])
        encrypted_message = self.encrypt_message(message, self.public_key)
        decrypted_message = self.decrypt_message(encrypted_message, self.private_key)
        print("Message: ", message)
        print("Encrypted message: ", encrypted_message)
        print("Decrypted message: ", decrypted_message)
        return message, encrypted_message, decrypted_message

    def generate_keys(self, p, q):
        self.n = p * q
        self.phi = (p - 1) * (q - 1)
        self.e = Generator.find_coprime(random.randint(1, self.phi), self.phi)
        self.d = self.generate_d(2, 2)
        print("generate_d: ", self.d)
        self.public_key = {'e': self.e, 'n': self.n}
        self.private_key = {'d': self.d, 'n': self.n}
        
    def generate_d(self, min: int, max: int):
        generated_d = random.randint(min, max)
        while (generated_d * self.e) % self.phi != 1:
            generated_d += 1
        return generated_d

    def encrypt(self, message: int, public_key: dict):
        message_encrypted = pow(message, public_key['e'], public_key['n'])
        return message_encrypted

    def decrypt(self, message: int, private_key: dict):
        message_decrypted = pow(message, private_key['d'], private_key['n'])
        return message_decrypted

    def encrypt_message(self, message: str, public_key: dict):
        message_encrypted = []
        for letter in message:
            letter_int = ord(letter)
            message_encrypted.append(self.encrypt(letter_int, public_key))
        return message_encrypted

    def decrypt_message(self, message: str, private_key: dict):
        message_decrypted = ''
        for letter in message:
            letter_decrypted = self.decrypt(letter, private_key)
            message_decrypted += chr(letter_decrypted)
        return message_decrypted

if __name__ == '__main__':
    algorithm = Algorithm()
    algorithm.main()
