#Piotr Stróżyk

def diff():
    hex1 = 'd9f1054cb6a2ca9d8fa7696f0af5d8a8f4a5b2f5dc88adb180257dca63b6cb4c2206d79a92de726e6a0500c02f44c176f7ef2bf584d86ca4d6216c1b425370c2'
    hex2 = '51952573fc09a3d6cd2009287624c9f40d5005866bd92b73b871486b9e721ce3b99dbab322fce1f72c689409ce4e175f882093efecbf98e917d80db218bc4564'

    bin1 = bin(int(hex1, 16))[2:].zfill(128)  
    bin2 = bin(int(hex2, 16))[2:].zfill(128)  

    dlugosc = len(bin1)
    roznica = ([x == y for (x, y) in zip(bin1, bin2)].count(False))
    procent = (float(roznica)/float(dlugosc))*100

    print("%d z %d, procentowo: %.2f%%." % (roznica, dlugosc, procent))

diff()