M = int(input())
N = int(input())
l = [] # 소수 리스트
for i in range(M, N+1):
    if i > 1:
        if i == 2:
            l.append(i)
        else:
            for k in range(2, i//2+1):
                if i % k == 0: # k가 i의 약수일 때
                    break
            else: l.append(i)
if l: print(sum(l), min(l), sep="\n")
else: print(-1) # 소수가 없을 때