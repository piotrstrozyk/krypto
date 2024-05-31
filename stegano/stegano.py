#Piotr Stróżyk
#31.05.2024

def embed_1():
    lines = open('cover.html', 'r').readlines()
    msg = open('mess.txt', 'r').read().strip()
    helper = ''
    for num in msg:
        binary = bin(int(num, 16))[2:].zfill(4)
        helper += binary
    if len(helper) > len(lines):
        print("Carrier is too small to convey the entire message.")
        sys.exit(1)
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
    new_cover_lines += "".join(lines[64:-1])
    with open('watermark.html', 'w+') as f:
        f.write(new_cover_lines)

def detect_1():
    watermark = open('watermark.html').readlines()
    msg = ''
    for line in watermark:
        helper = line.replace('\n', '')
        if helper[-1] == ' ':
            msg += '1'
        else:
            msg += '0'
        if len(msg) == 128:
            break
    h_msg = ''
    for i in range(0, len(msg), 4):
        h_number = hex(int(msg[i:i + 4], 2))[2:]
        h_msg += h_number
    with open('detect.txt', 'w+') as f:
        f.write(h_msg)
        
############################################################################################

def embed_2():
    with open("mess.txt", "r", encoding="utf-8") as f:
        msg = f.read().strip()
    with open("cover.html", "r", encoding="utf-8") as cover_file:
        cover = cover_file.readlines()
    b_msg = ""
    for x in msg:
        binary = bin(int(x, 16))[2:].zfill(4)
        b_msg += binary
    cover = "".join(cover).replace("  ", "")
    spc_counter = cover.count(" ")
    if len(b_msg) > spc_counter:
        print("Carrier is too small to convey the entire message.")
        sys.exit(1)
    watermark = ""
    cover = cover.split(" ")
    for i in range(len(b_msg)):
        bit = b_msg[i]
        if bit == "1":
            cover[i] += " "
        watermark += cover[i] + " "
    watermark += " ".join(cover[len(b_msg):])
    with open("watermark.html", "w+", encoding="utf-8") as f:
        f.writelines(watermark)


def detect_2():
    with open("watermark.html", "r", encoding="utf-8") as f:
        watermark = f.readlines()
    msg = ""
    watermark = "".join(watermark).split(" ")
    for i in range(len(watermark)):
        if watermark[i] == "":
            msg += "1"
        else:
            msg += "0"
    msg = msg.replace("01", "1")[:128]
    h_msg = ""
    for i in range(0, len(msg), 4):
        h_msg += hex(int(msg[i:i + 4], 2))[2:]
    with open("detect.txt", "w+") as f:
        f.write(h_msg)

############################################################################################

def embed_3():
    with open("mess.txt", "r", encoding="utf-8") as f:
        msg = f.read().strip()

    with open("cover.html", "r", encoding="utf-8") as cover_file:
        cover = cover_file.readlines()

    b_msg = ""
    for x in msg:
        binary = bin(int(x, 16))[2:].zfill(4)
        b_msg += binary

    if len(b_msg) > len(cover):
        print("Carrier is too small to convey the entire message.")
        sys.exit(1)

    watermark = ""
    i = 0
    for line in cover:
        watermark_line = line
        if "class" in line:
            if len(b_msg) > i and b_msg[i] == "1":
                watermark_line = line.replace('class', 'clas')
            else:
                pass
            watermark += watermark_line
            i += 1
        else:
            watermark += watermark_line

    with open("watermark.html", "w+", encoding="utf-8") as f:
        f.writelines(watermark)
        
def detect_3():
    with open("watermark.html", "r", encoding="utf-8") as f:
        watermark = f.readlines()

    message = ""
    for line in watermark:
        if "class" in line:
            message += "0"
        elif 'clas' in line:
            message += "1"
        else:
            pass
        if len(message) == 128:
            break

    hex_message = ""
    for i in range(0, len(message), 4):
        hex_message += hex(int(message[i: i + 4], 2))[2:]

    with open("detect.txt", "w+", encoding="utf-8") as f:
        f.write(hex_message)

############################################################################################

def embed_4():
    with open("mess.txt", "r", encoding="utf-8") as f:
        msg = f.read().strip()

    with open("cover.html", "r", encoding="utf-8") as cover_file:
        cover = cover_file.readlines()

    cover = [x.replace("<p></p>", "") for x in cover]

    num_fonts = "".join(cover).count("<p>")

    b_msg = ""
    for x in msg:
        binary = bin(int(x, 16))[2:].zfill(4)
        b_msg += binary
    if len(b_msg) > num_fonts:
        print("Carrier is too small to convey the entire message.")
        sys.exit(1)

    watermark = ""
    i = 0
    for line in cover:
        watermark_line = line
        if "<p>" in line:
            if len(b_msg) > i and b_msg[i] == "1":
                watermark_line = line.replace("<p>", "<p></p><p>")
            else:
                watermark_line = line.replace("</p>", "</p><p></p>")
            watermark += watermark_line
            i += 1
        else:
            watermark += watermark_line

    with open("watermark.html", "w+", encoding="utf-8") as f:
        f.write(watermark)
        
def detect_4():

    with open("watermark.html", "r", encoding="utf-8") as f:
        watermark = f.readlines()

    msg = ""
    for i in watermark:
        if "<p></p><p>" in i:
            msg += "1"
        if "</p><p></p>" in i:
            msg += "0"
        if len(msg) == 128:
            break

    h_msg = ""
    for i in range(0, len(msg), 4):
        h_msg += hex(int(msg[i: i + 4], 2))[2:]

    with open("detect.txt", "w+", encoding="utf-8") as f:
        f.write(h_msg)

import sys

def main():
    
    if len(sys.argv) != 3:
        print("Usage: python stegano.py <option e / d> <option 1-4>")
        return
    
    result = ""
    with open("cover.html", "r+") as file:
        for line in file:
            if not line.isspace():
                result += line

        file.seek(0)
        file.write(result)


    if sys.argv[1] == "-e":
        if sys.argv[2] == "-1":
            embed_1()
        elif sys.argv[2] == "-2":
            embed_2()
        elif sys.argv[2] == "-3":
            embed_3()
        elif sys.argv[2] == "-4":
            embed_4()
    elif sys.argv[1] == "-d":
        if sys.argv[2] == "-1":
            detect_1()
        elif sys.argv[2] == "-2":
            detect_2()
        elif sys.argv[2] == "-3":
            detect_3()
        elif sys.argv[2] == "-4":
            detect_4()

if __name__ == "__main__":
    main()
