for i in range(int(input())): # 테스트 케이스의 개수를 입력 받음
    l = list(map(int, input().split())) # 각 테스트 케이스의 학생 수와 학생들의 점수 입력
    n = l.pop(0) # 테스트 케이스의 학생 수를 꺼냄
    l = list(filter(lambda x: x>sum(l)/n, l)) # l에서 평균이 넘는 점수를 받은 학생들을 필터링하여 l를 재정의
    print(f"{len(l)/n*100:.3f}" + "%") # 소수 셋째자리까지 표시 후 % 붙임