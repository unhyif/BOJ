'''abcd가 d(n)의 생성자일 때
d(n) = 1000a+100b+10c+d+(a+b+c+d) = 1001a+101b+11c+2d
로 표현된다. (0 <= a <= 10, 0 <= b,c,d < 10, 단, a가 10일 땐 b=c=d = 0)'''

s = set()
for a in range(11):
    for b in range(10):
        for c in range(10):
            for d in range(10):
                s.add(1001*a+101*b+11*c+2*d) # 집합 s에 생성자를 가진 정수들을 모음
R = list(set(i for i in range(10001)).difference(s)) # 0이상 10000이하의 모든 정수 집합에서 s집합을 뺀 후(차집합), 리스트화 함
R.sort() # 정돈된 print를 위해 오름차순 정렬함
for r in R:
    print(r)