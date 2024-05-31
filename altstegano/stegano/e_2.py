# Bartosz Majkowski

def e_2():
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
        raise Exception("Nośnik jest za mały do przekazania całej wiadomości.")
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
