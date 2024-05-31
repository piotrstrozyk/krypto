
# Bartosz Majkowski

def e_4():
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
        raise Exception("Nośnik jest za mały do przekazania całej wiadomości.")

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
