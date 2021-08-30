import re

with open("username.txt") as fhand:
    fline = [line.strip() for line in fhand]
    for i in fline:
        if re.search("^[JLT][a-z]*\S[0-9]{2}$", i):
            print(i)
