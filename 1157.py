S = input().upper()
d = {}
for s in S:
    if s not in d:
        d[s] = S.count(s)
l = [k for k, v in d.items() if v == max(d.values())]
print("?" if len(l) != 1 else l[0])