l = []
for i in range(9):
    e = int(input())
    l.append(e)
print(max(l), l.index(max(l))+1, sep="\n")