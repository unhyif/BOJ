for t in range(int(input())):
    x_1, y_1, r_1, x_2, y_2, r_2 = map(int, input().split())
    d = ((x_1-x_2)**2 + (y_1-y_2)**2)**0.5 # 원의 중심 간의 거리
    r_sum = r_1 + r_2
    r_diff = r_1 - r_2
    if d == 0: # 원의 중심이 같을 때
        if r_diff == 0: # 두 원이 일치할 때
            print(-1)
        else:
            print(0)
    else: # 원의 중심이 다를 때
        if d > r_sum or d < abs(r_diff):
            print(0)
        elif d == r_sum or d == abs(r_diff): # 두 원이 접할 때
            print(1)
        else:
            print(2)