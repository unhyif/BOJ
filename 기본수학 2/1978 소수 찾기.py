n = int(input())
M = map(int, input().split())
L = [] # 소수 리스트
for m in M:
    if m == 1: pass
    elif m == 2: L.append(m)
    else:
        for k in range(2, m)
            if m % k == 0: # k가 m의 약수일 때
                break # m은 소수가 아님
        else: L.append(m) # 2이상 m미만 정수 중 m의 약수가 없었을 때
print(len(L))