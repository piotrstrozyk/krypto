
# Bartosz Majkowski

from len_maximum import LEN_MAXIMUM


def d_3():
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
        if len(message) == LEN_MAXIMUM:
            break

    hex_message = ""
    for i in range(0, len(message), 4):
        hex_message += hex(int(message[i: i + 4], 2))[2:]

    with open("detect.txt", "w+", encoding="utf-8") as f:
        f.write(hex_message.upper())
