for i in range(int(input())): # 테스트 케이스 개수
    R,S = input().split() # 한 문자당 반복 횟수와 문자열
    l = [s*int(R) for s in S]
    print("".join(l))