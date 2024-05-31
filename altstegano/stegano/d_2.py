# Bartosz Majkowski

from len_maximum import LEN_MAXIMUM


def d_2():
    with open("watermark.html", "r", encoding="utf-8") as f:
        watermark = f.readlines()
    msg = ""
    watermark = "".join(watermark).split(" ")
    for i in range(len(watermark)):
        if watermark[i] == "":
            msg += "1"
        else:
            msg += "0"
    msg = msg.replace("01", "1")[:LEN_MAXIMUM]
    h_msg = ""
    for i in range(0, len(msg), 4):
        h_msg += hex(int(msg[i:i + 4], 2))[2:]
    with open("detect.txt", "w+") as f:
        f.write(h_msg.upper())
