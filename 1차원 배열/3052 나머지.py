S = set()
for i in range(10):
    S.add(int(input()) % 42)  # input으로 받은 값을 42로 나눈 나머지를 set에 넣어줌
print(len(S))
