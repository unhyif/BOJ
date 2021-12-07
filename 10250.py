for i in range(int(input())):
    H, W, N = map(int, input().split())
    if N % H == 0: # N이 H의 배수일 때
        flr = H
        no = N // H
    else:
        flr = N % H
        no = N // H + 1
    if no < 10:
        print(f"{flr}0{no}")
    else:
        print(f"{flr}{no}")