N = int(input())
if N > 1:
    while N % 2 == 0: # 먼저, 가능할 때까지 2로 나누어 N을 홀수로 만들기
        print(2)
        N /= 2
    i = 3
    while i <= N//2: # 홀수가 된 N을 홀수 소인수로 나누기 (N == 3, 5일 때는 skip)
        while N % i == 0:
            print(i)
            N /= i
        i += 2
    if N > 1: # 최종 N이 1이 아닌 소수일 때
        print(int(N))