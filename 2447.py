def get_stars(l=[]): # 새로운 크기의 별 패턴을 생성하는 함수
    new_stars = []  # 새로운 패턴의 각 줄의 별들을 요소로 가질 리스트
    for i in range(len(l)*3): # 새로운 패턴의 total 줄 개수 == 직전 패턴의 3배
        if i // len(l) == 1: # 중앙의 공백 정사각형을 생성하기 위해
            new_stars.append(l[i%len(l)] + " "*len(l) + l[i%len(l)])
        else: # 나머지 줄들의 별들 생성
            new_stars.append(l[i%len(l)]*3)
    return new_stars

stars_by_line = ["***", "* *", "***"] # 크기 3의 초기 별 패턴
cnt = 0 # 함수 실행 횟수
n = int(input())
while n != 3: # 함수를 몇 번 실행해야 하는지 알기 위해
    n //= 3
    cnt += 1
for _ in range(cnt): # 크기 n의 별 패턴을 도출하기 위해
    stars_by_line = get_stars(stars_by_line) # 처음엔 크기 3의 별 패턴을 함수에 대입하여 새로운 패턴을 얻고, 그 패턴을 다시 매개변수에 전달
print("\n".join(stars_by_line)) # 최종 패턴의 모든 줄의 별들을 출력
