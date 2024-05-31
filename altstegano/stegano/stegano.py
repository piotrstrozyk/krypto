# Bartosz Majkowski

import sys

from e_1 import e_1
from d_1 import d_1
from e_2 import e_2
from d_2 import d_2
from e_3 import e_3
from d_3 import d_3
from e_4 import e_4
from d_4 import d_4

result = ""
with open("cover.html", "r+") as file:
    for line in file:
        if not line.isspace():
            result += line

    file.seek(0)
    file.write(result)


if sys.argv[1] == "-e":
    if sys.argv[2] == "-1":
        e_1()
    elif sys.argv[2] == "-2":
        e_2()
    elif sys.argv[2] == "-3":
        e_3()
    elif sys.argv[2] == "-4":
        e_4()
elif sys.argv[1] == "-d":
    if sys.argv[2] == "-1":
        d_1()
    elif sys.argv[2] == "-2":
        d_2()
    elif sys.argv[2] == "-3":
        d_3()
    elif sys.argv[2] == "-4":
        d_4()


