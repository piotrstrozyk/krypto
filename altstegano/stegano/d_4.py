# Bartosz Majkowski

from len_maximum import LEN_MAXIMUM


def d_4():

    with open("watermark.html", "r", encoding="utf-8") as f:
        watermark = f.readlines()

    msg = ""
    for i in watermark:
        if "<p></p><p>" in i:
            msg += "1"
        if "</p><p></p>" in i:
            msg += "0"
        if len(msg) == LEN_MAXIMUM:
            break

    h_msg = ""
    for i in range(0, len(msg), 4):
        h_msg += hex(int(msg[i: i + 4], 2))[2:]

    with open("detect.txt", "w+", encoding="utf-8") as f:
        f.write(h_msg.upper())
