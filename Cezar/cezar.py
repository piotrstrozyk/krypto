#Piotr Stróżyk
# 278795
# 8.03.2024

import sys


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def multiplicative_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

def affine_cipher(text, key):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                shifted = (key[0] * (ord(char) - ord('a')) + key[1]) % 26
                encrypted_text += chr(shifted + ord('a'))
            elif char.isupper():
                shifted = (key[0] * (ord(char) - ord('A')) + key[1]) % 26
                encrypted_text += chr(shifted + ord('A'))
        else:
            encrypted_text += char
    return encrypted_text

def decrypt_affine(text, key):
    a_inv = multiplicative_inverse(key[0], 26)
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                shifted = (a_inv * (ord(char) - ord('a') - key[1])) % 26
                decrypted_text += chr(shifted + ord('a'))
            elif char.isupper():
                shifted = (a_inv * (ord(char) - ord('A') - key[1])) % 26
                decrypted_text += chr(shifted + ord('A'))
        else:
            decrypted_text += char
    return decrypted_text

def affine_brute_force(text):
    for a in range(1, 313):
        if gcd(a, 26) == 1:  
            for b in range(26):
                key = (a, b)
                decrypted_text = decrypt_affine(text, key)
                print(f"Key: a={a}, b={b}, Decrypted text: {decrypted_text}")

def caesar_cipher(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char) + shift
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            encrypted_text += chr(shifted)
        else:
            encrypted_text += char
    return encrypted_text

def decrypt_caesar(text, shift):
    return caesar_cipher(text, -shift)

def caesar_brute_force(text):
    for shift in range(1, 26):
        decrypted_text = decrypt_caesar(text, shift)
        print(f"Shift: {shift}, Decrypted text: {decrypted_text}")

def read_file(filename):
    with open(filename, 'r') as file:
        return file.read().strip()

def write_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)

def main():
    cipher = sys.argv[1]
    option = sys.argv[2]
        
    if option not in ['-e', '-d', '-j', '-k']:
        print("Invalid option.")
        return
    
    if cipher == '-c':    
        shift = int(read_file('key.txt').split()[0])
        
        if option == '-e':
            plaintext = read_file('plain.txt')
            encrypted_text = caesar_cipher(plaintext, shift)
            write_file('crypto.txt', encrypted_text)
            print("Encryption completed.")
        elif option == '-d':
            encrypted_text = read_file('crypto.txt')
            decrypted_text = decrypt_caesar(encrypted_text, shift)
            write_file('decrypt.txt', decrypted_text)
            print("Decryption completed.")
        elif option == '-j':
            plaintext = read_file('extra.txt')
            encrypted_text = read_file('crypto.txt')
            for s in range(1, 26):
                decrypted_text = decrypt_caesar(encrypted_text, s)
                if plaintext in decrypted_text:
                    write_file('key-found.txt', f"cezar {s}")
                    write_file('decrypt.txt', decrypted_text)
                    print("Key found and decryption completed.")
                    return
            print("Key not found.")
        elif option == '-k':
            encrypted_text = read_file('crypto.txt')
            caesar_brute_force(encrypted_text)
        else:
            print("Invalid option.")
            return
    elif cipher == '-a':
        key = tuple(map(int, read_file('key.txt').split())) 
        if option == '-e':
            plaintext = read_file('plain.txt')
            encrypted_text = affine_cipher(plaintext, key)
            write_file('crypto.txt', encrypted_text)
            print("Encryption completed.")
        elif option == '-d':
            encrypted_text = read_file('crypto.txt')
            decrypted_text = decrypt_affine(encrypted_text, key)
            write_file('decrypt.txt', decrypted_text)
            print("Decryption completed.")
        elif option == '-j':
            plaintext = read_file('extra.txt')
            encrypted_text = read_file('crypto.txt')
            for a in range(1, 26):
                if gcd(a, 26) == 1:
                    for b in range(26):
                        key = (a, b)
                        decrypted_text = decrypt_affine(encrypted_text, key)
                        if plaintext in decrypted_text:
                            write_file('key-found.txt', f"Affine {key}")
                            write_file('decrypt.txt', decrypted_text)
                            print("Key found and decryption completed.")
                            return
            print("Key not found.")
        elif option == '-k':
            encrypted_text = read_file('crypto.txt')
            affine_brute_force(encrypted_text)
        else:
            print("Invalid option.")
            return

if __name__ == "__main__":
    main()