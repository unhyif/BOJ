for t in range(int(input())):
    x,y = map(int, input().split())
    n = 1 # 이동 과정 중 최대 이동 거리
    while n**2 <= y-x:
        if y-x < (n+1)**2:
            break # 최대 이동 거리 확정
        n += 1
    if n**2 == y-x:
        print(2*n-1)
    elif n**2 + n >= y-x:
        print(2*n)
    elif n**2 + 2*n >= y-x:
        print(2*n+1)