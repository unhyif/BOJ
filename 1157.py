S = input().upper()
d = {}
for s in S:
    if s not in d:
        d[s] = S.count(s) # 각 문자가 S에서 사용된 빈도수를 나타내는 딕셔너리
l = []
for k, v in d.items():
    if v == max(list(d.values())):
        l.append(k) # 가장 높은 사용 빈도수를 기록한 문자들의 리스트
if len(l) != 1:
    print("?")
else:
    print(*l)