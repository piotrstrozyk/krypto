#Piotr Stróżyk
# 278795
# 22.03.2024

import argparse

def prep(input_file, output_file):
    with open(input_file, 'r') as file:
        text = file.read().strip().lower()
    
    with open(output_file, 'w') as file:
        file.write(text)

def encrypt(plain_file, key_file, crypto_file):
    with open(plain_file, 'r', encoding='utf-8') as f_plain, open(key_file, 'r', encoding='utf-8') as f_key, open(crypto_file, 'w', encoding='utf-8') as f_crypto:
        plain = [line.rstrip("\n") for line in f_plain.readlines()]
        key = f_key.read()
        for line in plain:
            for i in range(64):
                f_crypto.write(chr(ord(line[i]) ^ ord(key[i])))

def crypto_analysis():
    with open("crypto.txt", "r") as f:
        crypto_text = f.read()
    lines = [crypto_text[i:i+64] for i in range(0, len(crypto_text), 64)]
    cols = [[line[i] for line in lines] for i in range(len(lines[0]))]
    decrypted_cols = []

    for col in cols:
        line = ["" for _ in range(len(col))]
        diff = [ord(col[i]) ^ ord(col[i+1]) for i in range(len(col)-1)]
        i = 0
        while i < len(diff):
            try:
                if (diff[i] & 224 == 0) and (diff[i+1] & 224 == 64) and (diff[i+2] & 224 == 64):
                    line[i] = chr(diff[i] ^ diff[i+1] ^ 32)
                    line[i+1] = chr(32 ^ diff[i+1])
                    line[i+2] = chr(32 ^ diff[i+2])
                    i += 3
                elif (diff[i] & 224 == 64) and (diff[i+1] & 224 == 64) and (diff[i+2] & 224 == 0) and i < len(line) - 2:
                    line[i] = chr(32 ^ diff[i])
                    line[i+1] = chr(32)
                    line[i+2] = chr(32 ^ diff[i+1])
                    i += 3
                elif (diff[i] == diff[i+2]) and (diff[i] & 224 == 0) and (diff[i+1] & 224 == 64):
                    line[i] = chr(32)
                    line[i+1] = chr(diff[i+1] ^ 32)
                    line[i+2] = chr(32)
                    i += 3
                elif (diff[i] & 224 == 0) and (diff[i+1] & 224 == 64) and (diff[i+2] & 224 == 0):
                    line[i] = chr(diff[i] ^ diff[i+1] ^ 32)
                    line[i+1] = chr(32 ^ diff[i+1])
                    line[i+2] = chr(32)
                    i += 3
                elif (diff[i] & 224 == 64) and (diff[i+1] & 224 == 0) and (diff[i+2] & 224 == 0):
                    line[i] = chr(32)
                    line[i+1] = chr(diff[i] ^ 32)
                    line[i+2] = chr(diff[i+1] ^ diff[i] ^ 32)
                    i += 1
                else:
                    line[i] = "_"
                    i += 1
            except IndexError:
                line[i] = "_"
                i += 1

        decrypted_cols.append("".join(line))

    decrypted_lines = ["".join(col) for col in zip(*decrypted_cols)]
    with open("decrypt.txt", "w") as f:
        f.write("\n".join(decrypted_lines))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", action="store_true")
    parser.add_argument("-e", action="store_true")
    parser.add_argument("-k", action="store_true")

    args = parser.parse_args()

    if args.p:
        prep('orig.txt', 'plain.txt')
        print("Text prepared")

    if args.e:
        encrypt('plain.txt', 'key.txt', 'crypto.txt')
        print("Text encrypted")

    if args.k:
        crypto_analysis()
        print("Crypto analysis performed")
