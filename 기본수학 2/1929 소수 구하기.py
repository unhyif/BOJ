M,N = map(int, input().split())
L = [0, 0] + [1]*(N-1) # 0 ~ N 인덱스를 가진 요소 리스트
for i in range(2, N//2 + 1): # N이 가질 수 있는 약수의 최솟값 2, 최댓값 N//2
    if L[i]: # L[i]이 소수일 때
        for k in range(2*i, N+1, i): # L[i의 배수]는 소수가 아님
            L[k] = 0 # 소수가 아님을 표시
for q in range(M, N+1):
    if L[q]: print(q) # M이상 N이하의 소수 출력