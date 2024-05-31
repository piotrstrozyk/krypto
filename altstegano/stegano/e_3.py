
# Bartosz Majkowski

def e_3():
    with open("mess.txt", "r", encoding="utf-8") as f:
        msg = f.read().strip()

    with open("cover.html", "r", encoding="utf-8") as cover_file:
        cover = cover_file.readlines()

    b_msg = ""
    for x in msg:
        binary = bin(int(x, 16))[2:].zfill(4)
        b_msg += binary

    if len(b_msg) > len(cover):
        raise Exception("Nośnik jest za mały do przekazania całej wiadomości.")

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
