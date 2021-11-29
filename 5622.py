a = "ABC DEF GHI JKL MNO PQRS TUV WXYZ".split()
d = {}
for i in range(8):
    for s in a[i]:
        d[s] = 3+i # 각 알파벳과 그에 대응하는 숫자로 이루어진 딕셔너리 생성
l = [d[c] for c in input()]
print(sum(l))