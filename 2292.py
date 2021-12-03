L = [1] # 벌집의 각 띠를 구성하는 수들의 최소값 리스트
for k in range(1000000000):
    a = 2+3*k*(k+1) # 두번째 띠부터의 최소값 생성 규칙
    if a > 1000000000:
        break # 10억이 포함된 띠까지만 고려하여 L을 구성함
    L.append(a)
n = int(input())
for i in range(len(L)-1): # n이 안쪽부터 몇 번째 띠에 속해 있는지를 찾는 과정
    if L[i] <= n < L[i+1]:
        print(i+1)
if L[-1] <= n: # n이 마지막 띠에 속해 있는 경우
    print(len(L))