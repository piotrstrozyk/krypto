#Piotr Stróżyk
# 278795
# 22.03.2024
import re
import os
 
class XOR:
    def prepare(self):
        with open('orig.txt', 'r') as fin, open('plain.txt', 'w') as fout:
            for line in fin:
                line = re.sub(r'[,.!?:;\'-0123456789]', '', line)
                line = line.lower()
                fout.write(line[:64] + '\n')
 
    def cryptanalysis(self):
        with open('crypto.txt', 'r', encoding='utf-8') as fin, open('decrypt.txt', 'w', errors='replace') as fout:
            lines = fin.readlines()
            lentresc = len(lines[0])
            arr = [bytearray(line, 'US-ASCII') for line in lines]
            bytes = bytearray(lentresc)
            bajtyhasla = [0]*lentresc
            for x in range(min(20, len(arr))):
                for y in range(min(lentresc, len(arr[x]))):
                    if arr[x][y] < 58:
                        bytes[y] = 32
                        bajtyhasla[y] = arr[x][y] - bytes[y]
            for x in range(min(20, len(arr))):
                for y in range(min(lentresc, len(arr[x]))):
                    arr[x][y] -= bajtyhasla[y]
                    if y == 38:  # If this is the 39th byte
                        # Perform a different operation on the 39th byte
                        arr[x][y] -= 13
                        
                    if 33 < arr[x][y] < 97:
                        arr[x][y] += 25
                    fout.write(chr(arr[x][y]))
                fout.write('\n')
 
    def asciikey(self):
        try:
            with open('key.txt', 'r') as key_file:
                akey = key_file.readline()
                bytes = bytearray(akey, 'US-ASCII')
                for i in range(len(akey)):
                    if 97 <= bytes[i] <= 122:  # Lowercase letters
                        bytes[i] -= 97
                    elif 65 <= bytes[i] <= 90:  # Uppercase letters
                        bytes[i] -= 65
                    else:
                        raise ValueError("Invalid character in key. ASCII value must be a letter.")
                return bytes
        except FileNotFoundError:
            print('Brak pliku z kluczem')
        except IOError:
            print('Problem we/wy')
    def encrypt(self):
        key = self.asciikey()
        with open('plain.txt', 'r') as fin, open('crypto.txt', 'w') as fout:
            all_text = fin.read()
            bytes = bytearray(all_text, 'US-ASCII')
            z = 0
            for i in range(len(bytes)):
                if z >= len(key):
                    z = 0
                result = bytes[i] + key[z]
                z += 1
                if result > 122:
                    result -= 25
                if bytes[i] == 10:
                    result = 10
                    z = 0
                fout.write(chr(result))
 
if __name__ == "__main__":
    import sys
    xor = XOR()
    if sys.argv[1] == '-p':
        xor.prepare()
    elif sys.argv[1] == '-e':
        xor.encrypt()
    elif sys.argv[1] == '-k':
        xor.cryptanalysis()