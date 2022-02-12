n = int(input())
while n: # n이 0이면 종료
    l = [0,0] + [1]*(2*n-1) # 0 ~ 2n 인덱스를 가진 요소 리스트
    if n == 1: print(1)
    else:
        for i in range(2, n+1):
            if l[i]: # l[i]가 소수일 때
                for k in range(2*i, 2*n+1, i):
                    l[k] = 0 # l[i의 배수]는 소수가 아님을 표시
        print(l[n+1:2*n+1].count(1)) # n초과 2n이하의 소수 개수
    n = int(input())