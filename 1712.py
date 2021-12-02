import math
A,B,C=map(int, input().split())
if B<C:
    n = math.ceil(A/(C-B))
    if (A/(C-B)) % 1 == 0: # 손익 0인 지점
        n += 1
else: n = -1
print(n)