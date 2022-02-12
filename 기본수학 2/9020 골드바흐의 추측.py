for t in range(int(input())):
    n = int(input())
    l = [0,0] + [1]*(n-1)
    for p in range(2, n//2 + 1):
        if l[p]:
            for q in range(2*p, n+1, p):
                l[q] = 0 # 소수가 아님을 표시
    for k in range(n//2, 1, -1): #두 수의 차이가 최소인 파티션을 찾기 위해
        if l[k] and l[n-k]: #k와 n-k가 소수일 때
            print(k, n-k)
            break