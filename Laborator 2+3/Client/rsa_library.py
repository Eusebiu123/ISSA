import random

import bitstring as bitstring
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii

prime_number_1 = 277
prime_number_2 = 239

ON_low = '0x01'

'''
Euclid's algorithm for determining the greatest common divisor
Use iteration to make it faster for larger integers
'''


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


'''
Euclid's extended algorithm for finding the multiplicative inverse of two numbers
'''


def multiplicative_inverse(e, phi):
    d = 0
    x1 = 0
    x2 = 1
    y1 = 1
    temp_phi = phi

    while e > 0:
        temp1 = temp_phi // e
        temp2 = temp_phi - temp1 * e
        temp_phi = e
        e = temp2

        x = x2 - temp1 * x1
        y = d - temp1 * y1

        x2 = x1
        x1 = x
        d = y1
        y1 = y

    if temp_phi == 1:
        return d + phi


'''
Tests to see if a number is prime.
'''


def is_prime(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for n in range(3, int(num ** 0.5) + 2, 2):
        if num % n == 0:
            return False
    return True


def generate_keypair(p, q):
    if not (is_prime(p) and is_prime(q)):
        raise ValueError('Both numbers must be prime.')
    elif p == q:
        raise ValueError('p and q cannot be equal')
    # n = pq
    modulus = p * q

    # Phi is the totient of n
    L = (p - 1) * (q - 1)
    # print("L=",L)

    # Choose an integer e such that e and L(n) are coprime
    e = random.randrange(2, L)
    # print('E=',e)

    # Use Euclid's Algorithm to verify that e and L(n) are comprime
    g = gcd(e, L)
    # print('G=',g)
    while g != 1:
        e = random.randrange(2, L)
        # print("E=",e)
        g = gcd(e, L)
        # print("G=",g)
    # Use Extended Euclid's Algorithm to generate the private key
    d = multiplicative_inverse(e, L)
    # print("D=",d)

    # Return public and private keypair
    # Public key is (e, n) and private key is (d, n)
    return ((e, modulus), (d, modulus))


############################### EXERCISE 1 ###############################
def encrypt(public_key, hex_number):
    return ((hex_number ** public_key[0]) % public_key[1])


############################### EXERCISE 2 ###############################
def decrypt(private_key, encrypted_msg):
    return ((encrypted_msg ** private_key[0]) % private_key[1])


############################### EXERCISE 3 ###############################
def low_check(hex_nr):
    global ON_low
    return int(ON_low, 16) == (int(hex(hex_nr & 0xff), 16))


############################### EXERCISE 4 ###############################
def number_check(hex_nr):
    high_bit = divmod(hex_nr, 0x100)[0]
    return bitstring.Bits(bin=bin(int(hex(high_bit), 16))[2:]).int == ~int(ON_low, 16)


if __name__ == "__main__":
    print()
    # mc = encrypt((5, 14), 2)
    # print("validare criptare:  ", mc)
    # print("validare decriptare:  ", decrypt((11, 14), mc))
    # print("validare low_check cu True:   ", low_check(int('8x5781', 16)))
    # print("validare low_check cu False:   ", low_check(int('8x5732', 16)))
    # print("validare number_check cu True:   ", number_check(int('0xfe01', 16)))
    # print("validare number_check cu False:   ", number_check(int('8x5732', 16)))
