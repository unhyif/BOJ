d = {}
for i in range(65,91): # chr(65) == "A", chr(90) == "Z"
    if i in range(65,68):
        d[chr(i)] = 3
    elif i in range(68,71):
        d[chr(i)] = 4
    elif i in range(71,74):
        d[chr(i)] = 5
    elif i in range(74,77):
        d[chr(i)] = 6
    elif i in range(77,80):
        d[chr(i)] = 7
    elif i in range(80,84):
        d[chr(i)] = 8
    elif i in range(84,87):
        d[chr(i)] = 9
    else:
        d[chr(i)] = 10
c = 0
for s in input():
    c += d[s]
print(c)