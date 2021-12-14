for t in range(int(input())):
    x,y = map(int, input().split())
    n = 1 # 이동 과정 중 최대 이동 거리
    while n**2 <= y-x:
        if y-x < (n+1)**2:
            break # 최대 이동 거리를 확정하기 위해
        n += 1
    if n**2 == y-x:
        print(2*n-1)
    elif n**2 + n >= y-x > n**2:
        print(2*n)
    elif n**2 + 2*n >= y-x > n**2 + n:
        print(2*n+1)
