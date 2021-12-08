for t in range(int(input())):
    K = int(input())
    N = int(input())
    flr = 0 # 현재 층
    ppl = [_ for _ in range(1, N+1)] # 0층의 거주민 수 리스트
    temp = [0]*N
    while flr < K:
        flr += 1
        for n in range(N): # 새로운 층의 거주민 명수 리스트 생성 과정
            temp[n] = sum(ppl[:n+1]) # 이전 층의 1~n호 합
        ppl = temp[:]
    print(ppl[-1]) # K층 N호의 거주민 수