#Piotr Stróżyk
# 278795
# 19.04.2024

import numpy as np
from PIL import Image
import hashlib

def read_bmp(file_path):
    image = Image.open(file_path)
    # Konwertuj obraz do skali szarości (jeśli jeszcze nie jest)
    if image.mode != 'L':
        image = image.convert('L')
    return np.array(image)

def read_key(file_path):
    try:
        with open(file_path, 'rb') as f:
            print("Using key.txt")
            return f.read()
    except FileNotFoundError:
        print("Using default key")
        return b'\x8b\xd1\xc1\xfb\xad\xe9\x88\xd1\xb9A7\x05\x81\xb4\xd3'

def block_encrypt_ecb(block, key):
    # Funkcja skrótu md5sum
    md5_hash = hashlib.md5()
    md5_hash.update(key)
    md5_hash.update(block.tobytes())
    # Konwertuj 16-bajtowy ciąg bajtów na blok 8x8 pikseli
    digest = np.frombuffer(md5_hash.digest(), dtype=np.uint8)
    # Powtarzaj digest, aby uzyskać wymaganą długość
    full_digest = np.tile(digest, 4)[:64]
    return full_digest.reshape(8, 8)

def block_encrypt_cbc(block, key, prev_cipher_block):
    # Funkcja skrótu md5sum
    md5_hash = hashlib.md5()
    md5_hash.update(key)
    md5_hash.update((block ^ prev_cipher_block).tobytes())
    # Konwertuj 16-bajtowy ciąg bajtów na blok 8x8 pikseli
    digest = np.frombuffer(md5_hash.digest(), dtype=np.uint8)
    # Powtarzaj digest, aby uzyskać wymaganą długość
    full_digest = np.tile(digest, 4)[:64]
    return full_digest.reshape(8, 8)

def encrypt_image_ecb(image, key):
    encrypted_image = np.zeros_like(image)
    height, width = image.shape
    for y in range(0, height, 8):
        for x in range(0, width, 8):
            block = image[y:y+8, x:x+8]
            encrypted_block = block_encrypt_ecb(block, key)
            encrypted_image[y:y+8, x:x+8] = encrypted_block
    return encrypted_image

def encrypt_image_cbc(image, key):
    encrypted_image = np.zeros_like(image)
    height, width = image.shape
    prev_cipher_block = np.zeros((8, 8), dtype=np.uint8)
    for y in range(0, height, 8):
        for x in range(0, width, 8):
            block = image[y:y+8, x:x+8]
            encrypted_block = block_encrypt_cbc(block, key, prev_cipher_block)
            encrypted_image[y:y+8, x:x+8] = encrypted_block
            prev_cipher_block = encrypted_block
    return encrypted_image

# Wczytanie obrazu
image = read_bmp("plain.bmp")

# Wczytanie klucza
key = read_key("key.txt")

# Szyfrowanie obrazu w trybie ECB
encrypted_image_ecb = encrypt_image_ecb(image, key)
Image.fromarray(encrypted_image_ecb).save("ecb_crypto.bmp")

# Szyfrowanie obrazu w trybie CBC
encrypted_image_cbc = encrypt_image_cbc(image, key)
Image.fromarray(encrypted_image_cbc).save("cbc_crypto.bmp")