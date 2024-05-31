# Bartosz Majkowski

from len_maximum import LEN_MAXIMUM


def e_1():
    lines = open('cover.html', 'r').readlines()
    msg = open('mess.txt', 'r').read().strip()
    helper = ''
    for num in msg:
        binary = bin(int(num, 16))[2:].zfill(4)
        helper += binary
    if len(helper) > len(lines):
        raise Exception("Nośnik jest za mały do przekazania całej wiadomości.")
    message_index = 0
    new_cover_lines = ""
    for i, bit in enumerate(helper):
        stripped_line = lines[i].replace('\n', '')
        if bit == '1':
            stripped_line += ' ' + '\n'
        else:
            stripped_line += '\n'
        message_index += 1
        new_cover_lines += stripped_line
    new_cover_lines += "".join(lines[LEN_MAXIMUM:-1])
    with open('watermark.html', 'w+') as f:
        f.write(new_cover_lines)
